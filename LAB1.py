import matplotlib.pyplot as plt
import numpy as np
import math

coefficient = [2., 9., 0., -21.]


def solve_func(x0):
    return coefficient[0] * x0 ** 3 + coefficient[1] * x0 ** 2 + coefficient[2] * x0 + coefficient[3]


def bisection_method():
    print("\n*** Метод половинного деления ***", end='\n\n')
    k = 0
    ak = a0
    bk = b0
    print(f"Левая граница - {a0:.3f}, правая граница - {b0:.3f}")

    center = (ak + bk) / 2
    print(f"Центр - {center}")

    plot_x = []
    plot_state = 0

    while math.fabs(bk - ak) > epsilon:
        print(f"|bk - ak| ({math.fabs(bk - ak):.3f}) > epsilon ({epsilon:.3f})")
        print(f"--- Итерация {k + 1} ---")
        yk = ak + math.fabs(bk - ak) / 4
        zk = bk - math.fabs(bk - ak) / 4
        if k == 0:
            plot_x.append(ak)
            plot_x.append(bk)
            plot_x.append(center)
            plot_x.append(yk)
            plot_x.append(zk)
        print(f"Четверть слева - {yk:.3f}, четверть справа - {zk:.3f}")

        print("Сравниваем значения функции слева от центра...", end='\t')
        if solve_func(yk) < solve_func(center):
            print(f"{solve_func(yk):.3f} < {solve_func(center):.3f}")
            bk = center
            center = yk
        else:
            print(f"{solve_func(yk):.3f} >= {solve_func(center):.3f}")
            print("Сравниваем значения функции справа от центра...", end='\t')
            if solve_func(zk) < solve_func(center):
                print(f"{solve_func(zk):.3f} < {solve_func(center):.3f}")
                ak = center
                center = zk
                if k == 0:
                    plot_state = 1
            else:
                print(f"{solve_func(zk):.3f} >= {solve_func(center):.3f}")
                ak = yk
                bk = zk
                if k == 0:
                    plot_state = 2
        print(f"Новый интервал - [{ak:.3f}; {bk:.3f}]")
        print(f"Новый центр - {center:.3f}")
        k += 1
        print(f"--- Конец итерации {k} ---")
    print(f"|bk - ak| ({math.fabs(bk - ak):.3f}) <= epsilon ({epsilon:.3f})")
    print("\n*** Конец метода половинного деления ***\n")
    create_plot(plot_x, ['ak', 'bk', 'xk', 'yk', 'zk'], plot_state)
    return [(ak + bk) / 2, solve_func((ak + bk) / 2), k]


def golden_ratio_method():
    print("\n*** Метод золотого сечения ***", end='\n\n')
    k = 0
    ak = a0
    bk = b0
    yk = a0 + (3. - math.sqrt(5)) / 2 * (b0 - a0)
    zk = a0 + b0 - yk
    print(f"Левая граница - {a0:.3f}, правая граница - {b0:.3f}")

    plot_x = [ak, bk, yk, zk]
    plot_state = 0

    while math.fabs(bk - ak) > epsilon:
        print(f"|bk - ak| ({math.fabs(bk - ak):.3f}) > epsilon ({epsilon:.3f})")
        print(f"--- Итерация {k + 1} ---")
        print(f'Точки "золотого сечения" слева - {yk:.3f}, справа - {zk:.3f}')
        print("Сравниваем значения функции слева и справа в точках \"золотого сечения\"...", end='\t')

        if solve_func(yk) <= solve_func(zk):
            print(f"{solve_func(yk):.3f} <= {solve_func(zk):.3f}")
            bk = zk
            zk = yk
            yk = ak + bk - yk
            if k == 0:
                plot_state = 3
        else:
            print(f"{solve_func(yk):.3f} > {solve_func(zk):.3f}")
            ak = yk
            yk = zk
            zk = ak + bk - zk
            if k == 0:
                plot_state = 4
        print(f"Новый интервал - [{ak:.3f}; {bk:.3f}]")
        print(f'Новые точки "золотого сечения" слева - {yk:.3f}, справа - {zk:.3f}')
        k += 1
        print(f"--- Конец итерации {k} ---")
    print(f"|bk - ak| ({math.fabs(bk - ak):.3f}) <= epsilon ({epsilon:.3f})")
    print("\n*** Конец метода золотого сечения ***\n")
    create_plot(plot_x, ['ak', 'bk', 'yk', 'zk'], plot_state)
    return [(ak + bk) / 2, solve_func((ak + bk) / 2), k]


