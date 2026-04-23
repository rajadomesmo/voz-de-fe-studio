# Script que varre todos os arquivos do projeto e gera data.json para o painel online
$root = "C:\Users\Uto\Documents\Claude\canal-dark-oracao"
$files = @()

Get-ChildItem -Path $root -Recurse -Include "*.md","*.txt" | ForEach-Object {
    $rel = $_.FullName.Replace($root + "\", "").Replace("\", "/")
    $skip = @("gerar-data.ps1")
    if ($skip -notcontains $_.Name) {
        $files += @{
            name    = $_.Name
            path    = $rel
            content = (Get-Content $_.FullName -Raw -Encoding UTF8)
            size    = $_.Length
            mtime   = $_.LastWriteTime.ToString("yyyy-MM-ddTHH:mm:ss")
        }
    }
}

$json = $files | ConvertTo-Json -Depth 3
$json | Out-File -FilePath "$root\data.json" -Encoding utf8
Write-Host "data.json gerado com $($files.Count) arquivos"



