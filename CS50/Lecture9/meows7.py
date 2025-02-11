import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help = "number of times to meow")  #python3 meows7.py -h 
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
