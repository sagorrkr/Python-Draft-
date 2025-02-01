name = input("What's your name? ")

file = open("names.txt", "a")   # "w" for writing , "a" for appending
file.write(f"{name}\n")  #file.write(name)
file.close()
