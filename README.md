Сбалансированный (Идеально для JHEP / Physical Review Letters)
# MEML 7.5 — Model of a Single World Sheet

## Covariant Orbifold Normalization on T²/Z₃, Derivation of the Gauge 
## Coupling and the Suppression Factor from Geometry

**Author:** Yurov D. V.  
**Year:** 2026  
**Status:** speculative toy model within 6D QFT

---

## Abstract

Version MEML 7.5 addresses the two main open problems of previous revisions 
(v7.0–9.7): the phenomenological status of the bulk coupling constant α_G 
and the dimensionless suppression factor ε.

**Honest verdict:** α_G and ε receive a **conditional interpretation** 
through orbifold geometry, but a **complete first-principles derivation 
is not achieved**. The modular integral I = 0.3653 remains a **postulate**, 
and its calibration parameter k = 0.1068 is a **phenomenological input**.

---

## 1. Geometry

### 1.1. Topology

We consider six-dimensional spacetime:

    M₆ = M₄ × T²/Z₃

where:
- **M₄** — 4D Minkowski spacetime;
- **T² = ℂ/Λ** — two-dimensional torus, Λ = ℤ + τℤ;
- **τ = e^{iπ/3} = 1/2 + i√3/2** — complex structure;
- **Z₃** — discrete group: z → ωz, ω = e^{2πi/3}.

### 1.2. Fixed Points

Three fixed points of the orbifold:

    z₀ = 0
    z₁ = (1+τ)/3
    z₂ = (2+2τ)/3

Each point corresponds to **one generation** of the SM particles.

### 1.3. Fundamental Domain

Area of the orbifold fundamental domain:

    V_orb = V₂/3 = 1/(3·m_KK²)

where V₂ = 1/m_KK² is the area of the covering torus.

---

## 2. Radion Equation

The torus radius is fixed by the balance of non-perturbative effects:

    R_T² = √I · M_Pl⁻¹ · exp(2π/(3α_G)) = 1/m_KK

where:
- M_Pl = 1.22 × 10¹⁹ GeV — unreduced Planck mass;
- I = 0.3653 — graviton zero-mode modular integral;
- α_G — bulk SU(5) coupling;
- m_KK — compactification scale.

---

## 3. Derivation of α_G (Conditional)

### 3.1. Formula

From non-perturbative moduli stabilization (KKLT approach):

    α_G = b₀/(12π),    b₀ = 3N − N_f

where N is the rank of the hidden group SU(N), and N_f is the number of 
matter flavors.

### 3.2. Group Choice

| Group | N_f | b₀ | α_G | Deviation from target 0.21128 |
|---|---|---|---|---|
| SU(2) | 0 | 6 | 0.1592 | −24.7% |
| SU(3) | 0 | 9 | 0.2387 | +13.0% |
| **SU(3)** | **1** | **8** | **0.21221** | **+0.44%** |
| SU(3) | 2 | 7 | 0.1857 | −12.1% |
| SU(4) | 4 | 8 | 0.21221 | +0.44% |

**Optimum:** α_G = 2/(3π) ≈ 0.212207.

### 3.3. Honest Caveats

- **SU(3) with N_f = 1 is not a unique choice.** SU(4) with N_f = 4 gives 
  the same α_G. The arbitrariness of the choice is not resolved.
- The +0.44% deviation from the empirical α_G = 0.21128 is attributed to 
  threshold corrections from light KK modes, but has **not been verified 
  numerically**.

**Status:** conditionally derived.

---

## 4. Scales

### 4.1. Compactification Scale

    m_KK = M_Pl/(√I · exp(π²)) ≈ 1.044 × 10¹⁵ GeV

**Note:** in v9.7, m_KK = 10¹⁵ GeV; in v7.5, m_KK = 1.044 × 10¹⁵ GeV. 
The +4.4% discrepancy **changes** R_T².

### 4.2. 6D Gravitational Scale

    M₆ = (3 · M_Pl² · m_KK²)^{1/4} ≈ 1.4853 × 10¹⁷ GeV

**Note:** in v9.7, M₆ = 1.4537 × 10¹⁷ GeV; the discrepancy is +2.2%.

### 4.3. Scalar Scale

    M* = M₆ · ε

---

## 5. Suppression Factor ε (Conditional)

### 5.1. Formula

    ε = x² · [1 + c₃′·x + c₄′·x² + c₅′·x³ + ...]

where x = α_G/(4π) ≈ 0.016887.

### 5.2. Coefficients

From the script MEML7.5.py:

    c₃′ = 0.192
    c₄′ = 0.0203
    c₅′ = 0.00271

**Problem:** these coefficients are **not derived** from diagrammatic 
contractions. They are **fitted** to obtain ε = 2.861 × 10⁻⁴.

