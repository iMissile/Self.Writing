# -----------------------------------------------------------------------------
# Environment
# -----------------------------------------------------------------------------

$env:UV_CACHE_DIR = 'D:\uv-cache'


# -----------------------------------------------------------------------------
# Encoding
# -----------------------------------------------------------------------------

$utf8 = [System.Text.UTF8Encoding]::new($false)

$OutputEncoding = $utf8
[Console]::InputEncoding  = $utf8
[Console]::OutputEncoding = $utf8


# -----------------------------------------------------------------------------
# PSReadLine
# -----------------------------------------------------------------------------

if (Get-Module -ListAvailable -Name PSReadLine) {
    Import-Module PSReadLine

    # Tab: interactive completion menu
    Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

    # Ctrl+Space: show all completion variants
    Set-PSReadLineKeyHandler -Key Ctrl+Spacebar -Function MenuComplete

    # History search using arrows
    Set-PSReadLineKeyHandler -Key UpArrow   -Function HistorySearchBackward
    Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward

    # Inline suggestions based on command history
    Set-PSReadLineOption -PredictionSource History
    Set-PSReadLineOption -PredictionViewStyle InlineView

    # Accept inline suggestion
    Set-PSReadLineKeyHandler -Key RightArrow -Function ForwardChar
}


# -----------------------------------------------------------------------------
# Prompt
# -----------------------------------------------------------------------------

# Uncomment if/when you want oh-my-posh:
# oh-my-posh init pwsh | Invoke-Expression