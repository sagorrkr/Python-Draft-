#pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, I am " +  sys.argv[1])