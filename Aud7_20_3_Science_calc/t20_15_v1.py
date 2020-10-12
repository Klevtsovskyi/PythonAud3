

import numpy as np


def dis(x1 ,x2):
    return np.sqrt(np.sum((x2 - x1)**2))
    return np.sqrt((x2[0] - x1[0])**2 +(x2[1] - x2[1])**2)


def is_eq_triangle(x1, x2, x3):
    a = dis(x1, x2)
    b = dis(x2, x3)
    c = dis(x3, x1)
    return np.all((np.isclose(a, b), np.isclose(b, c)))


def count_eq_triangles(x):
    count = 0
    for i in range(0, x.size, 2):
        for j in range(i + 2, x.size, 2):
            for k in range(j + 2, x.size, 2):
                x1 = x[i: i+2]
                x2 = x[j: j+2]
                x3 = x[k: k+2]
                if is_eq_triangle(x1 ,x2, x3):
                    count += 1
    return count


if __name__ == '__main__':
    points = np.array([-1, 0, 1, 0, 0, np.sqrt(3), 0, -np.sqrt(3)])
    print(count_eq_triangles(points))
