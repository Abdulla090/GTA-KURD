@echo off
title GTA KURD - زمانی کوردیی سۆرانی
cd /d "%~dp0"

echo ======================================================================
echo                      GTA KURD (GTA V Kurdish)
echo                 GTA V بە زمانی کوردیی سۆرانی لە براوسەر
echo ======================================================================
echo.

:: 1. Check Python runtime
if exist "runtime\python.exe" (
    set "PYTHON_EXE=runtime\python.exe"
) else (
    where python >nul 2>&1
    if not errorlevel 1 (
        set "PYTHON_EXE=python"
    ) else (
        echo [ERROR] Python runtime is not found in runtime\python.exe or system PATH.
        echo Please make sure the runtime folder is included.
        pause
        exit /b 1
    )
)

:: 2. Auto-detect mirror directory if not linked
if not exist "mirror\playgta5.com" (
    echo [!] Mirror directory is not currently linked.
    echo [*] Checking common download locations...
    
    if exist "%USERPROFILE%\Downloads\Compressed\mirror\playgta5.com" (
        echo [*] Found mirror at "%USERPROFILE%\Downloads\Compressed\mirror"!
        echo [*] Linking automatically...
        mklink /J "mirror" "%USERPROFILE%\Downloads\Compressed\mirror"
    ) else if exist "%USERPROFILE%\Downloads\mirror\playgta5.com" (
        echo [*] Found mirror at "%USERPROFILE%\Downloads\mirror"!
        echo [*] Linking automatically...
        mklink /J "mirror" "%USERPROFILE%\Downloads\mirror"
    ) else if exist "..\playgta5\mirror\playgta5.com" (
        echo [*] Found mirror in sibling playgta5 directory!
        mklink /J "mirror" "..\playgta5\mirror"
    ) else (
        echo.
        echo [NOTICE] Full game assets mirror not found.
        echo The Kurdish UI and intro screens will run using bundled assets.
        echo To play the full game, run Setup-Mirror.cmd to link your mirror folder.
        echo.
    )
)

echo [*] Starting GTA KURD server at http://localhost:8000/ ...
echo [*] Press Ctrl+C in this window to stop the server.
echo.

%PYTHON_EXE% serve_local.py --open

if errorlevel 1 (
    echo.
    echo [!] The server could not start or was closed.
    pause
)
