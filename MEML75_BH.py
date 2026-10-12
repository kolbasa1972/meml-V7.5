# -*- coding: utf-8 -*-
"""
================================================================
MEML 75 — АСТРОФИЗИЧЕСКИЙ МОДУЛЬ (Версия B, ADMX-HF)
================================================================
Расчёт зоны суперрадиации ПЧД, температуры Хокинга,
времени развития неустойчивости.

Модель: MEML 75 (Версия B)
m_a = 28.22 мкЭВ
alpha_max = 0.4 (пик l=m=1)

Запуск: python MEML75_BH.py
Требуется: numpy
================================================================
"""

import numpy as np

# ============================================================
# ИСХОДНЫЕ ПАРАМЕТРЫ ВЕРСИИ B
# ============================================================
m_a_eV    = 28.22e-6       # Прецизионная масса аксиона, эВ
alpha_max = 0.4            # Пик нестабильности моды l=m=1

# ============================================================
# ФУНДАМЕНТАЛЬНЫЕ КОНСТАНТЫ (СИ)
# ============================================================
G_SI      = 6.6743e-11     # Гравитационная постоянная, м³/(кг·с²)
c_SI      = 2.99792458e8   # Скорость света, м/с
M_sun_kg  = 1.98847e30     # Масса Солнца, кг
M_earth_kg = 5.9722e24     # Масса Земли, кг
hbar_SI   = 1.0545718e-34  # Приведённая постоянная Планка, Дж·с
eV_to_J   = 1.60217663e-19 # Перевод эВ → Дж
k_B_SI    = 1.380649e-23   # Постоянная Больцмана, Дж/К


def banner(num, title):
    print("\n" + "=" * 78)
    print(f"  {num}. {title}")
    print("=" * 78)


# ============================================================
# 1. РАСЧЁТ ЗОНЫ СУПЕРРАДИАЦИИ (REGGE PLANE)
# ============================================================
def compute_superradiance():
    """
    Зона суперрадиационной неустойчивости для моды l=m=1.
    Формула: M_BH = alpha_max * hbar * c / (G * m_a)
    """
    banner("1", "ЗОНА СУПЕРРАДИАЦИИ (REGGE PLANE)")

    print("  Формула: M_BH = alpha_max * hbar * c / (G * m_a)")
    print(f"  alpha_max = {alpha_max}")
    print(f"  m_a = {m_a_eV*1e6:.4f} мкЭВ")
    print()

    # Перевод массы аксиона в кг
    E_a_J  = m_a_eV * eV_to_J          # Энергия покоя, Дж
    m_a_kg = E_a_J / c_SI**2           # Масса в кг

    print(f"  Шаг 1: E_a = m_a * c² = {E_a_J:.4e} Дж")
    print(f"  Шаг 2: m_a (в кг) = E_a / c² = {m_a_kg:.4e} кг")
    print()

    # Числитель
    numerator = alpha_max * hbar_SI * c_SI
    print(f"  Шаг 3: числитель = alpha * hbar * c = {numerator:.4e}")

    # Знаменатель
    denominator = G_SI * m_a_kg
    print(f"  Шаг 4: знаменатель = G * m_a = {denominator:.4e}")
    print()

    # Масса ЧД
    M_BH_kg = numerator / denominator
    M_BH_solar = M_BH_kg / M_sun_kg
    M_BH_earth = M_BH_kg / M_earth_kg

    print(f"  Шаг 5: M_BH = {numerator:.4e} / {denominator:.4e}")
    print(f"         M_BH = {M_BH_kg:.4e} кг")
    print()
    print(f"  РЕЗУЛЬТАТ:")
    print(f"    M_BH = {M_BH_solar:.4e} M_sun")
    print(f"    M_BH = {M_BH_earth:.4f} M_Earth")
    print(f"    M_BH = {M_BH_earth*333000:.2f} масс Луны")
    print()
    print(f"    Тип объекта: ПЕРВИЧНАЯ ЧЁРНАЯ ДЫРА (ПЧД)")
    print()

    return M_BH_kg, M_BH_solar, M_BH_earth


# ============================================================
# 2. ГРАВИТАЦИОННЫЙ РАДИУС ПЧД
# ============================================================
def compute_schwarzschild_radius(M_BH_kg):
    """Радиус Шварцшильда: R_g = 2 G M / c²."""
    banner("2", "РАДИУС ШВАРЦШИЛЬДА ПЧД")

    R_g = 2 * G_SI * M_BH_kg / c_SI**2

    print(f"  Формула: R_g = 2 G M_BH / c²")
    print(f"  Шаг 1: 2 * G * M_BH = {2*G_SI*M_BH_kg:.4e}")
    print(f"  Шаг 2: c² = {c_SI**2:.4e}")
    print(f"  Шаг 3: R_g = {R_g:.4e} м = {R_g*1e3:.3f} мм")
    print()

    return R_g


# ============================================================
# 3. ТЕМП СУПЕРРАДИАЦИИ
# ============================================================
def compute_superradiance_rate():
    """
    Инкремент Gamma для l=m=1: Gamma = alpha^8 * m_a / (24 * hbar).
    Время развития tau = 1 / Gamma.
    """
    banner("3", "ТЕМП СУПЕРРАДИАЦИОННОГО ВЗРЫВА")

    print("  Формула: Gamma_SR = alpha^8 * m_a / (24 * hbar)")
    print()

    # Энергия аксиона в Дж
    E_a_J = m_a_eV * eV_to_J

    # Числитель и знаменатель
    alpha8 = alpha_max**8
    numerator = alpha8 * E_a_J
    denominator = 24.0 * hbar_SI

    print(f"  Шаг 1: alpha^8 = {alpha_max}^8 = {alpha8:.4e}")
    print(f"  Шаг 2: alpha^8 * m_a = {alpha8:.4e} * {E_a_J:.4e} = {numerator:.4e} Дж")
    print(f"  Шаг 3: 24 * hbar = {denominator:.4e}")
    print()

    Gamma_SR = numerator / denominator
    tau_SR = 1.0 / Gamma_SR

    print(f"  Шаг 4: Gamma_SR = {Gamma_SR:.4e} с⁻¹")
    print(f"  Шаг 5: tau_SR = 1/Gamma_SR = {tau_SR:.4e} с")
    print(f"                    = {tau_SR*1e6:.3f} мкс")
    print()

    return Gamma_SR, tau_SR


