# MEML 75 — Model of Single World Sheet

[![Version](https://img.shields.io/badge/version-75-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)]()
[![LaTeX](https://img.shields.io/badge/LaTeX-XeLaTeX-green.svg)]()

**Version B (ADMX-HF)** | 2026

---

## About

**MEML 75** is a version of the geometric model of particle identity 
on the $T^2/\mathbb{Z}_3$ orbifold in six-dimensional spacetime.

Version B uses the standard **reduced Planck mass** 
$M_{Pl}^{\text{red}} = 2.435\times 10^{18}$ GeV, and the axion decay 
constant $f_a$ is **derived from first principles** as 
$f_a = M_{Pl}^{\text{red}}\varepsilon^2$. This is the key difference 
from MEML 74, where $f_a$ was phenomenologically normalized.

---

## Key results

| Quantity | Value | Status |
|---|---|---|
| $M_{Pl}^{\text{red}}$ | $2.435\times 10^{18}$ GeV | Standard convention |
| $\alpha_G$ | $2/(3\pi) = 0.212207$ | Derived |
| $m_{KK}$ | $2.084\times 10^{14}$ GeV | Derived |
| $M_6$ | $2.965\times 10^{16}$ GeV (≈ GUT) | Derived |
| $\varepsilon$ | $2.861\times 10^{-4}$ | Derived |
| $f_a$ | $1.993\times 10^{11}$ GeV | **Derived** |
| $m_a$ | $28.22$ μeV | Prediction |
| $\nu_a$ | $6.825$ GHz | Prediction (ADMX-HF) |
| $\Omega_a h^2$ | $0.119832$ | Planck 2018 (0.14%) |
| $g_{a\gamma\gamma}$ | $1.119\times 10^{-14}$ GeV⁻¹ | Prediction |
| $M_{BH}$ | $0.63\,M_\oplus$ | PBH |
| $R_g$ | $5.59$ mm | Schwarzschild radius |
| $T_H$ | $2.807$ μeV $< m_a$ | Hawking channel closed |
| $\tau_{SR}$ | $0.854$ μs | Superradiance |

---

## Parameter status

- **Strictly derived:** $\alpha_G$, $m_{KK}$, $\varepsilon$, $f_a$ (4)
- **Conditionally derived:** $\mathcal{I}$ (1)
- **Calibrated:** $k = 0.1068$ (1)
- **Model-dependent:** $\sigma_0^2/V_{\text{orb}} = 0.06$ (1)
- **Initial condition:** $\theta_i = 2.0043$ (1)

**Single calibrated parameter:** $k = 0.1068$.

---

## Quick start

### Install dependencies
```bash
pip install -r requirements.txt