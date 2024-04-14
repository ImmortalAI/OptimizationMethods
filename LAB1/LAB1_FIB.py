from LAB1_PLOTTER import *


def solve_func(x0): return coefficient[0] * x0 ** 3 + coefficient[1] * x0 ** 2 + coefficient[2] * x0 + coefficient[3]


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
    print("-> ШАГ 1")
    print(f"L0 = [{ak}; {bk}], l = {epsilon}, ε = {eps}")
    print("-> ШАГ 2")
    print(f"N = {len(fib_list) - 1}")
    print("-> ШАГ 3")
    print("k = 0")
    print("-> ШАГ 4")
    print(f'y0 = {yk:.3f}, z0 = {zk:.3f}')

    plot_x = [ak, bk, yk, zk]
    plot_state = 0

    while k != len(fib_list) - 3:
        print(f"--- Итерация {k + 1} ---")
        print("-> ШАГ 5")
        print(f'f(y{k}) = {solve_func(yk):.3f}, f(z{k}) = {solve_func(zk):.3f}')
        print("-> ШАГ 6")
        print(f"Сравним f(y{k}) и f(z{k})...", end='\t')
        if solve_func(yk) <= solve_func(zk):
            print(f"{solve_func(yk):.3f} <= {solve_func(zk):.3f}")
            bk = zk
            zk = yk
            yk = ak + fib_list[-4 - k] / fib_list[-2 - k] * (bk - ak)
            if k == 0:
                plot_state = 3
            print("-> ШАГ 6(а)")
            print(f'Положим a{k + 1} = {ak:.3f}, b{k + 1} = {bk:.3f}, y{k + 1} = {yk:.3f}, z{k + 1} = {zk:.3f}')
        else:
            print(f"{solve_func(yk):.3f} > {solve_func(zk):.3f}")
            ak = yk
            yk = zk
            zk = ak + fib_list[-3 - k] / fib_list[-2 - k] * (bk - ak)
            if k == 0:
                plot_state = 4
            print("-> ШАГ 6(б)")
            print(f'Положим a{k + 1} = {ak:.3f}, b{k + 1} = {bk:.3f}, y{k + 1} = {yk:.3f}, z{k + 1} = {zk:.3f}')
        print("-> ШАГ 7")
        if k == len(fib_list) - 4:
            print(f"k = N - 3 ({k} = {len(fib_list) - 4})")
        else:
            print(f"k ≠ N - 3 ({k} ≠ {len(fib_list) - 4})")
            print(f"ШАГ 7(б) => ШАГ 5, k = {k + 1}")
        k += 1
    print("-> ШАГ 7(а)")
    print("Выполним N-ое вычисление функции для получения решения:")
    yN1 = (ak + bk) / 2
    zN1 = yN1 + eps
    print(f"Положим y{len(fib_list) - 2} = {yN1:.3f}, z{len(fib_list) - 2} = {zN1:.3f}")
    print(f"Сравним f(y{len(fib_list) - 2}) и f(z{len(fib_list) - 2})...", end='\t')
    if solve_func(yN1) <= solve_func(zN1):
        bk = zN1
        print(f"{solve_func(yN1):.3f} <= {solve_func(zN1):.3f}.")
        print(f'Положим a{len(fib_list) - 2} = {ak:.3f}, b{len(fib_list) - 2} = {bk:.3f}')
    else:
        ak = yN1
        print(f"{solve_func(yN1):.3f} > {solve_func(zN1):.3f}.")
        print(f'Положим a{len(fib_list) - 2} = {ak:.3f}, b{len(fib_list) - 2} = {bk:.3f}')
    print("\n*** Конец метода чисел Фибоначчи ***\n")
    graph_x = np.linspace(a0, b0, int((b0 - a0) / 0.005))
    create_plot(graph_x, solve_func(graph_x), plot_x, [solve_func(i) for i in plot_x],
                ['ak', 'bk', 'xk', 'yk', 'zk'], plot_state, "fib_method")
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


f_method = fibonacci_number_method()
print('Метод чисел Фибоначчи:')
print(f'Min f(x*) = {f_method[1]:.3f}, x* = {f_method[0]:.3f}')
print(f'Количество итераций: {f_method[2]}')