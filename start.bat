@echo off
TITLE MB

cd /d %~dp0

REM Check for uv
where uv >nul 2>&1
if errorlevel 1 goto install_uv

REM Create venv if missing
if not exist .venv (
    uv venv .venv
)

REM Install dependencies (fast, cached)
uv pip install -r requirements.txt

REM Run script inside uv venv
uv run pyeamu.py

goto :EOF

:install_uv
echo uv is not installed.
echo Install it from:
echo https://docs.astral.sh/uv/
echo:
echo Windows (PowerShell):
echo   iwr https://astral.sh/uv/install.ps1 -UseBasicParsing ^| iex
echo:
pause
