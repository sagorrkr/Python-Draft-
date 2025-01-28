"""
> 
>= 
<
<=
==
!=
"""

x = int(input("what's the value of X? "))
y = int(input("what's the value of Y? "))

if x < y:
    print("X is less than Y")
elif x > y:
    print("X is Greater than Y")
elif x == y:
    print("X is equal Y")
else:
    print("Invalid!") #we will never reach to this case!

a = int(input("what's the value of A? "))
b = int(input("what's the value of B? "))


if a > b or a < b: # a != b
    print(" A is not equal to B")
else:
    print("A is equal to B")
