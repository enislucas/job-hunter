"""Job Hunter local server: serves the app AND saves commits straight to disk.

Also serves the whole Job Hunter folder read-only over http://127.0.0.1:7345/
(dashboard.html by default), so the app runs same-origin with its saver and
browser policies can never block a commit.

Endpoints: GET /ping, POST /save {"name","content"}, POST /upload {"name","content_base64"}
(document harvest for onboarding: PDF, DOCX, images, text into inputs/onboarding-drops/),
GET /uploads (list what arrived), GET /<any file under the folder>.
Loopback only. Whitelisted save names and upload extensions only. Autostarts via the
Startup shortcut JobHunter-Saver; the pipeline's gate step restarts it if down.

ROOT is resolved relative to this file, so the repo works wherever it is cloned.
"""
import base64
import json
import re
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DROPS = ROOT / "inputs" / "corrections-drops"
ONBOARD = ROOT / "inputs" / "onboarding-drops"
ARCH = ROOT / "archive" / "corrections"
LOG = ROOT / "runner" / "saver.log"
MAX_BYTES = 200_000
UPLOAD_MAX = 28_000_000  # ~20 MB file after base64 inflation
UPLOAD_EXT = {".pdf", ".docx", ".doc", ".txt", ".md", ".png", ".jpg", ".jpeg", ".rtf", ".odt"}

TYPES = {
    ".html": "text/html; charset=utf-8", ".md": "text/plain; charset=utf-8",
    ".ico": "image/x-icon", ".png": "image/png", ".svg": "image/svg+xml",
    ".pdf": "application/pdf", ".css": "text/css", ".js": "text/javascript",
    ".json": "application/json",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}


def log(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " | " + msg + "\n")


def stamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def route(name):
    if name == "search-preferences.md":
        return ("replace", ROOT / "inputs" / "search-preferences.md")
    if name == "skill-test-results.md":
        return ("replace", ROOT / "inputs" / "skill-test-results.md")
    if re.fullmatch(r"journey-update[\w ()-]*\.md", name):
        return ("drop", DROPS / f"journey-update-{stamp()}.md")
    if re.fullmatch(r"[\w][\w .()-]*-feedback\.md", name):
        return ("drop", DROPS / f"{stamp()}-{name}")
    if re.fullmatch(r"test-request[\w ()-]*\.md", name):
        return ("drop", DROPS / f"test-request-{stamp()}.md")
    return None


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json(self, code, payload):
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.send_response(200); self._cors(); self.end_headers()

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == "/ping":
            self._json(200, b'{"ok": true}'); return
        if path == "/creed":
            body = ("verify before you trust. commit before you forget.\n"
                    "let the machine hunt, filter and write, but never let it press send.\n"
                    "rejection is data. honesty is leverage.\n").encode("utf-8")
            self.send_response(200); self._cors()
            self.send_header("Content-Type", "text/plain; charset=utf-8"); self.end_headers()
            self.wfile.write(body); return
        if path == "/uploads":
            try:
                items = []
                if ONBOARD.is_dir():
                    for f in sorted(ONBOARD.iterdir()):
                        if f.is_file() and f.name != "README.md":
                            items.append({"name": f.name, "kb": round(f.stat().st_size / 1024)})
                self._json(200, json.dumps({"ok": True, "files": items}).encode("utf-8"))
            except Exception as e:  # noqa: BLE001
                log(f"UPLOADS LIST ERROR {e}")
                self._json(500, b'{"ok": false}')
            return
        rel = path.lstrip("/") or "dashboard.html"
        try:
            target = (ROOT / rel).resolve()
            if not str(target).startswith(str(ROOT)) or not target.is_file():
                self._json(404, b'{"ok": false}'); return
            data = target.read_bytes()
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", TYPES.get(target.suffix.lower(), "application/octet-stream"))
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:  # noqa: BLE001
            log(f"GET ERROR {path}: {e}")
            self._json(500, b'{"ok": false}')

    def do_POST(self):
        if self.path == "/upload":
            try:
                n = int(self.headers.get("Content-Length", 0))
                if n > UPLOAD_MAX:
                    self._json(413, b'{"ok": false, "why": "file too large (20 MB cap)"}'); return
                data = json.loads(self.rfile.read(n).decode("utf-8"))
                name = Path(str(data["name"])).name
                if Path(name).suffix.lower() not in UPLOAD_EXT:
                    log(f"UPLOAD REFUSED {name}")
                    self._json(403, b'{"ok": false, "why": "extension not allowed"}'); return
                ONBOARD.mkdir(parents=True, exist_ok=True)
                target = ONBOARD / name
                if target.exists():
                    target = ONBOARD / f"{Path(name).stem}-{stamp()}{Path(name).suffix}"
                target.write_bytes(base64.b64decode(str(data["content_base64"])))
                log(f"uploaded {target.name} ({target.stat().st_size} bytes)")
                self._json(200, json.dumps({"ok": True, "saved_as": target.name}).encode("utf-8"))
            except Exception as e:  # noqa: BLE001
                log(f"UPLOAD ERROR {e}")
                self._json(500, b'{"ok": false}')
            return
        if self.path != "/save":
            self._json(404, b'{"ok": false}'); return
        try:
            n = int(self.headers.get("Content-Length", 0))
            if n > MAX_BYTES:
                raise ValueError("too large")
            data = json.loads(self.rfile.read(n).decode("utf-8"))
            name = Path(str(data["name"])).name
            target = route(name)
            if target is None:
                log(f"REFUSED {name}")
                self._json(403, b'{"ok": false, "why": "name not whitelisted"}'); return
            mode, path = target
            path.parent.mkdir(parents=True, exist_ok=True)
            if mode == "replace" and path.exists():
                ARCH.mkdir(parents=True, exist_ok=True)
                path.replace(ARCH / f"{path.stem}-{stamp()}{path.suffix}")
            path.write_text(str(data["content"]), encoding="utf-8")
            log(f"saved {name} -> {path}")
            self._json(200, b'{"ok": true}')
        except Exception as e:  # noqa: BLE001
            log(f"POST ERROR {e}")
            self._json(500, b'{"ok": false}')

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    log("saver starting on http://127.0.0.1:7345 (app + save)")
    ThreadingHTTPServer(("127.0.0.1", 7345), Handler).serve_forever()
