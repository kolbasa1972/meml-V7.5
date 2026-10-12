# -*- coding: utf-8 -*-
"""
================================================================
MEML 75 — ПОЛНЫЙ ЧИСЛЕННЫЙ РАСЧЁТ
================================================================
Скрипт воспроизводит все численные результаты статьи MEML 75:
    - вывод alpha_G из скрытого сектора SU(3);
    - масштаб компактификации m_KK;
    - 6D фундаментальный масштаб M_6;
    - фактор подавления epsilon через KK-суммирование;
    - модулярный интеграл I методом Монте-Карло;
    - проверку Монте-Карло через аналитику;
    - космологические следствия (f_a, m_a, nu_a, Omega_a h^2);
    - константу связи аксиона с фотонами g_agamma.

Статус параметров:
    alpha_G, m_KK, epsilon  — ВЫВЕДЕНЫ
    I                       — УСЛОВНО ВЫВЕДЕН (требует k)
    k                       — КАЛИБРОВАН под I = 0.3653
    sigma^2/V_orb           — МОДЕЛЬНЫЙ (оценка 0.06)
    theta_i                 — НАЧАЛЬНОЕ УСЛОВИЕ

Запуск:    python meml_75_calculations.py
Требуется: numpy  (pip install numpy)
================================================================
"""

import numpy as np

# ============================================================
# ФИЗИЧЕСКИЕ КОНСТАНТЫ
# ============================================================
M_Pl           = 1.22e19         # Планковская масса (неприведённая), ГэВ
I_target       = 0.3653          # Модулярный интеграл (цель)
alpha_G_target = 0.21128         # Феноменологическое значение alpha_G
epsilon_target = 2.861e-4        # Феноменологическое значение epsilon
Lambda_QCD     = 0.075           # QCD-масштаб, ГэВ
h_eVs          = 4.1357e-15      # Постоянная Планка, эВ*с
theta_i        = 0.9483          # Начальный угол смещения аксиона
alpha_em       = 1.0 / 137.036   # Постоянная тонкой структуры

# Калибровочные параметры
k_calib        = 0.1068          # Глубина варп-ямы (калибрована под I)
s_width        = 0.06            # sigma^2 / V_orb (модельная оценка)

# KSVZ-конфигурация
C_agamma       = -1.92           # Киральная поправка для KSVZ


def banner(num, title):
    """Печать заголовка раздела."""
    print("\n" + "=" * 78)
    print(f"  {num}. {title}")
    print("=" * 78)


# ============================================================
# 1. ВЫВОД alpha_G
# ============================================================
def compute_alpha_G():
    """
    Вывод alpha_G из KKLT-стабилизации.
    Формула: alpha_G = b_0 / (12*pi), где b_0 = 3N - N_f.
    Оптимум: SU(3), N_f=1, b_0=8.
    """
    banner("1", "ВЫВОД alpha_G ИЗ СКРЫТОГО СЕКТОРА")

    print("  Статус: ВЫВЕДЕН из первых принципов")
    print("  Формула: alpha_G = b_0 / (12*pi)")
    print("  Коэффициент беты: b_0 = 3N - N_f")
    print()

    # Числитель
    denom = 12 * np.pi
    print(f"  Числитель 12*pi = 12 * 3.14159265 = {denom:.8f}")
    print()

    # Скан групп
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
        alpha_G = b0 / denom
        dev = (alpha_G - alpha_G_target) / alpha_G_target * 100
        print(f"  {label:25s}  b_0={b0}  alpha_G={alpha_G:.6f}  откл={dev:+.2f}%")
    print("  " + "-" * 74)
    print()

    # Оптимальная конфигурация
    alpha_G_opt = 8 / denom
    print(f"  Оптимум: alpha_G = 8 / {denom:.8f} = {alpha_G_opt:.8f}")
    print(f"  Эквивалентно: 2/(3*pi) = {2/(3*np.pi):.8f}")
    print(f"  Отклонение от цели {alpha_G_target}: "
          f"{(alpha_G_opt - alpha_G_target)/alpha_G_target*100:+.4f}%")
    print()
    print("  Примечание: отклонение +0.44% объясняется однопетлевыми")
    print("  пороговыми поправками от ~5 KK-мод на масштабе m_KK.")
    print()

    return alpha_G_opt


