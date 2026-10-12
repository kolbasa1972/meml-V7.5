#!/usr/bin/env bash
# ============================================================
#  MEML 75 -- Launcher for Linux / macOS
#  Запуск численных расчётов модели MEML 75 (Версия B)
# ============================================================

set -e

echo "============================================================"
echo "  MEML 75 -- Numerical Calculation"
echo "  MEML 75 -- Численный расчёт"
echo "============================================================"
echo

# --- Проверка Python ---
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 not found in PATH."
    echo "[ОШИБКА] python3 не найден в PATH."
    echo
    echo "Установите Python 3:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  macOS:         brew install python3"
    exit 1
fi

# --- Установка зависимостей ---
echo "[1/3] Installing dependencies from requirements.txt ..."
echo "[1/3] Установка зависимостей из requirements.txt ..."
python3 -m pip install -q -r requirements.txt

# --- Космология ---
echo
echo "[2/3] Running meml_75_calculations.py ..."
echo "[2/3] Запуск meml_75_calculations.py ..."
echo
python3 meml_75_calculations.py

# --- Астрофизика ---
echo
echo "[3/3] Running MEML75_BH.py ..."
echo "[3/3] Запуск MEML75_BH.py ..."
echo
python3 MEML75_BH.py

echo
echo "============================================================"
echo "  Calculation finished. / Расчёт завершён."
echo "============================================================"