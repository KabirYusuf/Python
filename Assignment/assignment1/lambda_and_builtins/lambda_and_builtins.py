# def add(a: int, b: int) -> int:
#     """Adds two number"""
#
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
# print(add.__annotations__)
#
#
# def operates(x, y, func):
#     return func(x, y)

#
# print(operates(2, 3, add))
#
#
# def sub(x, y):
#     return y - x
#
#
# print(operates(5, 8, sub()))
#
#
# def multiply(a):
#     def by(b):
#         return a * b
#
#     return by
#
#
# multiply_by_five = multiply(5)
#
# print(multiply_by_five(6))
#
# adder = lambda a, b: a + b
# print(adder.__name__)
#
# print (adder(10, 9))
# print(operates(2, 3, adder))
# print(operates(2, 3, lambda a, b: a + b))
#
#
# print(abs(-1))
#
# print(round(56.38906, 2))
# print(round(56.38906, -2))
# print(round(56.38906, -3))
#
# letters = [['a'], ['b'], ['c'], ['d']]
# print(sum(letters, []))
#
# print(max(1,2,3,4,5,6,7))
#
# fruits = "apple pear cucumber mango grape water_melon".split()
# print(max(fruits)) #water_melon because in lexicographical order, w has the highest
#
# print (min (fruits, key= len)) # key is the factor(takes a function) that is used to determine the min of fruit, i.e using len in this case, it can be used for both maximum and minimum
#
# print(max(fruits, key=lambda  x: x[-1]))
#
#
# lst= [1,2,3,4,5]
# print(list (map(lambda  x: x ** 2, lst)))
# print([x ** 2 for x in lst])
# print(list(map(str.upper, fruits))) #upper is a function that is not been called i.e not written as  upper.()
# print(list(map(lambda  x: x.upper(), fruits)))
# fruits.append('Agbado')
# print(list(map(str.istitle, fruits)))
# print(list(map(lambda y: y.upper(),filter(lambda x: not x.istitle(), fruits))))
# print([x.upper() for x in fruits if not x.istitle()])
from functools import reduce

lst = [1, 2, 3, 4, 5]


def reduce_func(acc, item):
    print(f"acc -> {acc} <> item -> {item}")
    return acc + item


# print("\n################# Reduce ################\n")
# print(lst)
# print(reduce(reduce_func, lst, 100))

# using sum
print(sum(lst, 100))
print(reduce(lambda acc, item: acc if acc > item else item, lst))
print(max(lst))
