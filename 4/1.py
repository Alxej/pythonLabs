import numpy as np


def function(int_list: list):
    np_array = np.asarray(int_list)
    np_array[np_array < 0] += 3
    np_array[np_array > 0] *= 2
    np_array.sort()
    return np_array[-1] + np_array[-2]


if __name__ == "__main__":
    print(function([1, 2, 3, -3, 0]))
    print(function([1, 2, 3, -3, 13, 0]))
