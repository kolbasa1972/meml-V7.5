#!/usr/bin/env bash
# ============================================================
#  MEML 75 -- Launcher for Linux / macOS
# ============================================================

set -e

echo "============================================================"
echo "  MEML 75 -- Numerical Calculation"
echo "  MEML 75 -- Численный расчёт"
echo "============================================================"
echo

if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 not found in PATH."
    exit 1
fi

echo "[1/2] Installing dependencies from requirements.txt ..."
python3 -m pip install -q -r requirements.txt

echo
echo "[2/2] Running meml_75_calculations.py ..."
echo
python3 meml_75_calculations.py

echo
echo "============================================================"
echo "  Calculation finished. / Расчёт завершён."
echo "============================================================"