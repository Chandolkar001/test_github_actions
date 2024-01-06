import sys
from app import HelloWorld
import subprocess
import os

def get_file_mapping():
    root_dir = "."
    file_map = dict()

    for dir_, _, files in os.walk(root_dir):
        for file_name in files:
            path = os.path.join(dir_, file_name)
            mapping_path = os.path.relpath(path, root_dir)
            file_map[path] = mapping_path
    return file_map

if __name__ == '__main__':
    
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    print(result.stdout.decode())
    print(get_file_mapping())


    if sys.argv:
        hw = HelloWorld(sys.argv[1])
        print(hw.greet(12))

    