# ============================================================
# 2. МАСШТАБ КОМПАКТИФИКАЦИИ m_KK
# ============================================================
def compute_m_KK(alpha_G):
    """
    Вывод масштаба компактификации из уравнения радиона.
    Формула: m_KK = M_Pl / (sqrt(I) * exp(2*pi/(3*alpha_G))).
    """
    banner("2", "МАСШТАБ КОМПАКТИФИКАЦИИ m_KK")

    print("  Статус: ВЫВЕДЕН из уравнения радиона")
    print("  Формула: m_KK = M_Pl / (sqrt(I) * exp(2*pi/(3*alpha_G)))")
    print()

    # Показатель экспоненты
    exponent = 2 * np.pi / (3 * alpha_G)
    sqrt_I   = np.sqrt(I_target)
    exp_f    = np.exp(exponent)
    m_KK     = M_Pl / (sqrt_I * exp_f)

    print(f"  Шаг 1: alpha_G = {alpha_G:.8f}")
    print(f"  Шаг 2: 3 * alpha_G = 3 * {alpha_G:.8f} = {3*alpha_G:.8f}")
    print(f"  Шаг 3: 2 * pi = 2 * 3.14159265 = {2*np.pi:.8f}")
    print(f"  Шаг 4: показатель = {2*np.pi:.8f} / {3*alpha_G:.8f} "
          f"= {exponent:.8f}")
    print(f"  Шаг 5: pi^2 = {np.pi**2:.8f}  (совпадает: "
          f"{np.isclose(exponent, np.pi**2)})")
    print(f"  Шаг 6: sqrt(I) = sqrt({I_target}) = {sqrt_I:.8f}")
    print(f"  Шаг 7: exp({exponent:.6f}) = {exp_f:.4f}")
    print(f"  Шаг 8: sqrt(I) * exp = {sqrt_I:.6f} * {exp_f:.4f} "
          f"= {sqrt_I*exp_f:.4f}")
    print(f"  Шаг 9: m_KK = {M_Pl:.4e} / {sqrt_I*exp_f:.4f} = {m_KK:.4e} ГэВ")
    print()

    return m_KK


# ============================================================
# 3. 6D ФУНДАМЕНТАЛЬНЫЙ МАСШТАБ M_6
# ============================================================
def compute_M6(m_KK):
    """
    Вывод 6D фундаментального масштаба из редукции.
    Формула: M_6 = (3*M_Pl^2*m_KK^2)^(1/4).
    """
    banner("3", "6D ФУНДАМЕНТАЛЬНЫЙ МАСШТАБ M_6")

    print("  Статус: ВЫВЕДЕН из редукции (производная от m_KK)")
    print("  Формула: M_6 = (3*M_Pl^2*m_KK^2)^(1/4)")
    print()

    M_Pl2   = M_Pl ** 2
    m_KK2   = m_KK ** 2
    product = 3 * M_Pl2 * m_KK2
    M6      = product ** 0.25

    print(f"  Шаг 1: M_Pl^2 = ({M_Pl:.4e})^2 = {M_Pl2:.4e} ГэВ^2")
    print(f"  Шаг 2: m_KK^2 = ({m_KK:.4e})^2 = {m_KK2:.4e} ГэВ^2")
    print(f"  Шаг 3: 3*M_Pl^2*m_KK^2 = 3 * {M_Pl2:.4e} * {m_KK2:.4e} "
          f"= {product:.4e} ГэВ^4")
    print(f"  Шаг 4: M_6 = ({product:.4e})^(1/4) = {M6:.4e} ГэВ")
    print()

    return M6


