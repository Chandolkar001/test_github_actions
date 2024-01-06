import sys
from app import HelloWorld

if __name__ == '__main__':
    if sys.argv:
        hw = HelloWorld(sys.argv[1])
        print(hw.greet(12))

    