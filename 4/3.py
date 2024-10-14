import numpy as np


def function(a, b, c):
    M = np.array([
        [1, 0, 1, 0],
        [a, 0, b, -c],
        [-4, 4, 0, 1],
        [-1, 1, -2, 1]
    ])
    V = np.array([2, 0, 5, -2])
    res = np.linalg.solve(M, V)
    return int(res[0] + res[1] + res[2] + res[3])


if __name__ == "__main__":
    print(function(12, 6, 1))
    print(function(12, 6, 71))
