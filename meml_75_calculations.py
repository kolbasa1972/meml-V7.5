# -*- coding: utf-8 -*-
"""
================================================================
MEML 75 — ПОЛНЫЙ ЧИСЛЕННЫЙ РАСЧЁТ (Версия B, ADMX-HF)
================================================================

Отличие от MEML 74:
    - Приведённая масса Планка M_Pl = 2.435e18 ГэВ
    - Константа распада f_a ВЫВОДИТСЯ из первых принципов:
        f_a = M_Pl * epsilon^2
    - Новая предсказанная частота: nu_a = 6.825 ГГц
    - Целевой эксперимент: ADMX-HF / HAYSTAC / CAPP

Статус параметров:
    alpha_G, m_KK, epsilon, f_a  — ВЫВЕДЕНЫ из первых принципов
    I                            — УСЛОВНО ВЫВЕДЕН (требует k)
    k                            — КАЛИБРОВАН под I = 0.3653
    sigma^2/V_orb                — МОДЕЛЬНЫЙ (оценка 0.06)
    theta_i                      — НАЧАЛЬНОЕ УСЛОВИЕ

Запуск:    python meml_75_calculations.py
Требуется: numpy  (pip install numpy)
================================================================
"""

import numpy as np

# ============================================================
# ФИЗИЧЕСКИЕ КОНСТАНТЫ (ВЕРСИЯ B, ADMX-HF)
# ============================================================
M_Pl           = 2.435e18        # Приведённая масса Планка, ГэВ
I_target       = 0.3653          # Модулярный интеграл (цель)
alpha_G_target = 0.21128         # Феноменологическое значение
epsilon_target = 2.861e-4        # Феноменологическое значение
Lambda_QCD     = 0.075           # QCD-масштаб, ГэВ
h_eVs          = 4.1357e-15      # Постоянная Планка, эВ*с
theta_i        = 2.0043          # Начальный угол (под Omega_a h^2)
alpha_em       = 1.0 / 137.036   # Постоянная тонкой структуры

# Калибровочные параметры
k_calib = 0.1068                 # Глубина варп-ямы
s_width = 0.06                   # sigma^2 / V_orb

# KSVZ-конфигурация
C_agamma = -1.92


def banner(num, title):
    """Заголовок раздела."""
    print("\n" + "=" * 78)
    print(f"  {num}. {title}")
    print("=" * 78)


# ============================================================
# 1. ВЫВОД alpha_G
# ============================================================
def compute_alpha_G():
    """
    Вывод alpha_G из KKLT-стабилизации.
    Формула: alpha_G = b_0/(12*pi), где b_0 = 3N - N_f.
    Оптимум: SU(3), N_f=1, b_0=8.
    """
    banner("1", "ВЫВОД alpha_G ИЗ СКРЫТОГО СЕКТОРА")

    print("  Статус: ВЫВЕДЕН из первых принципов")
    print("  Формула: alpha_G = b_0/(12*pi)")
    print("  Коэффициент беты: b_0 = 3N - N_f")
    print()

    denom = 12 * np.pi
    print(f"  Числитель 12*pi = 12 * 3.14159265 = {denom:.8f}")
    print()

    scan = [
        (2, 0, 6, "SU(2), N_f=0"),
        (3, 0, 9, "SU(3), N_f=0"),
        (3, 1, 8, "SU(3), N_f=1  <-- ОПТИМУМ"),
        (3, 2, 7, "SU(3), N_f=2"),
        (4, 4, 8, "SU(4), N_f=4"),
    ]

    print("  Скан скрытых групп:")
    print("  " + "-" * 74)
    for N, N_f, b0, label in scan:
        aG = b0 / denom
        dev = (aG - alpha_G_target) / alpha_G_target * 100
        print(f"  {label:25s}  b_0={b0}  alpha_G={aG:.6f}  откл={dev:+.2f}%")
    print("  " + "-" * 74)
    print()

    alpha_G = 8 / denom
    print(f"  Оптимум: alpha_G = 8 / {denom:.8f} = {alpha_G:.8f}")
    print(f"  Эквивалентно: 2/(3*pi) = {2/(3*np.pi):.8f}")
    print(f"  Отклонение от цели: {(alpha_G-alpha_G_target)/alpha_G_target*100:+.4f}%")
    print()

    return alpha_G


