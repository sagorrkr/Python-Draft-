import os

def list_files_recursive(directory_path):
    try:
        print(f"Files in '{directory_path}', (recursive): ")
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                print(os.path.join(root, file))

    except FileNotFoundError:
        print(f"Error: The directory {directory_path} doesn't exist")
    except PermissionError:
        print(f"Error: Permission Denied to access {directory_path}")

directory_path = input("Enter the directory path: ")

list_files_recursive(directory_path)