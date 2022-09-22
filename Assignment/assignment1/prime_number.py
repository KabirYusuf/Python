number: int = int(input("Enter Number: "))
added_number = 0
for i in range(number, 0, -1):
    if number % i == 0:
        added_number += 1
if added_number == 2:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