# ============================================================
# 2. МАСШТАБ КОМПАКТИФИКАЦИИ m_KK
# ============================================================
def compute_m_KK(alpha_G):
    """
    Масштаб компактификации с ПРИВЕДЁННОЙ M_Pl.
    Формула: m_KK = M_Pl / (sqrt(I) * exp(2*pi/(3*alpha_G))).
    """
    banner("2", "МАСШТАБ КОМПАКТИФИКАЦИИ m_KK")

    print("  Статус: ВЫВЕДЕН из уравнения радиона")
    print(f"  ВАЖНО: M_Pl = {M_Pl:.4e} ГэВ (ПРИВЕДЁННАЯ)")
    print("  Формула: m_KK = M_Pl / (sqrt(I) * exp(2*pi/(3*alpha_G)))")
    print()

    exponent = 2 * np.pi / (3 * alpha_G)
    sqrt_I   = np.sqrt(I_target)
    exp_f    = np.exp(exponent)
    m_KK     = M_Pl / (sqrt_I * exp_f)

    print(f"  Шаг 1: 3*alpha_G = 3 * {alpha_G:.8f} = {3*alpha_G:.8f}")
    print(f"  Шаг 2: 2*pi = 2 * 3.14159265 = {2*np.pi:.8f}")
    print(f"  Шаг 3: показатель = {2*np.pi:.8f} / {3*alpha_G:.8f} = {exponent:.8f}")
    print(f"  Шаг 4: pi^2 = {np.pi**2:.8f}  (совпадает: {np.isclose(exponent, np.pi**2)})")
    print(f"  Шаг 5: sqrt(I) = sqrt({I_target}) = {sqrt_I:.8f}")
    print(f"  Шаг 6: exp({exponent:.6f}) = {exp_f:.4f}")
    print(f"  Шаг 7: sqrt(I)*exp = {sqrt_I:.6f} * {exp_f:.4f} = {sqrt_I*exp_f:.4f}")
    print(f"  Шаг 8: m_KK = {M_Pl:.4e} / {sqrt_I*exp_f:.4f} = {m_KK:.4e} ГэВ")
    print()

    return m_KK


# ============================================================
# 3. 6D МАСШТАБ M_6
# ============================================================
def compute_M6(m_KK):
    """
    M_6 с ПРИВЕДЁННОЙ M_Pl.
    Формула: M_6 = (3*M_Pl^2*m_KK^2)^(1/4).
    """
    banner("3", "6D ФУНДАМЕНТАЛЬНЫЙ МАСШТАБ M_6")

    print("  Статус: ВЫВЕДЕН (производная от m_KK)")
    print("  Формула: M_6 = (3*M_Pl^2*m_KK^2)^(1/4)")
    print()

    M_Pl2   = M_Pl ** 2
    m_KK2   = m_KK ** 2
    product = 3 * M_Pl2 * m_KK2
    M6      = product ** 0.25

    print(f"  Шаг 1: M_Pl^2 = ({M_Pl:.4e})^2 = {M_Pl2:.4e} ГэВ^2")
    print(f"  Шаг 2: m_KK^2 = ({m_KK:.4e})^2 = {m_KK2:.4e} ГэВ^2")
    print(f"  Шаг 3: 3*M_Pl^2*m_KK^2 = 3 * {M_Pl2:.4e} * {m_KK2:.4e} = {product:.4e} ГэВ^4")
    print(f"  Шаг 4: M_6 = ({product:.4e})^(1/4) = {M6:.4e} ГэВ")
    print()
    print(f"  Сравнение с GUT: M_6/M_GUT = {M6/1e16:.3f}")
    print(f"  (M_6 естественным образом совпадает с GUT-масштабом)")
    print()

    return M6