### 5.3. Numerical Result

    ε = 2.860924 × 10⁻⁴
    Target: 2.861 × 10⁻⁴
    Deviation: −0.0027%

**Status:** conditionally derived (coefficients fitted).

---

## 6. Modular Integral I (Postulate)

### 6.1. Definition

    I = ∫_{T²/Z₃} |Ψ_g(z,z̄)|² d²z

where Ψ_g is the graviton zero-mode wavefunction.

### 6.2. Gaussian Warp Factor Model

    A(z,z̄) = −k · Σⱼ exp(−|z−zⱼ|²/(2σ₀²))

Parameters:
- **k = 0.1068** — well depth;
- **σ₀²/V_orb = 0.06** — well width.

### 6.3. Monte Carlo Calculation

    J = ⟨exp(2A)⟩ = 0.91255
    I = V_orb/J = 0.36528

**Analytic check:** J_analytic = 0.91214, I_analytic = 0.36544. 
Agreement: 0.045%.

### 6.4. Honest Status

**k = 0.1068 is a calibration parameter.** It is **fitted** to I = 0.3653.

**Attempt to derive k from deficit angle δ = 4π/3:**
- Simple formula: k ≈ 0.709 → gives J ≠ 0.9126
- At σ₀ = 1/m_KK: k ≈ 0.018 or 1.016 → J = 0.9126 (fit)

**Conclusion:** k is **not derived** from the defect geometry by simple 
formulas.

**Status:** postulate.

---

## 7. Cosmological Consequences

### 7.1. Peccei–Quinn Decay Constant

    f_a = M_Pl · ε² ≈ 9.9856 × 10¹¹ GeV

### 7.2. Axion Mass

    m_a = Λ_QCD²/f_a ≈ 5.633 × 10⁻⁶ eV

where Λ_QCD = 0.075 GeV.

### 7.3. Signal Frequency

    ν_a = m_a c²/h ≈ 1.3621 GHz

### 7.4. Relic Density

    Ω_a h² = 0.120 · (f_a/10¹²)^{7/6} · θ_i² · f_anh(θ_i)

At θ_i = 0.9483:

    Ω_a h² = 0.119832

**Deviation from Planck 2018 (0.120 ± 0.001): ~0.14%.**

---

## 8. Honest Status of Parameters

| Parameter | Value | Status | Comment |
|---|---|---|---|
| **α_G** | 0.21221 | Conditionally derived | SU(3), N_f=1 choice arbitrary |
| **ε** | 2.861 × 10⁻⁴ | Conditionally derived | Coefficients c_i′ fitted |
| **I** | 0.3653 | **Postulate** | k = 0.1068 calibrated |
| **θ_i** | 0.9483 | Free | Cosmological initial condition |
| **m_KK** | 1.044 × 10¹⁵ GeV | Derived from radion equation | From α_G and I |
| **M₆** | 1.4853 × 10¹⁷ GeV | Derived | From m_KK and M_Pl |

---

## 9. Open Problems

1. **6D anomalies of SU(5) on T²/Z₃.** Not checked.
2. **Derivation of α_G.** SU(3) with N_f=1 is an arbitrary choice.
3. **Derivation of ε.** Coefficients c_i′ fitted.
4. **Derivation of I.** k = 0.1068 calibrated.
5. **Derivation of θ_i.** Inflationary dynamics required.
6. **Einstein equations.** Metric not solved.
7. **Stability of torus defects.** Not checked.
8. **SM particle spectrum.** Not derived.

---

## 10. Conclusion

MEML 7.5 is **not a complete theory**. It is a **toy model** in which:
- α_G receives a **conditional interpretation** through SU(3), N_f=1;
- ε is reproduced by a **radiative series** with fitted c_i′;
- I is **calibrated** through the parameter k;
- θ_i **remains free** as an initial condition.

**Overall status:** 2 parameters conditionally interpreted, 1 postulated, 
1 free. **Elimination of free parameters has not been achieved.**

---

## 11. Recommendations for Further Work

1. **Derive c_i′ from KK loop diagrams.**
2. **Derive k from deficit angle δ = 4π/3.**
3. **Justify the choice SU(3), N_f=1** through anomalies or generation number.
4. **Check 6D anomalies** by explicit calculation of I₈ on T²/Z₃.
5. **Derive θ_i from inflationary dynamics.**
6. **Solve 6D Einstein equations** for exact metric.

---

**Keywords:** extra dimensions, 6D QFT, T²/Z₃ orbifold, axion, dark matter, 
superradiance, black holes, ADMX.

**Links:**
- GitHub: github.com/kolbasa1972/meml-V9.6
- Zenodo: 10.5281/zenodo.23289871


# MEML 7.5 — Модель единого мирового листа

## Ковариантная нормировка орбифолда T²/Z₃, вывод калибровочной константы 
## и фактора подавления из геометрии

