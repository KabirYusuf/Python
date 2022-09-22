
# cont = [num * num for num in range(1, 11)]
# print(cont)
#
# names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Racheal']
# my_name = [name for name in names if name.istitle()]
# input_names = [input(f"{i + 1} Name? ") for i in range(5)]
#
#
# even = [num for num in range(1, 11) if num % 2 == 0]
# print(even)
# print(my_name)
# print(input_names)
x_and_y = [(x,y) for x in range(1,6) for y in range(1,6)]
print(x_and_y)

listcomp = [num % 3 for num in range(1, 10)]
setcomp = {num % 3 for num in range(1, 10)}
dictcomp = {k:v for k, v in enumerate(range(11, 16))}
genex = (num for num in range(1, 6))

print (type(listcomp), listcomp)
print (type(setcomp), setcomp)
print (type(dictcomp), dictcomp)
print (type(genex), genex)
