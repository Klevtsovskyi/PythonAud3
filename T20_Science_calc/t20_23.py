import numpy as np


TEST_NUM = 10000
RED = 0
BLUE = 1
BLACK = 2


def check(choice, to_obtain):
    rez = np.zeros(choice.shape[0], dtype=bool)
    for i in range(choice.shape[0]):
        k = 0
        for j in range(choice.shape[1]):
            if choice[i, j] == to_obtain[k]:
                k += 1
                if k == len(to_obtain):
                    rez[i] = True
                    break
        else:
            rez[i] = False
    return rez


def beads_probability(beads, count, to_obtain):
    choice = np.zeros((TEST_NUM, count))
    for i in range(TEST_NUM):
        choice[i, :] = np.random.choice(beads, count, replace=False)
    choice.sort(axis=1)
    to_obtain = np.sort(to_obtain)
    rez = check(choice, to_obtain)
    return np.sum(rez) / TEST_NUM


if __name__ == "__main__":
    beads = np.array(
        (RED, RED, RED, RED, BLUE, BLUE, BLUE, BLUE, BLACK, BLACK, BLACK, BLACK)
    )
    p = beads_probability(beads, 3, (BLACK, BLACK))
    print(p)
