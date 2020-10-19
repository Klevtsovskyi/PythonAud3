

import numpy as np


TEST_NUM = 10000
RED = 0
BLUE = 1
BLACK = 2


def check(choice, to_extract):
    rez = np.zeros(choice.shape[0])
    for i in range(choice.shape[0]):
        k = 0
        for j in range(choice.shape[1]):
            if k < len(to_extract) and choice[i, j] == to_extract[k]:
                k += 1
        if k == len(to_extract):
            rez[i] = True
        else:
            rez[i] = False
    return rez


def beads_probability(beads, count, to_extract):
    choice = np.zeros((TEST_NUM, count))
    for i in range(TEST_NUM):
        choice[i, :] = np.random.choice(beads, count, replace=False)
    choice = np.sort(choice, axis=1)
    to_extract = np.sort(to_extract)
    rez = check(choice, to_extract)
    return np.sum(rez) / TEST_NUM


if __name__ == '__main__':
    beads = np.array([RED, RED, RED, RED,
                      BLUE, BLUE, BLUE, BLUE,
                      BLACK, BLACK, BLACK, BLACK])
    p = beads_probability(beads, 3, (BLACK, BLACK))
    print(p)
