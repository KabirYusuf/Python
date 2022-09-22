words: str = str(input("Enter words: "))
count = 1

for element in range(0, len(words)):
    if words[element].isupper():
        count += 1
print("We have ", count, "words")
