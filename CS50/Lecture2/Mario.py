def main():
    print_column(3)
    print_row(4)
    print_squre(3)

def print_column(height):
    print("# \n" * height, end = "")

def print_row(width):
    print("?" * width)

def print_squre(size):
    #for each row in squre
    for i in range(size):
        #for each brick in row
        for j in range(size):
            print("#", end = "")
            
        print()
    
main()

 