@echo off
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    exit /b 1
)

python passcraft.py %*