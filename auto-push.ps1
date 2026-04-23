Set-Location "C:\Users\Uto\Documents\Claude\canal-dark-oracao"
Write-Host "Gerando data.json..." -ForegroundColor Yellow
powershell -File ".\gerar-data.ps1"
$data = Get-Date -Format "dd/MM/yyyy HH:mm"
git add .
git commit -m "atualizacao "
git push
Write-Host "Painel online atualizado com sucesso!" -ForegroundColor Green