**Автор:** Юров Д. В.  
**Год:** 2026  
**Статус:** спекулятивная игрушечная модель в рамках 6D КТП

---

## Аннотация

Версия MEML 7.5 посвящена решению двух главных открытых проблем 
предыдущих ревизий : феноменологического статуса bulk-константы 
связи α_G и безразмерного фактора подавления ε. 

**Честный итог:** α_G и ε получают **условную интерпретацию** через геометрию 
орбифолда, но **полного вывода из первых принципов не достигнуто**. 
Модулярный интеграл I = 0.3653 остаётся **постулатом**, а его калибровочный 
параметр k = 0.1068 — **феноменологическим входом**.

---

## 1. Геометрия

### 1.1. Топология

Рассматривается шестимерное пространство-время:

    M₆ = M₄ × T²/Z₃

где:
- **M₄** — 4D-пространство Минковского;
- **T² = ℂ/Λ** — двумерный тор, Λ = ℤ + τℤ;
- **τ = e^{iπ/3} = 1/2 + i√3/2** — комплексная структура;
- **Z₃** — дискретная группа: z → ωz, ω = e^{2πi/3}.

### 1.2. Неподвижные точки

Три фиксированные точки орбифолда:

    z₀ = 0
    z₁ = (1+τ)/3
    z₂ = (2+2τ)/3

Каждая точка соответствует **одному поколению** частиц СМ.

### 1.3. Фундаментальная область

Площадь фундаментальной области орбифолда:

    V_orb = V₂/3 = 1/(3·m_KK²)

где V₂ = 1/m_KK² — площадь накрывающего тора.

---

## 2. Уравнение радиона

Радиус тора фиксируется балансом непертурбативных эффектов:

    R_T² = √I · M_Pl⁻¹ · exp(2π/(3α_G)) = 1/m_KK

где:
- M_Pl = 1.22 × 10¹⁹ ГэВ — неприведённая масса Планка;
- I = 0.3653 — модулярный интеграл нулевой моды гравитона;
- α_G — bulk-константа связи SU(5);
- m_KK — масштаб компактификации.

---

## 3. Вывод α_G (условный)

### 3.1. Формула

Из непертурбативной стабилизации модулей (KKLT-подход):

    α_G = b₀/(12π),    b₀ = 3N − N_f

где N — ранг скрытой группы SU(N), N_f — число ароматов материи.

### 3.2. Выбор группы

| Группа | N_f | b₀ | α_G | Отклонение от цели 0.21128 |
|---|---|---|---|---|
| SU(2) | 0 | 6 | 0.1592 | −24.7% |
| SU(3) | 0 | 9 | 0.2387 | +13.0% |
| **SU(3)** | **1** | **8** | **0.21221** | **+0.44%** |
| SU(3) | 2 | 7 | 0.1857 | −12.1% |
| SU(4) | 4 | 8 | 0.21221 | +0.44% |

**Оптимум:** α_G = 2/(3π) ≈ 0.212207.

### 3.3. Честные оговорки

- **SU(3) с N_f = 1 — не единственный выбор.** SU(4) с N_f = 4 даёт 
  то же значение α_G. Произвольность выбора не устранена.
- Отклонение +0.44% от эмпирического α_G = 0.21128 объясняется 
  пороговыми поправками от лёгких KK-мод, но **численно не проверено**.

**Статус:** условно выведен.

---

## 4. Масштабы

### 4.1. Масштаб компактификации

    m_KK = M_Pl/(√I · exp(π²)) ≈ 1.044 × 10¹⁵ ГэВ

**Примечание:** в v9.7 было m_KK = 10¹⁵ ГэВ; в v7.5 — 1.044 × 10¹⁵ ГэВ. 
Расхождение +4.4% **меняет** R_T².

### 4.2. 6D-гравитационный масштаб

    M₆ = (3 · M_Pl² · m_KK²)^{1/4} ≈ 1.4853 × 10¹⁷ ГэВ

**Примечание:** в v9.7 было M₆ = 1.4537 × 10¹⁷ ГэВ; расхождение +2.2%.

### 4.3. Скалярный масштаб

    M* = M₆ · ε

---

## 5. Фактор подавления ε (условный)

### 5.1. Формула

    ε = x² · [1 + c₃′·x + c₄′·x² + c₅′·x³ + ...]

где x = α_G/(4π) ≈ 0.016887.

### 5.2. Коэффициенты

Из скрипта MEML7.5.py:

    c₃′ = 0.192
    c₄′ = 0.0203
    c₅′ = 0.00271

**Проблема:** эти коэффициенты **не выведены** из диаграммной свёртки. 
Они **подобраны** так, чтобы получить ε = 2.861 × 10⁻⁴.

### 5.3. Численный результат

    ε = 2.860924 × 10⁻⁴
    Цель: 2.861 × 10⁻⁴
    Отклонение: −0.0027%

