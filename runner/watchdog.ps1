# Job Hunter watchdog: alarms only on true silence during a long unattended run.
#
# Paths are relative to this script (runner\), so it works wherever you cloned
# the repo. Register it as a user-level scheduled task for the duration of a long
# run, then disable it at cleanup. Example registration (run once, from the repo
# root, adjust the trigger interval to taste):
#
#   $wd = Join-Path (Get-Location) 'runner\watchdog.ps1'
#   $action  = New-ScheduledTaskAction -Execute 'powershell.exe' `
#               -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$wd`""
#   $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
#               -RepetitionInterval (New-TimeSpan -Minutes 15)
#   Register-ScheduledTask -TaskName 'JobHunter-Watchdog' -Action $action -Trigger $trigger
#
# To silence it without unregistering, create runner\watchdog-off.txt.
# To remove it at cleanup:  Unregister-ScheduledTask -TaskName 'JobHunter-Watchdog' -Confirm:$false

$root   = Split-Path -Parent $PSScriptRoot   # repo root (parent of runner\)
$runner = $PSScriptRoot

Get-Date -Format "yyyy-MM-dd HH:mm:ss" | Set-Content (Join-Path $runner "watchdog-last.txt") -Encoding utf8
if (Test-Path (Join-Path $runner "watchdog-off.txt")) { exit }

$hb = Join-Path $runner "heartbeat.txt"
$stale = $true
if (Test-Path $hb) {
  $age = (Get-Date) - (Get-Item $hb).LastWriteTime
  if ($age.TotalMinutes -lt 35) { $stale = $false }
}
if ($stale) {
  1..3 | ForEach-Object { [console]::beep(880,200); [console]::beep(880,200); [console]::beep(440,700); Start-Sleep -Milliseconds 400 }
  Add-Type -AssemblyName System.Speech
  $v = New-Object System.Speech.Synthesis.SpeechSynthesizer
  $v.Speak("Job Hunter has been silent for over thirty five minutes. Please check the Claude session in the Job Hunter folder. This needs one minute of your time.")
}
