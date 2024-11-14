import pandas as pd
import numpy as np


def series_data(name, index):
    # Генерация всех положительных нечетных чисел, меньших 10000 и кратных 15
    odds = np.arange(15, 10000, 30)  # 15, 45, 75, ..., 9990
    s = pd.Series(odds, name=name)  # Создание Series с указанным названием

    # Преобразование чисел, начиная с указанного индекса
    for i in range(index - 1, len(s)):  # Индекс в Python начинается с 0
        if (i + 1) % 2 == 1:  # Не четный индекс
            s[i] *= 2
        else:  # Четный индекс
            s[i] -= 70

    # Находим значения с индексами index, index+1, index-5
    index_values = [index - 1, index, index - 6]  # Корректируем индексы для Python
    valid_values = [s[i] for i in index_values if 0 <= i < len(s)]  # Проверка на допустимость индексов

    # Возвращаем наибольшее значение
    return max(valid_values)


if __name__ == "__main__":
    print(series_data('Название серии', 8))
    print(series_data('Название серии', 18))