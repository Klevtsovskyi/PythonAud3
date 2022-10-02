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
                    def is_within_directory(directory, target):
                        
                        abs_directory = os.path.abspath(directory)
                        abs_target = os.path.abspath(target)
                    
                        prefix = os.path.commonprefix([abs_directory, abs_target])
                        
                        return prefix == abs_directory
                    
                    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                    
                        for member in tar.getmembers():
                            member_path = os.path.join(path, member.name)
                            if not is_within_directory(path, member_path):
                                raise Exception("Attempted Path Traversal in Tar File")
                    
                        tar.extractall(path, members, numeric_owner) 
                        
                    
                    safe_extract(tf, log_dir)
                os.remove(archive)


if __name__ == "__main__":
    date = datetime.datetime.now()
    unarchive_logs(date)
