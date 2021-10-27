import os
import time


def get_oldest_file(dirr):
    oldest_time = time.time()
    oldest_name = ""

    for root, dirs, files in os.walk(dirr):
        for name in files:
            path = os.path.join(root, name)
            curr_time = os.path.getctime(path)
            if curr_time < oldest_time:
                oldest_time = curr_time
                oldest_name = path

    return oldest_name, oldest_time


if __name__ == '__main__':
    dirr = input()
    filename, createtime = get_oldest_file(dirr)
    print(filename, time.ctime(createtime))
