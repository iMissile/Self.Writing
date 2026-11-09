# Turns off ChatGPT desktop's start-at-login task (the Store app's StartupTask). No admin needed.
# Re-check after every ChatGPT reinstall/update - an update can switch it back on.
$root = 'HKCU:\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\SystemAppData'
$keys = Get-ChildItem $root -ErrorAction SilentlyContinue | Where-Object { $_.PSChildName -like 'OpenAI.Codex_*' }
if (-not $keys) { "  ChatGPT desktop (OpenAI.Codex) startup entry not found - nothing to do."; exit 0 }
foreach ($k in $keys) {
    $app = Join-Path $k.PSPath 'App'
    if (-not (Test-Path $app)) { continue }
    $before = (Get-ItemProperty $app).State
    Set-ItemProperty -Path $app -Name State -Value 0 -Type DWord
    Set-ItemProperty -Path $app -Name LastDisabledTime -Value ([DateTime]::UtcNow.ToFileTimeUtc()) -Type QWord
    "  {0}: State {1} -> 0 (disabled)" -f $k.PSChildName, $before
}
"  [OK] ChatGPT will no longer start by itself at login. Open it after the VPN is connected."