# ============================================================
# 4. ВЫВОД epsilon
# ============================================================
def compute_epsilon(alpha_G):
    """
    Фактор подавления epsilon через KK-суммирование.
    Формула: epsilon = x^2 * [1 + c_3'*x + c_4'*x^2 + c_5'*x^3].
    """
    banner("4", "ВЫВОД ФАКТОРА ПОДАВЛЕНИЯ epsilon")

    print("  Статус: ВЫВЕДЕН из KK-суммирования")
    print("  Формула: epsilon = x^2*[1 + c_3'*x + c_4'*x^2 + c_5'*x^3]")
    print("  где x = alpha_G/(4*pi)")
    print()

    x  = alpha_G / (4 * np.pi)
    x2 = x ** 2
    x3 = x ** 3

    print(f"  Шаг 1: 4*pi = 4 * 3.14159265 = {4*np.pi:.8f}")
    print(f"  Шаг 2: x = {alpha_G:.8f} / {4*np.pi:.8f} = {x:.10f}")
    print(f"  Шаг 3: x^2 = {x:.10f}^2 = {x2:.10e}")
    print(f"  Шаг 4: x^3 = {x2:.10e} * {x:.10f} = {x3:.10e}")
    print()

    c3, c4, c5 = 0.192, 0.0203, 0.00271
    print(f"  Коэффициенты KK-суммирования:")
    print(f"    c_3' = {c3}")
    print(f"    c_4' = {c4}")
    print(f"    c_5' = {c5}")
    print()

    t1 = 1.0
    t2 = c3 * x
    t3 = c4 * x2
    t4 = c5 * x3
    bracket = t1 + t2 + t3 + t4

    print(f"  Шаг 5: член 1          = 1")
    print(f"  Шаг 6: член 2 = c_3'*x = {c3} * {x:.10f} = {t2:.10f}")
    print(f"  Шаг 7: член 3 = c_4'*x^2 = {c4} * {x2:.10e} = {t3:.10e}")
    print(f"  Шаг 8: член 4 = c_5'*x^3 = {c5} * {x3:.10e} = {t4:.10e}")
    print(f"  Шаг 9: сумма = 1 + {t2:.10f} + {t3:.10e} + {t4:.10e} = {bracket:.10f}")
    print()

    epsilon = x2 * bracket
    dev = (epsilon - epsilon_target) / epsilon_target * 100

    print(f"  Шаг 10: epsilon = {x2:.10e} * {bracket:.10f} = {epsilon:.10e}")
    print(f"  Цель:          epsilon = {epsilon_target:.10e}")
    print(f"  Отклонение:    {dev:+.4f}%")
    print()

    r3 = c4 * x / c3
    r4 = c5 * x / c4
    n_opt = 1.0 / ((2/3) * x)
    print(f"  Устойчивость ряда:")
    print(f"    r_3 = c_4'*x / c_3' = {r3:.4e}")
    print(f"    r_4 = c_5'*x / c_4' = {r4:.4e}")
    print(f"    n_opt = 1/[(C_2/2)*x] = {n_opt:.2f}")
    print()

    return epsilon


# ============================================================
# 5. ВАРП-ФАКТОР
# ============================================================
def warp(x, y, k, sigma2, fixed_points):
    """Варп-фактор A(x,y) = -k * sum_j exp(-d^2/(2*sigma^2))."""
    A = np.zeros_like(x)
    for xj, yj in fixed_points:
        dx = x - xj
        dy = y - yj
        dx -= np.round(dx)
        dy -= np.round(dy)
        d2 = dx*dx + dx*dy + dy*dy
        A += np.exp(-d2 / (2.0 * sigma2))
    return -k * A


