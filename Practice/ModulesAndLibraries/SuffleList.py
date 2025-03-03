#Write a program to shuffle a list of items using the random module.

import os
import random

def list_file_in_directory(directory_path):
    try:
        items = os.listdir(directory_path)

        files = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]

        if files:
            print(f"Files in the {directory_path} :")
            for file in files:
                print(file)
        print(("After suffle:"))
        randomise = random.choices(files, k = len(files))
        for x in randomise:
            print(x)

    except FileNotFoundError:
        print(f"Error: The directory {directory_path} doesn't exist. ")

directory_path = "/Users/sagor/Desktop/Python-Draft-/Practice/ModulesAndLibraries"
list_file_in_directory(directory_path)    