$root = "C:\Users\Uto\Documents\Claude\canal-dark-oracao"
$files = @()
Get-ChildItem -Path $root -Recurse -Include "*.md","*.txt" | ForEach-Object {
    $rel = $_.FullName.Replace($root + "\", "").Replace("\", "/")
    $content = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    $files += [PSCustomObject]@{
        name    = $_.Name
        path    = $rel
        content = $content
        size    = $_.Length
        mtime   = $_.LastWriteTime.ToString("yyyy-MM-ddTHH:mm:ss")
    }
}
$json = $files | ConvertTo-Json -Depth 3 -Compress
[System.IO.File]::WriteAllText("$root\data.json", $json, [System.Text.Encoding]::UTF8)
Write-Host "data.json gerado com $($files.Count) arquivos"
