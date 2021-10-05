import numpy as np


TEST_NUM = 100000


def dices_win_probability(n_dice, max_win_value, _reward):
    dices = np.random.randint(1, 7, TEST_NUM * n_dice)
    dices.shape = (TEST_NUM, n_dice)
    value = np.sum(dices, axis=1)
    win = value[value <= max_win_value]
    return len(win) / TEST_NUM, _reward * len(win) - TEST_NUM


if __name__ == "__main__":
    reward = 10
    probability, money_won = dices_win_probability(4, 9, reward)
    print("Ймовірність перемоги: ", probability)
    print("Справедлива сума виграшу: ", 1 / probability)
    print("Поточна сума виграшу: ", reward)
    print("Кількість виграих грошей при {} повторень гри: {:.1f}"
          .format(TEST_NUM, money_won))
    print("Кількіість виграних грошей в середньому: {:.3f}"
          .format(money_won / TEST_NUM))
