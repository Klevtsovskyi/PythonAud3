

import os
import sys


def compare(dir1, dir2):
    set1 = set(os.listdir(dir1))
    set2 = set(os.listdir(dir2))
    print("Файли, що присутні в {} та відсутні в {}"
          .format(dir1, dir2))
    for name in set1 - set2:
        print(name)


if __name__ == '__main__':
    newout = open("output.txt", "w", encoding="utf-8")
    oldout = sys.stdout
    sys.stdout = newout

    dir1 = os.path.join(sys.path[0], "dir1")
    dir2 = os.path.join(sys.path[0], "dir2")
    compare(dir1, dir2)
    compare(dir2, dir1)

    sys.stdout = oldout
    newout.close()
