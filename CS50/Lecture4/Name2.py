import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: #to indicate from second to the last index, we might use [1:-1]
    print("Hello, My name is ", arg)