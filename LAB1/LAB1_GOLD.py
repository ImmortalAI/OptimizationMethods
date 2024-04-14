import math
from LAB1_PLOTTER import *


def solve_func(x0): return coefficient[0] * x0 ** 3 + coefficient[1] * x0 ** 2 + coefficient[2] * x0 + coefficient[3]


def golden_ratio_method():
    print("\n*** Метод золотого сечения ***", end='\n\n')
    k = 0
    ak = a0
    bk = b0
    yk = a0 + (3. - math.sqrt(5)) / 2 * (b0 - a0)
    zk = a0 + b0 - yk
    print("-> ШАГ 1")
    print(f"L0 = [{ak}; {bk}], ε = {epsilon}")
    print("-> ШАГ 2")
    print("k = 0")
    print("-> ШАГ 3")
    print(f'y0 = {yk:.3f}, z0 = {zk:.3f}')

    plot_x = [ak, bk, yk, zk]
    plot_state = 0

    while math.fabs(bk - ak) > epsilon:
        print(f"--- Итерация {k + 1} ---")
        print("-> ШАГ 4")
        print(f'f(y{k}) = {solve_func(yk):.3f}, f(z{k}) = {solve_func(zk):.3f}')
        print("-> ШАГ 5")
        print(f"Сравним значения f(y{k}) и f(z{k})...", end='\t')
        if solve_func(yk) <= solve_func(zk):
            print(f"{solve_func(yk):.3f} <= {solve_func(zk):.3f}")
            bk = zk
            zk = yk
            yk = ak + bk - yk
            if k == 0:
                plot_state = 3
            print("-> ШАГ 5(а)")
            print(f'Положим a{k + 1} = {ak:.3f}, b{k + 1} = {bk:.3f}, y{k + 1} = {yk:.3f}, z{k + 1} = {zk:.3f}')
        else:
            print(f"{solve_func(yk):.3f} > {solve_func(zk):.3f}")
            ak = yk
            yk = zk
            zk = ak + bk - zk
            if k == 0:
                plot_state = 4
            print("-> ШАГ 5(б)")
            print(f'Положим a{k + 1} = {ak:.3f}, b{k + 1} = {bk:.3f}, y{k + 1} = {yk:.3f}, z{k + 1} = {zk:.3f}')
        print("-> ШАГ 6")
        print(f"Δ = {math.fabs(bk - ak):.3f}")
        if math.fabs(bk - ak) <= epsilon:
            print(f"L2{k + 1} <= ε ({math.fabs(bk - ak):.3f} <= {epsilon})")
            print(f"ШАГ 6(а)")
            print(f"Поиск закончен, x* = [{ak:.3f}; {bk:.3f}]")
        else:
            print(f"L2{k + 1} > ε ({math.fabs(bk - ak):.3f} > {epsilon})")
            print(f"ШАГ 6(б) => ШАГ 4, k = {k + 1}")
        k += 1
    print("\n*** Конец метода золотого сечения ***\n")
    graph_x = np.linspace(a0, b0, int((b0 - a0) / 0.005))
    create_plot(graph_x, solve_func(graph_x), plot_x, [solve_func(i) for i in plot_x],
                ['ak', 'bk', 'xk', 'yk', 'zk'], plot_state, "gold_method")
    return [(ak + bk) / 2, solve_func((ak + bk) / 2), k]



print("!!! Предупреждение !!! Десятичная часть в вводе/выводе отделяется точкой!")
print("Ввод значений для функции вида f(x) = Ax^3 + Bx^2 + Cx + D")
coefficient = [0., 0., 0., 0.]
coefficient[0] = float(input("Введите A... "))
coefficient[1] = float(input("Введите B... "))
coefficient[2] = float(input("Введите C... "))
coefficient[3] = float(input("Введите D... "))
a0, b0 = map(float, input("Введите интервал неопределённости в виде \"[a0;b0]\"... ")[1:-1].split(';'))
epsilon = float(input("Введите точность вычислений (epsilon)... "))


g_method = golden_ratio_method()
print('Метод "золотого сечения":')
print(f'Min f(x*) = {g_method[1]:.3f}, x* = {g_method[0]:.3f}')
print(f'Количество итераций: {g_method[2]}')
