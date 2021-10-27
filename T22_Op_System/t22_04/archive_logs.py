import os
import sys
import datetime
import tarfile


def archive_logs(date):
    log_dir = os.path.join(sys.path[0], "logs")
    if os.path.exists(log_dir):
        lst = []
        for name in os.listdir(log_dir):
            if name.endswith(".log"):
                log_time = datetime.datetime.strptime(name,
                                                      "%Y%m%d_%H%M%S.log")
                if log_time < date:
                    lst.append(name)
        if lst:
            archive = os.path.join(log_dir, date.strftime("%Y%m%d_%H%M%S") + ".tar.gz")

            with tarfile.open(archive, "w:gz") as tf:
                for name in lst:
                    tf.add(os.path.join(log_dir, name), name)


if __name__ == "__main__":
    archive_date = datetime.datetime.now()
    archive_logs(archive_date)
