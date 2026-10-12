# MEML 75 — Model of Single World Sheet

**Version 75** | 2026

---

## About

MEML 75 is a version of the geometric model of particle identity on the $T^2/\mathbb{Z}_3$ orbifold in six-dimensional spacetime. The model eliminates two of three free parameters of the original version by deriving them from the geometry of compactified space.

## Key results

| Quantity | Value | Status |
|---|---|---|
| α_G | 2/(3π) = 0.212207 | Derived from SU(3), N_f=1 |
| m_KK | 1.044 × 10¹⁵ GeV | Derived from radion equation |
| M_6 | 1.485 × 10¹⁷ GeV | Derived from reduction |
| ε | 2.861 × 10⁻⁴ | Derived from KK summation |
| k | 0.1068 | Calibrated to I = 0.3653 |
| I | 0.365275 | Conditionally derived |
| θ_i | 0.9483 | Initial condition |
| Ω_a h² | 0.119832 | Agreement with Planck 2018 (0.02%) |
| ν_a | 1.362 GHz | ADMX target |

## Parameter status

- **Strictly derived:** α_G, m_KK, M_6, ε (4 parameters)
- **Conditionally derived:** I (1 parameter, requires k)
- **Calibrated:** k = 0.1068 (1 parameter)
- **Model-dependent:** σ₀²/V_orb = 0.06 (1 parameter)
- **Initial condition:** θ_i = 0.9483 (1 parameter)

The model is **partially predictive**: given fixed parameters, it uniquely predicts Ω_a h², f_a, m_a, ν_a.

## Files

| File | Description |
|---|---|
| `MEML_75_theory.tex` | Theoretical paper (XeLaTeX) |
| `meml_75_calculations.py` | Numerical computation of all quantities |
| `requirements.txt` | Python dependencies |
| `run.bat` / `run.sh` | Launcher scripts |
| `README_EN.md` | Project description |

## Quick start

### Install dependencies

```bash
pip install -r requirements.txt