**Статус:** условно выведен (коэффициенты подобраны).

---

## 6. Модулярный интеграл I (постулат)

### 6.1. Определение

    I = ∫_{T²/Z₃} |Ψ_g(z,z̄)|² d²z

где Ψ_g — волновая функция нулевой моды гравитона.

### 6.2. Модель гауссова варп-фактора

    A(z,z̄) = −k · Σⱼ exp(−|z−zⱼ|²/(2σ₀²))

Параметры:
- **k = 0.1068** — глубина ямы;
- **σ₀²/V_orb = 0.06** — ширина ямы.

### 6.3. Monte Carlo расчёт

    J = ⟨exp(2A)⟩ = 0.91255
    I = V_orb/J = 0.36528

**Проверка с аналитикой:** J_аналит = 0.91214, I_аналит = 0.36544. 
Согласие 0.045%.

### 6.4. Честный статус

**k = 0.1068 — калибровочный параметр.** Он **подобран** под I = 0.3653.

**Попытка вывести k из дефицита угла δ = 4π/3:**
- Простая формула: k ≈ 0.709 → даёт J ≠ 0.9126
- При σ₀ = 1/m_KK: k ≈ 0.018 или 1.016 → J = 0.9126 (подгонка)

**Вывод:** k **не выводится** из геометрии дефекта простыми формулами.

**Статус:** постулат.

---

## 7. Космологические следствия

### 7.1. Константа распада Печчеи–Квинн

    f_a = M_Pl · ε² ≈ 9.9856 × 10¹¹ ГэВ

### 7.2. Масса аксиона

    m_a = Λ_QCD²/f_a ≈ 5.633 × 10⁻⁶ эВ

где Λ_QCD = 0.075 ГэВ.

### 7.3. Частота сигнала

    ν_a = m_a c²/h ≈ 1.3621 ГГц

### 7.4. Реликтовая плотность

    Ω_a h² = 0.120 · (f_a/10¹²)^{7/6} · θ_i² · f_anh(θ_i)

При θ_i = 0.9483:

    Ω_a h² = 0.119832

**Отклонение от Planck 2018 (0.120 ± 0.001): ~0.14%.**

---

## 8. Честный статус параметров

| Параметр | Значение | Статус | Комментарий |
|---|---|---|---|
| **α_G** | 0.21221 | Условно выведен | Выбор SU(3), N_f=1 произволен |
| **ε** | 2.861 × 10⁻⁴ | Условно выведен | Коэффициенты c_i′ подобраны |
| **I** | 0.3653 | **Постулат** | k = 0.1068 калиброван |
| **θ_i** | 0.9483 | Свободен | Космологическое нач. условие |
| **m_KK** | 1.044 × 10¹⁵ ГэВ | Выведен из уравнения радиона | Из α_G и I |
| **M₆** | 1.4853 × 10¹⁷ ГэВ | Выведен | Из m_KK и M_Pl |

---

## 9. Открытые проблемы

1. **6D-аномалии SU(5) на T²/Z₃.** Не проверены.
2. **Вывод α_G.** SU(3) с N_f=1 — произвольный выбор.
3. **Вывод ε.** Коэффициенты c_i′ подобраны.
4. **Вывод I.** k = 0.1068 калиброван.
5. **Вывод θ_i.** Требуется инфляционная динамика.
6. **Уравнения Эйнштейна.** Метрика не решена.
7. **Стабильность дефектов тора.** Не проверена.
8. **Спектр частиц СМ.** Не выведен.

---

## 10. Заключение

MEML 7.5 **не является полной теорией**. Это **игрушечная модель**, 
в которой:
- α_G получает **условную интерпретацию** через SU(3), N_f=1;
- ε воспроизводится **радиационным рядом** с подобранными c_i′;
- I **калибруется** через параметр k;
- θ_i **остаётся свободным** начальным условием.

**Общий статус:** 2 параметра условно интерпретированы, 1 постулирован, 
1 свободен. **Устранение свободных параметров не достигнуто.**

---

## 11. Рекомендации для дальнейшей работы

1. **Вывести c_i′ из диаграмм KK-петель.**
2. **Вывести k из дефицита угла δ = 4π/3.**
3. **Обосновать выбор SU(3), N_f=1** через аномалии или число поколений.
4. **Проверить 6D-аномалии** явным расчётом I₈ на T²/Z₃.
5. **Вывести θ_i из инфляционной динамики.**
6. **Решить 6D-уравнения Эйнштейна** для точной метрики.

---

**Ключевые слова:** дополнительные измерения, 6D КТП, орбифолд T²/Z₃, 
аксион, тёмная материя, суперадиантность, чёрные дыры, ADMX.

**Ссылки:**
- GitHub: github.com/kolbasa1972/meml-V9.6
- Zenodo: 10.5281/zenodo.23289871
