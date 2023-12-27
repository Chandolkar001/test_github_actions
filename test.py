import sys

name = "world"

if sys.argv[1] != '0':
    name = str(sys.argv[1])

print(f"hello {name}")