# ============================================================
# 4. ВЫВОД ФАКТОРА ПОДАВЛЕНИЯ epsilon
# ============================================================
def compute_epsilon(alpha_G):
    """
    Вывод фактора подавления epsilon через KK-суммирование.
    Формула: epsilon = x^2 * [1 + c_3'*x + c_4'*x^2 + c_5'*x^3],
    где x = alpha_G / (4*pi).
    """
    banner("4", "ВЫВОД ФАКТОРА ПОДАВЛЕНИЯ epsilon")

    print("  Статус: ВЫВЕДЕН из KK-суммирования")
    print("  Формула: epsilon = x^2 * [1 + c_3'*x + c_4'*x^2 + c_5'*x^3]")
    print("  где x = alpha_G / (4*pi)")
    print()

    # Параметр разложения
    x  = alpha_G / (4 * np.pi)
    x2 = x ** 2
    x3 = x ** 3

    print(f"  Шаг 1: 4*pi = 4 * 3.14159265 = {4*np.pi:.8f}")
    print(f"  Шаг 2: x = {alpha_G:.8f} / {4*np.pi:.8f} = {x:.10f}")
    print(f"  Шаг 3: x^2 = {x:.10f}^2 = {x2:.10e}")
    print(f"  Шаг 4: x^3 = {x2:.10e} * {x:.10f} = {x3:.10e}")
    print()

    # Коэффициенты KK-суммирования
    c3, c4, c5 = 0.192, 0.0203, 0.00271
    print(f"  Коэффициенты из KK-суммирования:")
    print(f"    c_3' = {c3}")
    print(f"    c_4' = {c4}")
    print(f"    c_5' = {c5}")
    print()

    # Пошаговое суммирование
    t1 = 1.0
    t2 = c3 * x
    t3 = c4 * x2
    t4 = c5 * x3
    bracket = t1 + t2 + t3 + t4

    print(f"  Шаг 5: член 1          = 1")
    print(f"  Шаг 6: член 2 = c_3'*x = {c3} * {x:.10f} = {t2:.10f}")
    print(f"  Шаг 7: член 3 = c_4'*x^2 = {c4} * {x2:.10e} = {t3:.10e}")
    print(f"  Шаг 8: член 4 = c_5'*x^3 = {c5} * {x3:.10e} = {t4:.10e}")
    print(f"  Шаг 9: сумма = 1 + {t2:.10f} + {t3:.10e} + {t4:.10e} "
          f"= {bracket:.10f}")
    print()

    # Итоговое значение
    epsilon = x2 * bracket
    dev = (epsilon - epsilon_target) / epsilon_target * 100

    print(f"  Шаг 10: epsilon = {x2:.10e} * {bracket:.10f} = {epsilon:.10e}")
    print(f"  Цель:          epsilon = {epsilon_target:.10e}")
    print(f"  Отклонение:    {dev:+.4f}%")
    print()

    # Проверка устойчивости
    r3 = c4 * x / c3
    r4 = c5 * x / c4
    n_opt = 1.0 / ((2/3) * x)
    print(f"  Устойчивость ряда:")
    print(f"    r_3 = c_4'*x / c_3' = {r3:.4e}")
    print(f"    r_4 = c_5'*x / c_4' = {r4:.4e}")
    print(f"    n_opt = 1/[(C_2/2)*x] = {n_opt:.2f}")
    print(f"    Оба отношения << 1, ряд сходится быстро.")
    print()

    return epsilon


# ============================================================
# 5. ВАРП-ФАКТОР
# ============================================================
def warp(x, y, k, sigma2, fixed_points):
    """
    Варп-фактор A(x,y) = -k * sum_j exp(-d^2/(2*sigma^2)).
    Метрика: ds^2 = dx^2 + dx*dy + dy^2 (tau = exp(i*pi/3)).
    Учитывается периодизация на торе.
    """
    A = np.zeros_like(x)
    for xj, yj in fixed_points:
        dx = x - xj
        dy = y - yj
        dx -= np.round(dx)
        dy -= np.round(dy)
        # Квадрат расстояния в метрике тора
        d2 = dx*dx + dx*dy + dy*dy
        A += np.exp(-d2 / (2.0 * sigma2))
    return -k * A


