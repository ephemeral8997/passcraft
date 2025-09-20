@echo off
set SCRIPT_DIR=%~dp0

where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    exit /b 1
)


python "%SCRIPT_DIR%passcraft.py" %*