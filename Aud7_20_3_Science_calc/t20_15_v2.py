

import numpy as np


def dis(x1 ,x2):
    return np.sqrt(np.sum((x2 - x1)**2, axis=1))


def is_eq_dis(x):
    x1 = np.vstack((x[1:], x[:1]))
    diss = dis(x, x1)
    diss0 = np.ones_like(diss)
    diss0.fill(diss[0])
    return np.all(np.isclose(diss, diss0))


def count_eq_triangles(x):
    y = x.copy()
    y.shape = (x.size // 2, 2)
    count = 0
    for i in range(y.shape[0]):
        for j in range(i + 1, y.shape[0]):
            for k in range(j + 1, y.shape[0]):
                cur = y[np.array((i, j, k))]
                if is_eq_dis(cur):
                    count += 1
    return count


if __name__ == '__main__':
    points = np.array([-1, 0, 1, 0, 0, np.sqrt(3), 0, -np.sqrt(3)])
    #print(points)
    print(count_eq_triangles(points))