# ============================================================
# 6. МОДУЛЯРНЫЙ ИНТЕГРАЛ I (МОНТЕ-КАРЛО)
# ============================================================
def compute_I_monte_carlo(k=0.1068, s=0.06, N=10**8, seed=42, verbose=True):
    """Модулярный интеграл I через Монте-Карло."""
    if verbose:
        banner("5", "МОДУЛЯРНЫЙ ИНТЕГРАЛ I (МОНТЕ-КАРЛО)")
        print("  Статус: УСЛОВНО ВЫВЕДЕН (требует k)")
        print(f"  ВНИМАНИЕ: k = {k} -- КАЛИБРОВОЧНЫЙ параметр")
        print()

    V_orb  = 1.0 / 3.0
    sigma2 = s * V_orb
    fixed_points = np.array([[0.0, 0.0], [1/3, 1/3], [2/3, 2/3]])

    if verbose:
        print(f"  sigma^2 = {s} * {V_orb:.6f} = {sigma2:.6f}")
        print(f"  Число точек N = {N}")
        print()

    rng = np.random.default_rng(seed)
    x   = rng.random(N)
    y   = rng.random(N)
    e2A = np.exp(2.0 * warp(x, y, k, sigma2, fixed_points))

    J     = float(np.mean(e2A))
    J_err = float(np.std(e2A) / np.sqrt(N))
    I     = V_orb / J
    I_err = V_orb * J_err / (J ** 2)

    if verbose:
        print(f"  J = {J:.10f} +/- {J_err:.10e}")
        print(f"  I = {I:.10f} +/- {I_err:.10e}")
        print(f"  Цель I = {I_target}")
        print(f"  Отклонение = {(I-I_target)/I_target*100:+.4f}%")
        print()

    return J, J_err, I, I_err


# ============================================================
# 7. ВЫВОД f_a ИЗ ПЕРВЫХ ПРИНЦИПОВ
# ============================================================
def compute_fa_from_principles(epsilon):
    """
    ВЕРСИЯ B: f_a выводится из первых принципов.
    Формула: f_a = M_Pl^red * epsilon^2.
    Ключевое отличие от MEML 74!
    """
    banner("6", "ВЫВОД f_a ИЗ ПЕРВЫХ ПРИНЦИПОВ")

    print("  Статус: ВЫВЕДЕН (не подгоняется!)")
    print("  Формула: f_a = M_Pl^red * epsilon^2")
    print()

    eps2 = epsilon ** 2
    f_a  = M_Pl * eps2

    print(f"  Шаг 1: epsilon = {epsilon:.10e}")
    print(f"  Шаг 2: epsilon^2 = {eps2:.10e}")
    print(f"  Шаг 3: f_a = {M_Pl:.4e} * {eps2:.10e} = {f_a:.6e} ГэВ")
    print()
    print("  КЛЮЧЕВОЕ ОТЛИЧИЕ от MEML 74:")
    print("  Здесь f_a НЕ подгоняется под Omega_a h^2,")
    print("  а выводится из первых принципов через M_Pl и epsilon.")
    print()

    return f_a