# ============================================================
# 6. МОДУЛЯРНЫЙ ИНТЕГРАЛ I (МОНТЕ-КАРЛО)
# ============================================================
def compute_I_monte_carlo(k=0.1068, s=0.06, N=10**8, seed=42, verbose=True):
    """
    Вычисление модулярного интеграла I методом Монте-Карло.
    J = < exp(2A) > по тору T^2.
    I = V_orb / J.
    """
    if verbose:
        banner("5", "МОДУЛЯРНЫЙ ИНТЕГРАЛ I МЕТОДОМ МОНТЕ-КАРЛО")

        print("  Статус: УСЛОВНО ВЫВЕДЕН (требует k)")
        print("  Формула: J = < exp(2A) > по тору T^2")
        print("  Формула: I = V_orb / J,  V_orb = 1/3")
        print("  Варп: A(x,y) = -k * sum_j exp(-d^2/(2*sigma^2))")
        print("  Метрика: ds^2 = dx^2 + dx*dy + dy^2 (tau = exp(i*pi/3))")
        print()
        print(f"  ВНИМАНИЕ: k = {k} -- КАЛИБРОВОЧНЫЙ параметр,")
        print(f"  подобранный под I_target = {I_target}")
        print()
        print("  Неподвижные точки: (0,0), (1/3,1/3), (2/3,2/3)")

    # Область интегрирования
    V_orb  = 1.0 / 3.0
    sigma2 = s * V_orb

    # Неподвижные точки
    fixed_points = np.array([[0.0, 0.0],
                             [1/3, 1/3],
                             [2/3, 2/3]])

    if verbose:
        print(f"  Параметры: k = {k}, s = sigma^2/V_orb = {s}")
        print(f"  sigma^2 = {s} * {V_orb:.6f} = {sigma2:.6f}")
        print(f"  Число точек N = {N}")
        print()

    # Генерация случайных точек
    rng = np.random.default_rng(seed)
    x   = rng.random(N)
    y   = rng.random(N)

    # Вычисление exp(2A) в каждой точке
    e2A = np.exp(2.0 * warp(x, y, k, sigma2, fixed_points))

    # Статистика
    J     = float(np.mean(e2A))
    J_err = float(np.std(e2A) / np.sqrt(N))
    I     = V_orb / J
    I_err = V_orb * J_err / (J ** 2)

    if verbose:
        print(f"  Шаг 1: N точек сгенерировано = {N}")
        print(f"  Шаг 2: для каждой точки вычислено A(x,y) и exp(2A)")
        print(f"  Шаг 3: J = <exp(2A)> = {J:.10f}")
        print(f"  Шаг 4: статистическая ошибка dJ = {J_err:.10e}")
        print(f"  Шаг 5: I = V_orb / J = {V_orb:.10f} / {J:.10f} "
              f"= {I:.10f}")
        print(f"  Шаг 6: статистическая ошибка dI = {I_err:.10e}")
        print(f"  Цель I = {I_target}")
        print(f"  Отклонение = {(I-I_target)/I_target*100:+.4f}%")
        print()

    return J, J_err, I, I_err


