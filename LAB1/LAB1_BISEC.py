import math
from LAB1_PLOTTER import *


def solve_func(x0): return coefficient[0] * x0 ** 3 + coefficient[1] * x0 ** 2 + coefficient[2] * x0 + coefficient[3]


def bisection_method():
    print("\n*** Метод половинного деления ***", end='\n\n')
    k = 0
    ak = a0
    bk = b0
    print("-> ШАГ 1")
    print(f"L0 = [{ak}; {bk}], ε = {epsilon}")
    print("-> ШАГ 2")
    print("k = 0")

    xk = (ak + bk) / 2
    L2k = bk - ak
    print("-> ШАГ 3")
    print(f"x{k} = {xk:.3f}, |L2{k}| = {L2k}, f(x{k}) = {solve_func(xk):.3f}")

    plot_x = []
    plot_state = 0

    while math.fabs(bk - ak) > epsilon:
        print(f"--- Итерация {k+1} ---")
        yk = ak + (bk - ak) / 4
        zk = bk - (bk - ak) / 4
        if k == 0:
            plot_x.append(ak)
            plot_x.append(bk)
            plot_x.append(xk)
            plot_x.append(yk)
            plot_x.append(zk)
        print("-> ШАГ 4")
        print(f"y{k} = {yk:.3f}, z{k} = {zk:.3f}, f(y{k}) = {solve_func(yk):.3f}, f(z{k}) = {solve_func(zk):.3f}")

        print("-> ШАГ 5")
        print(f"Сравним значения f(y{k}) и f(x{k})...", end='\t')
        if solve_func(yk) < solve_func(xk):
            print(f"{solve_func(yk):.3f} < {solve_func(xk):.3f}")
            bk = xk
            xk = yk
            print("-> ШАГ 5(а)")
            print(f'Положим b{k+1} = {bk:.3f}, a{k+1} = {ak:.3f}, x{k+1} = {xk:.3f}, f(x{k+1}) = {solve_func(xk):.3f}')
        else:
            print(f"{solve_func(yk):.3f} >= {solve_func(xk):.3f}")
            print("-> ШАГ 5(б) => ШАГ 6")
            print("-> ШАГ 6")
            print(f"Сравним значения f(z{k}) и f(x{k})...", end='\t')
            if solve_func(zk) < solve_func(xk):
                print(f"{solve_func(zk):.3f} < {solve_func(xk):.3f}")
                ak = xk
                xk = zk
                if k == 0:
                    plot_state = 1
                print("-> ШАГ 6(а)")
                print(f'Положим a{k + 1} = {ak:.3f}, b{k + 1} = {bk:.3f}, x{k + 1} = {xk:.3f}, f(x{k+1}) = {solve_func(xk):.3f}')
            else:
                print(f"{solve_func(zk):.3f} >= {solve_func(xk):.3f}")
                ak = yk
                bk = zk
                if k == 0:
                    plot_state = 2
                print("-> ШАГ 6(б)")
                print(f'Положим a{k + 1} = {ak:.3f}, b{k + 1} = {bk:.3f}, x{k + 1} = {xk:.3f}, f(x{k+1}) = {solve_func(xk):.3f}')
        print("-> ШАГ 7")
        print("Проверим условие окончания... ")
        if math.fabs(bk - ak) <= epsilon:
            print(f"L2{k+1} <= ε ({math.fabs(bk - ak):.3f} <= {epsilon})")
            print(f"ШАГ 7(а)")
            print(f"Поиск закончен, x* = [{ak:.3f}; {bk:.3f}]")
        else:
            print(f"L2{k + 1} > ε ({math.fabs(bk - ak):.3f} > {epsilon})")
            print(f"ШАГ 7(б) => ШАГ 4, k = {k+1}")
        k += 1
    print("\n*** Конец метода половинного деления ***\n")
    graph_x = np.linspace(a0, b0, int((b0 - a0) / 0.005))
    create_plot(graph_x, solve_func(graph_x), plot_x, [solve_func(i) for i in plot_x],
                ['ak', 'bk', 'xk', 'yk', 'zk'], plot_state, "div_method")
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

b_method = bisection_method()
print('Метод половинного деления:')
print(f'Min f(x*) = {b_method[1]:.3f}, x* = {b_method[0]:.3f}')
print(f'Количество итераций: {b_method[2]}')
