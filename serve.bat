@echo off
cd /d "%~dp0"

set "PORT=8000"
set "URL=http://localhost:%PORT%/index.html"

for /f "delims=" %%a in ('powershell -NoProfile -Command "(Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notmatch '^(169\.254|127\.)' -and $_.PrefixOrigin -ne 'WellKnown'} | Select-Object -ExpandProperty IPAddress | Select-Object -First 1)"') do set "LOCALIP=%%a"

if defined LOCALIP (
    set "PHONE_URL=http://%LOCALIP%:%PORT%/index.html"
) else (
    set "PHONE_URL=http://<tu-ip-local>:%PORT%/index.html"
)

echo Iniciando servidor local en %URL%
if defined LOCALIP echo Abre en tu telefono usando: %PHONE_URL%

echo Buscando Python 3...
start "Servidor local" cmd /k "py -3 -m http.server %PORT% --bind 0.0.0.0 2>nul || python -m http.server %PORT% --bind 0.0.0.0 2>nul || npx http-server . -p %PORT% -a 0.0.0.0 2>nul || powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0serve.ps1""

echo Espera unos segundos mientras se inicia el servidor...
timeout /t 2 /nobreak >nul

echo Abriendo en Google Chrome...
where chrome >nul 2>nul
if %errorlevel%==0 (
    start "" chrome "%URL%"
) else (
    if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
        start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "%URL%"
    ) else if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
        start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" "%URL%"
    ) else (
        echo No se encontro Google Chrome. Abriendo navegador predeterminado...
        start "" "%URL%"
    )
)

echo Si el navegador no abre, visita manualmente: %URL%
if defined LOCALIP echo Si quieres verlo en tu telefono, usa: %PHONE_URL%
