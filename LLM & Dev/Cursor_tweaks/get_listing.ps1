function Get-CustomChildItem {
    param(
        [string]$Path = '.'
    )
    # List all items (including hidden) in the specified path
    Get-ChildItem -LiteralPath $Path -Force | ForEach-Object {
        if ($_.PSIsContainer) {
            # If directory name starts with a dot, skip it (and don't recurse)
            if ($_.Name -match '^\.') {
                return
            }
            else {
                # Output the directory, then recurse into it
                $_
                Get-CustomChildItem -Path $_.FullName
            }
        }
        else {
            # Output file
            $_
        }
    }
}

# Get the current working directory
$cwd = Get-Location

# Use the custom function, then convert each full path into a relative path
Get-CustomChildItem | ForEach-Object {
    # Compute the relative path by removing the current working directory prefix.
    # The +1 removes the trailing backslash.
    $_.FullName.Substring($cwd.Path.Length + 1)
} | Out-File -FilePath "_listing.txt" -Encoding UTF8
