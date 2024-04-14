import matplotlib.pyplot as plt
import numpy as np


def create_plot(x, y, vert_line_points, vert_line_Ypoints, vert_line_name, state, plot_name):
    plt_min = min(y)
    x_step = (max(x) - min(x)) / 64
    y_step = (max(y) - plt_min) / 8
    if plt_min >= 0:
        plt_min = -y_step
    else:
        plt_min -= y_step

    plt.plot(x, y)
    for i in range(len(vert_line_points)):
        plt.plot([vert_line_points[i], vert_line_points[i]], [0, vert_line_Ypoints[i]], color='k',
                 linestyle='--')
        plt.text(vert_line_points[i] + x_step, -y_step / 2, vert_line_name[i])
        plt.text(vert_line_points[i] - x_step * 4, vert_line_Ypoints[i] + y_step / 4,
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
    plt.savefig(f"LAB1/{plot_name}.png")
    plt.clf()