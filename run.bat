@echo off
REM ============================================================
REM  MEML 75 -- Launcher for Windows
REM  Запуск численных расчётов модели MEML 75 (Версия B)
REM ============================================================

title MEML 75 -- Numerical Calculations

echo ============================================================
echo   MEML 75 -- Numerical Calculation
echo   MEML 75 -- Численный расчёт
echo ============================================================
echo.

REM --- Проверка Python ---
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found in PATH.
    echo [ОШИБКА] Python не найден в PATH.
    echo.
    echo Установите Python с https://www.python.org/downloads/
    pause
    exit /b 1
)

REM --- Установка зависимостей ---
echo [1/3] Installing dependencies from requirements.txt ...
echo [1/3] Установка зависимостей из requirements.txt ...
python -m pip install -q -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies.
    echo [ОШИБКА] Не удалось установить зависимости.
    pause
    exit /b 1
)

REM --- Космология ---
echo.
echo [2/3] Running meml_75_calculations.py ...
echo [2/3] Запуск meml_75_calculations.py ...
echo.
python meml_75_calculations.py

REM --- Астрофизика ---
echo.
echo [3/3] Running MEML75_BH.py ...
echo [3/3] Запуск MEML75_BH.py ...
echo.
python MEML75_BH.py

echo.
echo ============================================================
echo   Calculation finished. / Расчёт завершён.
echo ============================================================
pause