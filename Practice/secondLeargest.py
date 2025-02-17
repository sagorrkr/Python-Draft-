numbers = list(map(int, input("Enter numbres separated by space: ").split()))
numbers = list(set(numbers))
numbers.sort(reverse= True)
print(numbers[1])