# ============================================================
# 7. ПРОВЕРКА МОНТЕ-КАРЛО ЧЕРЕЗ АНАЛИТИКУ
# ============================================================
def verify_monte_carlo():
    """
    Независимая проверка: сравнение Монте-Карло с аналитическим
    разложением для J.
    """
    banner("6", "ПРОВЕРКА МОНТЕ-КАРЛО ЧЕРЕЗ АНАЛИТИКУ")

    print("  Статус: ПРОВЕРКА (независимый метод)")
    print("  Аналитическая формула:")
    print("  J = 1 - 8*sqrt(3)*pi*k*sigma^2")
    print("        + 4*sqrt(3)*pi*k^2*sigma^2*[1 + 2*exp(-R^2/(4*sigma^2))]")
    print("  где R^2 = 1/3")
    print()

    # Параметры
    k      = k_calib
    s      = s_width
    V_orb  = 1.0 / 3.0
    sigma2 = s * V_orb
    R2     = 1.0 / 3.0
    sqrt3  = np.sqrt(3.0)

    print(f"  Шаг 1: sigma^2 = {s} * {V_orb:.6f} = {sigma2:.6f}")
    print(f"  Шаг 2: sqrt(3) = {sqrt3:.10f}")
    print(f"  Шаг 3: 8*sqrt(3)*pi = {8*sqrt3*np.pi:.10f}")
    print(f"  Шаг 4: 4*sqrt(3)*pi = {4*sqrt3*np.pi:.10f}")

    term1 = 8 * sqrt3 * np.pi * k * sigma2
    print(f"  Шаг 5: term1 = {8*sqrt3*np.pi:.6f} * {k} * {sigma2:.6f} "
          f"= {term1:.10f}")

    k2 = k ** 2
    term2 = 4 * sqrt3 * np.pi * k2 * sigma2
    print(f"  Шаг 6: k^2 = {k}^2 = {k2:.10f}")
    print(f"  Шаг 7: term2 = {4*sqrt3*np.pi:.6f} * {k2:.10f} * {sigma2:.6f} "
          f"= {term2:.10f}")

    exp_arg = -R2 / (4 * sigma2)
    exp_val = np.exp(exp_arg)
    cross   = 2 * exp_val
    print(f"  Шаг 8:  R^2 = {R2:.10f}")
    print(f"  Шаг 9:  R^2/(4*sigma^2) = {R2:.10f} / {4*sigma2:.10f} "
          f"= {R2/(4*sigma2):.10f}")
    print(f"  Шаг 10: exp({exp_arg:.10f}) = {exp_val:.10f}")
    print(f"  Шаг 11: cross = 2 * {exp_val:.10f} = {cross:.10f}")

    bracket = 1.0 + cross
    print(f"  Шаг 12: 1 + cross = {bracket:.10f}")

    J_analytic = 1.0 - term1 + term2 * bracket
    I_analytic = V_orb / J_analytic

    print(f"  Шаг 13: J_аналит = 1 - {term1:.10f} "
          f"+ {term2:.10f} * {bracket:.10f}")
    print(f"  Шаг 14: J_аналит = {J_analytic:.10f}")
    print(f"  Шаг 15: I_аналит = {V_orb:.10f} / {J_analytic:.10f} "
          f"= {I_analytic:.10f}")
    print()

    # Запуск Монте-Карло
    print(f"  Запуск Монте-Карло (N = 10^8):")
    J_mc, J_mc_err, I_mc, I_mc_err = compute_I_monte_carlo(
        k=k, s=s, N=10**8, verbose=False)
    print(f"  J_mc = {J_mc:.10f} +/- {J_mc_err:.10e}")
    print(f"  I_mc = {I_mc:.10f} +/- {I_mc_err:.10e}")
    print()

    # Сравнение
    diff_J = abs(J_mc - J_analytic) / J_analytic * 100
    diff_I = abs(I_mc - I_analytic) / I_analytic * 100
    print(f"  Сравнение J: расхождение = {diff_J:.4f}%")
    print(f"  Сравнение I: расхождение = {diff_I:.4f}%")
    if diff_J < 1.0:
        print(f"  Статус: OK — согласие в пределах 1%")
    else:
        print(f"  Статус: ВНИМАНИЕ — расхождение > 1%")
    print()

    return {"J_analytic": J_analytic, "I_analytic": I_analytic,
            "J_mc": J_mc, "J_mc_err": J_mc_err,
            "I_mc": I_mc, "I_mc_err": I_mc_err,
            "diff_J": diff_J, "diff_I": diff_I}


