import numpy as np


TEST_NUM = 10000


def krap_play(n_dice, win_values, lose_values, lose_values_repeat):
    dices = np.random.randint(1, 7, n_dice)
    value = np.sum(dices)
    if value in lose_values:
        return False
    elif value in win_values:
        return True
    else:
        our_value = value
        while True:
            dices = np.random.randint(1, 7, n_dice)
            value = np.sum(dices)
            if value in lose_values_repeat:
                return False
            elif value == our_value:
                return True


def krap_win_probability(n_dice, win_values, lose_values, lose_values_repeat):
    rez = np.zeros(TEST_NUM)
    for i in range(TEST_NUM):
        rez[i] = krap_play(n_dice, win_values, lose_values, lose_values_repeat)
    return np.sum(rez) / TEST_NUM


if __name__ == "__main__":
    p = krap_win_probability(2, (7, 11), (2, 3, 13), (7, ))
    print(p)
