import math


# class MyDict(dict):
#     def __setitem__(self, key, value):
#         if type(key) != str:
#             raise TypeError("Can Only accepts string as a key")
#         super().__setitem__(key, value)

# def __getitem__(self, item):
#     if not isinstance(item, str):
#         raise TypeError("Can Only accepts string as a key")
#     return super(MyDict, self).__getitem__(item)


# diction = MyDict()
# diction["key"] = "value"
# print(diction["key"])


# diction[3] = 3
# print(diction["val"])

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}i + {self.y}j"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 1

    def __bool__(self):
        return True

    def __lt__(self, other):
        return abs(self) < abs(other)


v1 = Vector(2, 4)
v2 = Vector(1, 6)
v3 = v1 + v2
print(bool(v1))
print(v3)
if v1:
    print(v1)
