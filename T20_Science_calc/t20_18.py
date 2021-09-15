

import numpy as np


TEST_NUM = 100000


def dices_win_probability(n_dice, max_win_value, win_money):
    dices = np.random.randint(1, 7, TEST_NUM * n_dice)
    # print(dices)
    dices.shape = (TEST_NUM, n_dice)
    # print(dices)
    value = np.sum(dices, axis=1)
    # print(value)
    win = value[value <= max_win_value]
    # print(win)
    return len(win) / TEST_NUM, -TEST_NUM + win_money * len(win)


if __name__ == '__main__':
    win_money = 10
    p, m = dices_win_probability(4, 9, win_money)
    print("Ймовірність перемоги: ", p)
    print("Справедлива сума виграшу: ", 1/p)
    print("Поточна сума виграшу: ", win_money)
    print("Кількість виграих грошей при {} повторень гри: {:.1f}"
          .format(TEST_NUM, m))
    print("Кількіість виграних грошей в середньому: {:.3f}"
          .format(m / TEST_NUM))
