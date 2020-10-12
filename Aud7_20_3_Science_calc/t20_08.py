

import numpy as np


def signsort_v1(x):
    neg = []
    pos = []
    for i in range(x.size):
        if x[i] < 0:
            neg.append(x[i])
        else:
            pos.append((x[i]))
    return np.array(neg + pos)


def signsort_v2(x):
    neg = x[x < 0]
    pos = x [x >= 0]
    return np.hstack((neg, pos))


if __name__ == '__main__':
    x = np.array([9, 2, -1, 3, -2, -3, 0, 7, -4])
    print(signsort_v1(x))
    print(signsort_v2(x))