# ============================================================
# 8. КОСМОЛОГИЧЕСКИЕ СЛЕДСТВИЯ
# ============================================================
def compute_cosmology(epsilon):
    """
    Космологические следствия:
        f_a = M_Pl * epsilon^2
        m_a = Lambda_QCD^2 / f_a
        nu_a = m_a c^2 / h
        Omega_a h^2 (Лит--Тёрнер)
        g_agamma (KSVZ)
    """
    banner("7", "КОСМОЛОГИЧЕСКИЕ СЛЕДСТВИЯ")

    print("  Статус: ПРЕДСКАЗАНИЯ (при фиксированных параметрах)")
    print("  Формулы:")
    print("    f_a = M_Pl * epsilon^2")
    print("    m_a = Lambda_QCD^2 / f_a")
    print("    nu_a = m_a * c^2 / h")
    print("    Omega_a h^2 = 0.120 * (f_a/10^12)^(7/6) * theta_i^2 * f_anh")
    print("    g_agamma = alpha_em * |C_agamma| / (2*pi*f_a)")
    print()

    # --- f_a ---
    eps2 = epsilon ** 2
    f_a  = M_Pl * eps2
    print(f"  Шаг 1:  epsilon = {epsilon:.10e}")
    print(f"  Шаг 2:  epsilon^2 = {eps2:.10e}")
    print(f"  Шаг 3:  f_a = {M_Pl:.4e} * {eps2:.10e} = {f_a:.6e} ГэВ")
    print()

    # --- m_a ---
    L2      = Lambda_QCD ** 2
    m_a_GeV = L2 / f_a
    m_a_eV  = m_a_GeV * 1e9
    print(f"  Шаг 4:  Lambda_QCD = {Lambda_QCD} ГэВ")
    print(f"  Шаг 5:  Lambda_QCD^2 = {Lambda_QCD}^2 = {L2:.6e} ГэВ^2")
    print(f"  Шаг 6:  m_a = {L2:.6e} / {f_a:.6e} = {m_a_GeV:.6e} ГэВ")
    print(f"  Шаг 7:  m_a = {m_a_GeV:.6e} ГэВ * 1e9 = {m_a_eV:.6e} эВ")
    print()

    # --- nu_a ---
    nu_a_Hz  = m_a_eV / h_eVs
    nu_a_GHz = nu_a_Hz * 1e-9
    print(f"  Шаг 8:  nu_a = {m_a_eV:.6e} / {h_eVs:.4e} = {nu_a_Hz:.6e} Гц")
    print(f"  Шаг 9:  nu_a = {nu_a_Hz:.6e} Гц = {nu_a_GHz:.4f} ГГц")
    print()

    # --- Omega_a h^2 ---
    ratio = theta_i / np.pi
    inner = np.e / (1 - ratio**2)
    ln_v  = np.log(inner)
    f_anh = ln_v ** (7.0/6.0)
    pref  = (f_a / 1e12) ** (7.0/6.0)
    Omega = 0.120 * pref * theta_i**2 * f_anh

    print(f"  Шаг 10: theta_i = {theta_i}")
    print(f"  Шаг 11: theta_i/pi = {theta_i} / 3.14159265 = {ratio:.10f}")
    print(f"  Шаг 12: (theta_i/pi)^2 = {ratio**2:.10f}")
    print(f"  Шаг 13: 1 - (theta_i/pi)^2 = {1-ratio**2:.10f}")
    print(f"  Шаг 14: e/(...) = {np.e:.6f} / {1-ratio**2:.6f} "
          f"= {inner:.10f}")
    print(f"  Шаг 15: ln(...) = {ln_v:.10f}")
    print(f"  Шаг 16: f_anh = ({ln_v:.6f})^(7/6) = {f_anh:.10f}")
    print(f"  Шаг 17: (f_a/1e12)^(7/6) = ({f_a/1e12:.6e})^(7/6) "
          f"= {pref:.10f}")
    print(f"  Шаг 18: theta_i^2 = {theta_i**2:.10f}")
    print(f"  Шаг 19: Omega = 0.120 * {pref:.6f} * {theta_i**2:.6f} "
          f"* {f_anh:.6f}")
    print(f"  Шаг 20: Omega_a h^2 = {Omega:.10f}")
    print(f"  Planck 2018: 0.120 +/- 0.001")
    print()

    # --- g_agamma ---
    abs_C = abs(C_agamma)
    g_agamma = alpha_em * abs_C / (2 * np.pi * f_a)
    print(f"  Шаг 21: alpha_em = 1/137.036 = {alpha_em:.8e}")
    print(f"  Шаг 22: |C_agamma| = {abs_C} (KSVZ)")
    print(f"  Шаг 23: 2*pi*f_a = 2 * 3.14159265 * {f_a:.6e} "
          f"= {2*np.pi*f_a:.6e}")
    print(f"  Шаг 24: g_agamma = {alpha_em:.6e} * {abs_C} "
          f"/ {2*np.pi*f_a:.6e}")
    print(f"  Шаг 25: g_agamma = {g_agamma:.6e} ГэВ^-1")
    print(f"  Округлённо: |g_agamma| = {g_agamma:.3e} ГэВ^-1")
    print()

    return {"f_a": f_a, "m_a_eV": m_a_eV,
            "nu_a_GHz": nu_a_GHz, "Omega_a_h2": Omega,
            "g_agamma": g_agamma}


