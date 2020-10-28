

import os
import sys
import time
import datetime


def compare(dir1, dir2):
    set1 = set(os.listdir(dir1))
    set2 = set(os.listdir(dir2))

    for name in set1 & set2:
        path1 = os.path.join(dir1, name)
        path2 = os.path.join(dir2, name)
        if (os.path.isfile(path1) and os.path.isfile(path2)):
            ctime1 = os.path.getctime(path1)
            ctime2 = os.path.getctime(path2)
            if ctime1 > ctime2:
                print("Файл {} з каталогу {} ({}) був створений пізніше"
                      "за файл з каталогу {} ({})"
                      .format(name, dir1, time.ctime(ctime1),
                              dir2, time.ctime(ctime2)))
            elif ctime1 == ctime1:
                print("Файли {} було створено одночасно".format(name))
            else:
                print("Файл {} з каталогу {} ({}) був створений пізніше"
                      "за файл з каталогу {} ({})"
                      .format(name, dir2, time.ctime(ctime2),
                              dir1, time.ctime(ctime1)))
            print("Різниця в часі: ",
                  datetime.timedelta(abs(ctime2 - ctime1)/60/60/24))


if __name__ == '__main__':
    root = sys.path[0]
    dir1 = "dir1"
    dir2 = "dir2"
    os.chdir(root)
    compare(dir1, dir2)
