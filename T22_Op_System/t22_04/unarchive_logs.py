import os
import sys
import datetime
import tarfile


def unarchive_logs(date):
    log_dir = os.path.join(sys.path[0], "logs")
    assert os.path.exists(log_dir)

    for name in os.listdir(log_dir):
        if name.endswith(".tar.gz"):
            log_date = datetime.datetime.strptime(name, "%Y%m%d_%H%M%S.tar.gz")
            if log_date < date:
                archive = os.path.join(log_dir, name)
                with tarfile.open(archive, "r:gz") as tf:
                    tf.extractall(log_dir)
                os.remove(archive)


if __name__ == "__main__":
    date = datetime.datetime.now()
    unarchive_logs(date)
