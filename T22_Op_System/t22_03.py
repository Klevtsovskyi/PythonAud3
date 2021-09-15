

import os
import sys


def compare(dir1, dir2):
    set1 = set(os.listdir(dir1))
    set2 = set(os.listdir(dir2))

    for name in set1 & set2:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if (os.path.isfile(path1) and os.path.isfile(path2)):
            size1 = os.path.getsize(path1)
            size2 = os.path.getsize(path2)
            if size1 > size2:
                print("Файл {} з каталогу {} ({} байт) більший "
                      "за файл з каталогу {} ({} байт)"
                      .format(name, dir1, size1,
                              dir2, size2))
            elif size1 == size2:
                print("Файли {} мають днаковий розмір ({} байт)".format(name, size1))
            else:
                print("Файл {} з каталогу {} ({} байт) більший "
                      "за файл з каталогу {} ({} байт)"
                      .format(name, dir2, size2,
                              dir1, size1))
            print("Різниця в розмірі: ",
                  abs(size2 - size1))


if __name__ == '__main__':
    root = sys.path[0]
    dir1 = "dir1"
    dir2 = "dir2"
    os.chdir(root)
    compare(dir1, dir2)