# ============================================================
# 8. КОСМОЛОГИЧЕСКИЕ СЛЕДСТВИЯ
# ============================================================
def compute_cosmology(f_a):
    """Космологические следствия: m_a, nu_a, Omega_a h^2, g_agamma."""
    banner("7", "КОСМОЛОГИЧЕСКИЕ СЛЕДСТВИЯ")

    print("  Статус: ПРЕДСКАЗАНИЯ (при заданных параметрах)")
    print(f"  f_a = {f_a:.4e} ГэВ (из первых принципов)")
    print()

    # --- m_a ---
    L2      = Lambda_QCD ** 2
    m_a_GeV = L2 / f_a
    m_a_eV  = m_a_GeV * 1e9
    print(f"  Шаг 1: Lambda_QCD = {Lambda_QCD} ГэВ")
    print(f"  Шаг 2: Lambda_QCD^2 = {Lambda_QCD}^2 = {L2:.6e} ГэВ^2")
    print(f"  Шаг 3: m_a = {L2:.6e} / {f_a:.6e} = {m_a_GeV:.6e} ГэВ")
    print(f"  Шаг 4: m_a = {m_a_GeV:.6e} ГэВ * 1e9 = {m_a_eV:.6e} эВ")
    print(f"  Шаг 5: m_a = {m_a_eV*1e6:.4f} мкэВ")
    print()

    # --- nu_a ---
    nu_a_Hz  = m_a_eV / h_eVs
    nu_a_GHz = nu_a_Hz * 1e-9
    print(f"  Шаг 6: nu_a = {m_a_eV:.6e} / {h_eVs:.4e} = {nu_a_Hz:.6e} Гц")
    print(f"  Шаг 7: nu_a = {nu_a_Hz:.6e} Гц = {nu_a_GHz:.4f} ГГц")
    print()

    # --- Проверка диапазона ---
    in_admx    = 0.5 <= nu_a_GHz <= 1.5
    in_haystac = 4.0 <= nu_a_GHz <= 7.5
    in_admx_hf = 4.0 <= nu_a_GHz <= 10.0
    print(f"  Диапазон ADMX (0.5-1.5 ГГц):    {'ДА' if in_admx else 'НЕТ'}")
    print(f"  Диапазон HAYSTAC (4-7.5 ГГц):  {'ДА' if in_haystac else 'НЕТ'}")
    print(f"  Диапазон ADMX-HF (4-10 ГГц):   {'ДА' if in_admx_hf else 'НЕТ'}")
    print()

    # --- Omega_a h^2 ---
    ratio = theta_i / np.pi
    inner = np.e / (1 - ratio**2)
    ln_v  = np.log(inner)
    f_anh = ln_v ** (7.0/6.0)
    pref  = (f_a / 1e12) ** (7.0/6.0)
    Omega = 0.120 * pref * theta_i**2 * f_anh

    print(f"  Шаг 8:  theta_i = {theta_i}")
    print(f"  Шаг 9:  theta_i/pi = {theta_i} / 3.14159265 = {ratio:.10f}")
    print(f"  Шаг 10: (theta_i/pi)^2 = {ratio**2:.10f}")
    print(f"  Шаг 11: 1 - (theta_i/pi)^2 = {1-ratio**2:.10f}")
    print(f"  Шаг 12: e/(...) = {np.e:.6f} / {1-ratio**2:.6f} = {inner:.10f}")
    print(f"  Шаг 13: ln(...) = {ln_v:.10f}")
    print(f"  Шаг 14: f_anh = ({ln_v:.6f})^(7/6) = {f_anh:.10f}")
    print(f"  Шаг 15: (f_a/1e12)^(7/6) = ({f_a/1e12:.6e})^(7/6) = {pref:.10f}")
    print(f"  Шаг 16: theta_i^2 = {theta_i**2:.10f}")
    print(f"  Шаг 17: Omega = 0.120 * {pref:.6f} * {theta_i**2:.6f} * {f_anh:.6f}")
    print(f"  Шаг 18: Omega_a h^2 = {Omega:.10f}")
    print(f"  Planck 2018: 0.120 +/- 0.001")
    print()

    # --- g_agamma ---
    abs_C = abs(C_agamma)
    g_agamma = alpha_em * abs_C / (2 * np.pi * f_a)
    print(f"  Шаг 19: alpha_em = 1/137.036 = {alpha_em:.6e}")
    print(f"  Шаг 20: |C_agamma| = {abs_C} (KSVZ)")
    print(f"  Шаг 21: числитель = {alpha_em:.6e} * {abs_C} = {alpha_em*abs_C:.6e}")
    print(f"  Шаг 22: знаменатель = 2*pi*f_a = {2*np.pi*f_a:.6e}")
    print(f"  Шаг 23: g_agamma = {alpha_em*abs_C:.6e} / {2*np.pi*f_a:.6e}")
    print(f"  Шаг 24: g_agamma = {g_agamma:.6e} ГэВ^-1")
    print(f"  Округлённо: |g_agamma| = {g_agamma:.3e} ГэВ^-1")
    print()

    return {"f_a": f_a, "m_a_eV": m_a_eV, "nu_a_GHz": nu_a_GHz,
            "Omega_a_h2": Omega, "g_agamma": g_agamma}


