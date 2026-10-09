# Start GTA KURD with Python runtime
Set-Location -Path $PSScriptRoot

$python = if (Test-Path "runtime\python.exe") { "runtime\python.exe" } else { "python" }

if (-not (Test-Path "mirror\playgta5.com")) {
    $common = "$env:USERPROFILE\Downloads\Compressed\mirror"
    if (Test-Path "$common\playgta5.com") {
        Write-Host "[*] Linking mirror from $common..." -ForegroundColor Cyan
        cmd /c mklink /J "mirror" "$common"
    }
}

Write-Host "==========================================================" -ForegroundColor Green
Write-Host "               GTA KURD - زمانی کوردیی سۆرانی" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "[*] Launching GTA KURD at http://localhost:8000/ ..." -ForegroundColor Cyan

& $python serve_local.py --open