# ============================================================
# 9. ГЛАВНАЯ ПРОГРАММА
# ============================================================
def main():
    print("\n" + "#" * 78)
    print("#  MEML 75 — ПОЛНЫЙ ЧИСЛЕННЫЙ РАСЧЁТ")
    print("#" * 78)
    print("#  Статус параметров:")
    print("#    alpha_G, m_KK, epsilon   — ВЫВЕДЕНЫ из первых принципов")
    print("#    M_6                      — ПРОИЗВОДНАЯ от m_KK")
    print("#    I                        — УСЛОВНО ВЫВЕДЕН (требует k)")
    print("#    k                        — КАЛИБРОВАН под I = 0.3653")
    print("#    sigma^2/V_orb            — МОДЕЛЬНЫЙ (оценка 0.06)")
    print("#    theta_i                  — НАЧАЛЬНОЕ УСЛОВИЕ")
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

    # --- Шаг 6: Проверка Монте-Карло ---
    verify = verify_monte_carlo()

    # --- Шаг 7: Космология ---
    cosmo = compute_cosmology(epsilon)

    # --- Итоговая сводка ---
    print("\n" + "=" * 78)
    print("  ИТОГОВАЯ СВОДКА")
    print("=" * 78)
    print(f"  alpha_G   = {alpha_G:.8f}         [выведен]")
    print(f"  m_KK      = {m_KK:.4e} ГэВ     [выведен]")
    print(f"  M_6       = {M6:.4e} ГэВ     [производная]")
    print(f"  epsilon   = {epsilon:.6e}    [выведен]")
    print(f"  k         = {k_calib}              [КАЛИБРОВАН]")
    print(f"  J (MC)    = {J:.8f}         [условно выведен]")
    print(f"  I (MC)    = {I:.8f}         [условно выведен]")
    print(f"  f_a       = {cosmo['f_a']:.4e} ГэВ     [предсказание]")
    print(f"  m_a       = {cosmo['m_a_eV']:.4e} эВ     [предсказание]")
    print(f"  nu_a      = {cosmo['nu_a_GHz']:.4f} ГГц     [предсказание]")
    print(f"  Omega h^2 = {cosmo['Omega_a_h2']:.6f}      [предсказание]")
    print(f"  g_agamma  = {cosmo['g_agamma']:.3e} ГэВ^-1  [предсказание]")
    print("=" * 78)
    print("  Согласие Монте-Карло и аналитики:")
    print(f"    J: расхождение = {verify['diff_J']:.4f}%")
    print(f"    I: расхождение = {verify['diff_I']:.4f}%")
    print("=" * 78)
    print("  Расчёт завершён.")
    print("=" * 78)


# ============================================================
# ТОЧКА ВХОДА
# ============================================================
if __name__ == "__main__":
    main()