def fibonacci_set():
    fib_list = [1, 1]
    i = 2
    while fib_list[i - 1] < (b0 - a0) / epsilon:
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        i += 1
    return fib_list


def fibonacci_number_method():
    print("\n*** Метод чисел Фибоначчи ***", end='\n\n')
    eps = epsilon / 2
    fib_list = fibonacci_set()

    k = 0
    ak = a0
    bk = b0
    yk = a0 + fib_list[-3] / fib_list[-1] * (b0 - a0)
    zk = a0 + fib_list[-2] / fib_list[-1] * (b0 - a0)
    print(f"Левая граница - {a0:.3f}, правая граница - {b0:.3f}")
    print(f'Точки, найденные при помощи последовательности Фибоначчи: слева - {yk:.3f}, справа - {zk:.3f}')

    plot_x = [ak, bk, yk, zk]
    plot_state = 0

    while k != len(fib_list) - 3:
        print(f"k ({k}) != N - 3 ({len(fib_list) - 3})")
        print(f"--- Итерация {k + 1} ---")
        print("Сравниваем значения функции слева и справа в этих точках...", end='\t')
        if solve_func(yk) <= solve_func(zk):
            print(f"{solve_func(yk):.3f} <= {solve_func(zk):.3f}")
            bk = zk
            zk = yk
            yk = ak + fib_list[-4 - k] / fib_list[-2 - k] * (bk - ak)
            if k == 0:
                plot_state = 3
        else:
            print(f"{solve_func(yk):.3f} > {solve_func(zk):.3f}")
            ak = yk
            yk = zk
            zk = ak + fib_list[-3 - k] / fib_list[-2 - k] * (bk - ak)
            if k == 0:
                plot_state = 4
        print(f"Новый интервал - [{ak:.3f}; {bk:.3f}]")
        print(f'Новые точки (последовательности Фибоначчи): слева - {yk:.3f}, справа - {zk:.3f}')
        k += 1
        print(f"--- Конец итерации {k} ---")
    print(f"k ({k}) = N - 3 ({len(fib_list) - 3})")
    print("Выполним N-ое вычисление функции для получения решения:")
    yN1 = (ak + bk) / 2
    zN1 = yN1 + eps
    print(f"Положим y(N-1) = {yN1:.3f}, z(N-1) = {zN1:.3f}")
    print("Сравним значения функции в этих точках... ", end='')
    if solve_func(yN1) <= solve_func(zN1):
        bk = zN1
        print(f"{solve_func(yN1):.3f} <= {solve_func(zN1):.3f}.\n Положим a(N-1) = {ak:.3f}, b(N-1) = {bk:.3f}")
    else:
        ak = yN1
        print(f"{solve_func(yN1):.3f} > {solve_func(zN1):.3f}.\n Положим a(N-1) = {ak:.3f}, b(N-1) = {bk:.3f}")
    print("\n*** Конец метода чисел Фибоначчи ***\n")
    create_plot(plot_x, ['ak', 'bk', 'yk', 'zk'], plot_state)
    return [(ak + bk) / 2, solve_func((ak + bk) / 2), k]


