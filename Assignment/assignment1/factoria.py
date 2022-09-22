number: int = int(input("Enter number: "))

count = number - 1
while count > 0:
    number *= count
    count -= 1
print("The factorial is:", number)
