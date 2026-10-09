@echo off
title GTA KURD - بەستنەوەی داتای یاری (Setup Mirror)
cd /d "%~dp0"

echo ======================================================================
echo                  GTA KURD - بەستنەوەی داتای یاری (Mirror)
echo ======================================================================
echo.
echo Please enter the full path to your extracted mirror folder.
echo Example: C:\Users\%USERNAME%\Downloads\Compressed\mirror
echo.

set /p "USER_MIRROR=Mirror Folder Path: "

if not exist "%USER_MIRROR%\playgta5.com" (
    echo.
    echo [ERROR] The folder "%USER_MIRROR%" does not appear to contain playgta5.com.
    echo Please make sure you selected the folder containing "playgta5.com".
    pause
    exit /b 1
)

if exist "mirror" (
    echo Removing existing mirror link...
    rmdir "mirror"
)

echo Creating link...
mklink /J "mirror" "%USER_MIRROR%"
if errorlevel 1 (
    echo [ERROR] Failed to create link.
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Mirror linked successfully to GTA KURD!
echo You can now run Launch-GTA-KURD.cmd to play.
echo.
pause
