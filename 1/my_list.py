from string import ascii_letters
from random import choice
from sys import getsizeof


def my_list(n):
    first_number = None

    for i in range(n + 1, 100000):
        if i % 724 == 0:
            first_number = i
            break

    if first_number is None:
        return 0

    first_array = []
    number = first_number
    while (number < 100000):
        first_array.append(number)
        number += 724

    if len(first_array) < 70:
        return None

    second_array = first_array[49:70]

    second_array.pop(10)

    result = round(sum(second_array) / len(second_array))
    return result


def work(n):
    set_1 = set([i for i in range(2, n + 1, 2)])
    set_2 = set([i for i in range(5, 101, 5)])

    sum_1 = sum(set_1.union(set_2))
    sum_2 = sum(set_1.intersection(set_2))

    return sum_1 + sum_2


def weather_forecast(day):
    weather_station_1 = {
        1: [20, 735],
        2: [21, 737],
        3: [23, 740],
        4: [20, 739],
        5: [21, 750],
        6: [21, 751],
        7: [22, 749],
        8: [19, 745],
        9: [22, 752],
        10: [23, 753]
    }

    weather_station_2 = {
        1: [20, 89],
        2: [20, 90],
        3: [24, 95],
        4: [20, 88],
        5: [21, 87],
        6: [21, 80],
        7: [22, 72],
        8: [18, 80],
        9: [22, 75],
        10: [23, 78]
    }

    temperature = (weather_station_1[day][0] + weather_station_2[day][0]) / 2
    atmo = weather_station_1[day][1]
    liq = weather_station_2[day][1]

    return temperature + atmo + liq


def generate(): return ["".join([choice(ascii_letters) for i in range(5)]) for j in range(1000)]


def yield_generate():
    for j in range(1000):
        yield from generate()


def check_generator():
    mas_gen = ["".join([choice(ascii_letters) for i in range(5)]) for j in range(1000)]
    print(mas_gen)
    mem1 = getsizeof(mas_gen)

    def yield_generate():
        for j in range(1000):
            yield "".join([choice(ascii_letters) for i in range(5)]) 

    generator = yield_generate()
    first = next(generator)
    print(first)
    second = next(generator)
    print(second)
    mem2 = getsizeof(second)

    return mem1 - mem2


def function(n):
    list_1 = [i for i in range(1, 101)]

    filtered = list(filter(lambda x: x % n == 0, list_1))

    list_2 = list(map(lambda x: x * x, filtered))

    list_3 = list(zip(filtered, list_2))
    sum_1 = sum([i[0] + i[1] for i in list_3])
    return sum_1

if __name__ == "__main__":
    print(check_generator())
    print(function(3))
