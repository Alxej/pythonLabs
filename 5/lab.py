import scipy.integrate as integrate
import math
import sympy as smp
import numpy as np
import matplotlib.pyplot as plt


from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.stats import uniform
from IPython.display import display


def first_task():
    first_integral = integrate.quad(lambda x: 2-x, -2, 3)
    second_integral = integrate.dblquad(
        lambda x,y: (math.exp(x / 100)) * (math.exp(y / 1000)),  # noqa E501
        1, 10,
        1, 10
    )
    return (first_integral[0], second_integral[0])


# Правая часть дифференциального уравнения
def f(y, x):
    return x + 1


def second_task():
    y0 = 1.0  # Начальное условие
    step_count = 200  # Количество шагов разбиения отрезка для численного интегрирования # noqa E501
    x_output = np.linspace(0, 1, step_count)  # Разделение отрезка [0, 1] на step_count  # noqa E501
    y_result = odeint(f, y0, x_output)  # Решение уравнения
    # print(y_result)
    print(y_result[-1] - odeint(f, y0, np.linspace(0, 1, 2))[-1])
    return y_result[-1]


# Функция из задания
def f1(x):
    return (-math.cos(x)) ** 3


def third_task():
    razbienie10 = np.linspace(0, 10, 11, endpoint=True)  # Разбиение отрезка [0, 11] на 11 точек с концом в 10 # noqa E501
    applyall = np.vectorize(f1)  # Преобразование функции к функции для массива
    values10 = applyall(razbienie10)  # Применение функции ко всем элементам массива # noqa E501
    razbienie100 = np.linspace(0, 10, 101, endpoint=True)  # Разбиение отрезка [0, 11] на 11 точек с концом в 10 # noqa E501
    lin = interp1d(razbienie10, values10)  # Линейная интерполяция
    cub = interp1d(razbienie10, values10, kind='cubic')  # Кубическая интерполяция  # noqa E501
    plt.plot(razbienie10, values10, 'o',
             razbienie100, lin(razbienie100), '-',
             razbienie100, cub(razbienie100), '--')
    plt.legend(['Данные', 'линейная', 'кубическая'], loc='best')
    plt.show()


def fourth_task():
    raspr = uniform(loc=10, scale=10)  # Равномерное распределение на отрезке от 10 до 20  # noqa E501
    values = np.sort(raspr.rvs(size=20))  # Сгенерированная выборка  # noqa E501
    print("Сгенерированная выборка ", values)
    func_raspr15 = raspr.cdf(15)  # Функция распределения в точке 15
    print("Функция распределения в точке 15 ", func_raspr15)
    plotn15 = raspr.pdf(15)  # Плотность распределения в точке 15
    print("Плотность распределения в точке 15 ", plotn15)
    plt.subplot(2, 1, 1)
    plt.plot(np.arange(10, 21, 1), raspr.cdf(np.arange(10, 21, 1)))
    plt.legend(["Функция распр."])
    plt.subplot(2, 1, 2)
    plt.plot(np.arange(10, 21, 1), raspr.pdf(np.arange(10, 21, 1)))
    plt.legend(["Плотность распр."])
    plt.show()


def fifth_task():
    x = smp.Symbol('x')  # Символьная переменная
    expr = (-3 * (x ** 2) + x - 3) / (-(x ** 2) - x + 3)
    display(smp.limit(expr, x, smp.oo))


if __name__ == "__main__":
    print("Первое задание: ", first_task())
    print("Второе задание: ", second_task())
    print("Третье задание: ")
    third_task()
    print("Четвертое задание: ")
    fourth_task()
    print("Пятое задание: ")
    fifth_task()
