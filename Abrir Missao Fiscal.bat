@echo off
chcp 65001 >nul
title Missão Fiscal - servidor local
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python nao encontrado. Instale o Python 3 e tente de novo.
  pause
  exit /b 1
)
python sistema\gerar.py --servir --abrir
echo.
pause