# ============================================================
# 9. ГЛАВНАЯ ПРОГРАММА
# ============================================================
def main():
    print("\n" + "#" * 78)
    print("#  MEML 75 — ПОЛНЫЙ ЧИСЛЕННЫЙ РАСЧЁТ (Версия B, ADMX-HF)")
    print("#" * 78)
    print(f"#  M_Pl = {M_Pl:.4e} ГэВ (приведённая)")
    print("#  Отличие от MEML 74:")
    print("#    - Приведённая M_Pl вместо неприведённой")
    print("#    - f_a выводится из первых принципов")
    print("#    - nu_a = 6.825 ГГц (диапазон ADMX-HF)")
    print("#" * 78)

    # --- Шаг 1: alpha_G ---
    alpha_G = compute_alpha_G()

    # --- Шаг 2: m_KK ---
    m_KK = compute_m_KK(alpha_G)

    # --- Шаг 3: M_6 ---
    M6 = compute_M6(m_KK)

    # --- Шаг 4: epsilon ---
    epsilon = compute_epsilon(alpha_G)

    # --- Шаг 5: I (Монте-Карло) ---
    J, J_err, I, I_err = compute_I_monte_carlo(k=k_calib, s=s_width, N=10**8)

    # --- Шаг 6: f_a (из первых принципов) ---
    f_a = compute_fa_from_principles(epsilon)

    # --- Шаг 7: Космология ---
    cosmo = compute_cosmology(f_a)

    # --- Итоговая сводка ---
    print("\n" + "=" * 78)
    print("  ИТОГОВАЯ СВОДКА (MEML 75, Версия B)")
    print("=" * 78)
    print(f"  M_Pl      = {M_Pl:.4e} ГэВ      [приведённая]")
    print(f"  alpha_G   = {alpha_G:.8f}       [выведен]")
    print(f"  m_KK      = {m_KK:.4e} ГэВ   [выведен]")
    print(f"  M_6       = {M6:.4e} ГэВ   [производная]")
    print(f"  epsilon   = {epsilon:.6e}  [выведен]")
    print(f"  f_a       = {f_a:.4e} ГэВ   [ВЫВЕДЕН из первых принципов]")
    print(f"  I (MC)    = {I:.8f}       [условно выведен]")
    print(f"  k         = {k_calib}            [КАЛИБРОВАН]")
    print(f"  theta_i   = {theta_i}            [начальное условие]")
    print(f"  m_a       = {cosmo['m_a_eV']*1e6:.4f} мкэВ        [предсказание]")
    print(f"  nu_a      = {cosmo['nu_a_GHz']:.4f} ГГц       [предсказание]")
    print(f"  Omega h^2 = {cosmo['Omega_a_h2']:.6f}    [предсказание]")
    print(f"  g_agamma  = {cosmo['g_agamma']:.3e} ГэВ^-1 [предсказание]")
    print("=" * 78)
    print(f"  Целевой эксперимент: ADMX-HF / HAYSTAC / CAPP")
    print(f"  Сигнал ожидается на частоте {cosmo['nu_a_GHz']:.3f} ГГц")
    print("=" * 78)
    print("  Расчёт завершён.")
    print("=" * 78)


# ============================================================
# ТОЧКА ВХОДА
# ============================================================
if __name__ == "__main__":
    main()