def create_plot(vert_line_points: list, vert_line_name: list, state: int):
    x = np.linspace(a0, b0, int((b0 - a0) / 0.005))
    y = solve_func(x)
    plt_min = min(y)
    x_step = (max(x) - min(x)) / 64
    y_step = (max(y) - plt_min) / 8
    if plt_min >= 0:
        plt_min = -y_step
    else:
        plt_min -= y_step

    plt.plot(x, y)
    for i in range(len(vert_line_points)):
        plt.plot([vert_line_points[i], vert_line_points[i]], [0, solve_func(vert_line_points[i])], color='k',
                 linestyle='--')
        plt.text(vert_line_points[i] + x_step, -y_step / 2, vert_line_name[i])
        plt.text(vert_line_points[i] - x_step * 4, solve_func(vert_line_points[i]) + y_step / 4,
                 f"f({vert_line_name[i]})")

    match state:
        case 0:
            plt.plot([vert_line_points[2], vert_line_points[2]], [0, plt_min], color='k')
            plt.plot([vert_line_points[0], vert_line_points[2]], [plt_min, plt_min], color='k')
            plt.text((vert_line_points[2] + vert_line_points[0]) / 2, plt_min + y_step / 4, "Новый интервал",
                     ha="center")
        case 1:
            plt.plot([vert_line_points[2], vert_line_points[2]], [0, plt_min], color='k')
            plt.plot([vert_line_points[2], vert_line_points[1]], [plt_min, plt_min], color='k')
            plt.text((vert_line_points[2] + vert_line_points[1]) / 2, plt_min + y_step / 4, "Новый интервал",
                     ha="center")
        case 2:
            plt.plot([vert_line_points[3], vert_line_points[3]], [0, plt_min], color='k')
            plt.plot([vert_line_points[4], vert_line_points[4]], [0, plt_min], color='k')
            plt.plot([vert_line_points[3], vert_line_points[4]], [plt_min, plt_min], color='k')
            plt.text((vert_line_points[3] + vert_line_points[4]) / 2, plt_min + y_step / 4, "Новый интервал",
                     ha="center")
        case 3:
            plt.plot([vert_line_points[3], vert_line_points[3]], [0, plt_min], color='k')
            plt.plot([vert_line_points[0], vert_line_points[3]], [plt_min, plt_min], color='k')
            plt.text((vert_line_points[0] + vert_line_points[3]) / 2, plt_min + y_step / 4, "Новый интервал",
                     ha="center")
        case 4:
            plt.plot([vert_line_points[2], vert_line_points[2]], [0, plt_min], color='k')
            plt.plot([vert_line_points[2], vert_line_points[1]], [plt_min, plt_min], color='k')
            plt.text((vert_line_points[2] + vert_line_points[1]) / 2, plt_min + y_step / 4, "Новый интервал",
                     ha="center")

    plt.plot([vert_line_points[0], vert_line_points[0]], [0, plt_min - y_step], color='k')
    plt.plot([vert_line_points[1], vert_line_points[1]], [0, plt_min - y_step], color='k')
    plt.plot([vert_line_points[0], vert_line_points[1]], [plt_min - y_step, plt_min - y_step], color='k')
    plt.text((vert_line_points[1] + vert_line_points[0]) / 2, plt_min - y_step + y_step / 4, "Текущий интервал",
             ha="center")
    plt.axhline(color='k', linewidth=2)
    plt.axvline(color='k', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции f(x)')
    plt.show()


print("!!! Предупреждение !!! Десятичная часть в вводе/выводе отделяется точкой!")
print("Ввод значений для функции вида f(x) = Ax^3 + Bx^2 + Cx + D")
coefficient[0] = float(input("Введите A... "))
coefficient[1] = float(input("Введите B... "))
coefficient[2] = float(input("Введите C... "))
coefficient[3] = float(input("Введите D... "))
a0, b0 = map(float, input("Введите интервал неопределённости в виде \"[a0;b0]\"... ")[1:-1].split(';'))
epsilon = float(input("Введите точность вычислений (epsilon)... "))

b_method = bisection_method()
print(
    f'Метод половинного деления: \nФункция f(x) принимает минимальное значение {b_method[1]:.3f} в точке x0 = {b_method[0]:.3f}. \nКоличество итераций - {b_method[2]}')
g_method = golden_ratio_method()
print(
    f'Метод "золотого сечения": \nФункция f(x) принимает минимальное значение {g_method[1]:.3f} в точке x0 = {g_method[0]:.3f}. \nКоличество итераций - {g_method[2]}')
f_method = fibonacci_number_method()
print(
    f'Метод чисел Фибоначчи: \nФункция f(x) принимает минимальное значение {f_method[1]:.3f} в точке x0 = {f_method[0]:.3f}. \nКоличество итераций - {f_method[2]}')