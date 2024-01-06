import sys
from app import HelloWorld
import subprocess

if __name__ == '__main__':
    
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    print(result.stdout.decode())

    if sys.argv:
        hw = HelloWorld(sys.argv[1])
        print(hw.greet(12))

    