

import numpy as np


def norm_v1(x, axis=0):
    if axis == 0:
        m = 0
        for j in range(x.shape[1]):
            s = 0
            for i in range(x.shape[0]):
                s += abs(x[i, j])
            if s > m:
                m = s
        return m
    if axis == 1:
        m = 0
        for i in range(x.shape[0]):
            s = 0
            for j in range(x.shape[1]):
                s += abs(x[i, j])
            if s > m:
                m = s
        return m


def norm_v2(x, axis=0):
    return np.max(np.sum(np.abs(x), axis=axis))



if __name__ == '__main__':
    x = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [-7, -8, -9]])
    print(x)
    print("Norm 1: ", norm_v1(x, 1))
    print("Norm 2: ", norm_v1(x, 0))

    print("Norm 1: ", norm_v2(x, 1))
    print("Norm 2: ", norm_v2(x, 0))