# ============================================================
# 4. ТЕМПЕРАТУРА ХОКИНГА
# ============================================================
def compute_hawking_temperature(M_BH_kg):
    """T_H = hbar c³ / (8 pi G M_BH k_B)."""
    banner("4", "ТЕМПЕРАТУРА ХОКИНГА")

    print("  Формула: T_H = hbar * c³ / (8 * pi * G * M_BH * k_B)")
    print()

    # Числитель и знаменатель
    numerator = hbar_SI * c_SI**3
    denominator_K = 8 * np.pi * G_SI * M_BH_kg * k_B_SI
    denominator_eV = 8 * np.pi * G_SI * M_BH_kg * eV_to_J

    print(f"  Шаг 1: hbar * c³ = {numerator:.4e}")
    print(f"  Шаг 2: 8 * pi * G * M_BH = {8*np.pi*G_SI*M_BH_kg:.4e}")
    print()

    T_H_K = numerator / denominator_K
    T_H_eV = numerator / denominator_eV
    T_H_u_eV = T_H_eV * 1e6

    print(f"  Шаг 3: T_H = {T_H_K:.4e} К")
    print(f"  Шаг 4: T_H = {T_H_eV:.6e} эВ = {T_H_u_eV:.3f} мкЭВ")
    print()

    return T_H_K, T_H_eV


# ============================================================
# 5. ВЕРДИКТ ИСПАРЕНИЯ ЧЕРЕЗ АКСИОНЫ
# ============================================================
def verdict_hawking(T_H_eV):
    banner("5", "ВЕРДИКТ АКСИОННОГО КАНАЛА ХОКИНГА")

    print(f"  T_H = {T_H_eV*1e6:.3f} мкЭВ")
    print(f"  m_a = {m_a_eV*1e6:.3f} мкЭВ")
    print()

    print("  " + "-" * 74)

    if T_H_eV > m_a_eV:
        print(f"  СТАТУС: аксионный канал ХОКИНГА ОТКРЫТ")
        print(f"  T_H ({T_H_eV*1e6:.1f} мкЭВ) > m_a ({m_a_eV*1e6:.1f} мкЭВ)")
        print(f"  ПЧД испаряется через эмиссию аксионов тёмной материи.")
    else:
        print(f"  СТАТУС: аксионный канал ХОКИНГА ЗАКРЫТ кинематически")
        print(f"  T_H ({T_H_eV*1e6:.1f} мкЭВ) < m_a ({m_a_eV*1e6:.1f} мкЭВ)")
        print(f"  Чёрная дыра слишком холодна для эмиссии таких тяжёлых частиц.")

    print("  " + "-" * 74)


# ============================================================
# 6. ГЛАВНАЯ ПРОГРАММА
# ============================================================
def main():
    print("\n" + "#" * 78)
    print("#  MEML 75 — АСТРОФИЗИЧЕСКИЙ МОДУЛЬ (ВЕРСИЯ B, ADMX-HF)")
    print("#" * 78)
    print(f"#  Масса аксиона: m_a = {m_a_eV*1e6:.2f} мкЭВ")
    print(f"#  Пик суперрадиации: alpha = {alpha_max}")
    print("#" * 78)

    # --- Шаг 1: Зона суперрадиации ---
    M_BH_kg, M_BH_solar, M_BH_earth = compute_superradiance()

    # --- Шаг 2: Радиус Шварцшильда ---
    R_g = compute_schwarzschild_radius(M_BH_kg)

    # --- Шаг 3: Темп суперрадиации ---
    Gamma_SR, tau_SR = compute_superradiance_rate()

    # --- Шаг 4: Температура Хокинга ---
    T_H_K, T_H_eV = compute_hawking_temperature(M_BH_kg)

    # --- Шаг 5: Вердикт ---
    verdict_hawking(T_H_eV)

    # --- Итоговая сводка ---
    print("\n" + "=" * 78)
    print("  ИТОГОВАЯ СВОДКА (MEML 75, ПЧД)")
    print("=" * 78)
    print(f"  m_a         = {m_a_eV*1e6:.2f} мкЭВ")
    print(f"  M_BH        = {M_BH_kg:.4e} кг")
    print(f"  M_BH        = {M_BH_solar:.4e} M_sun")
    print(f"  M_BH        = {M_BH_earth:.4f} M_Earth")
    print(f"  R_g         = {R_g*1e3:.3f} мм")
    print(f"  Gamma_SR    = {Gamma_SR:.4e} с⁻¹")
    print(f"  tau_SR      = {tau_SR*1e6:.3f} мкс")
    print(f"  T_H         = {T_H_K:.4e} К")
    print(f"  T_H         = {T_H_eV*1e6:.3f} мкЭВ")
    print(f"  T_H > m_a   = {T_H_eV > m_a_eV}")
    print("=" * 78)
    print("  Расчёт завершён.")
    print("=" * 78)


if __name__ == "__main__":
    main()