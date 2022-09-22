import  random
lst = list(range(1, 11))
print(lst)

# random.shuffle(lst)
# print(lst)

# lst.append(28)
# print(lst)

# lst.append([3,5,7])
# print(lst)

# lst.extend([3,5,7])
# print(lst)

lst.insert(0, 56)
print(lst)

lst.insert(-1, 68)
print(lst)

last_item = lst.pop()
print(last_item)
print(lst)

item_at_index = lst.pop(0)
print(lst)

lst.remove(6)
print(lst)

lst.clear()
print(lst)