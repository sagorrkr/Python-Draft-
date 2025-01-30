import sys


if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many argumenrts")
else:
    print("Hello, My name is ", sys.argv[1])



try:
    print("Hello, My name is ", sys.argv[1])
except IndexError:
    print("Too few arguments")