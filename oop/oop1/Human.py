# class Human:
#     name = 'Hadiza'
#
#     def getName(self):
#         return self.name
#
#     def setName(self, name):
#         self.name = name
#
# h1 = Human()
# print(h1.getName())
# print(h1.name)
#
# h1.setName("Racheal")
# print(h1.getName())

class Human:
    def __init__(self, name="", age=0):
        self._name = name
        self._age = age

    # def getName(self):
    #     return self.name
    #
    # def setName(self, name):
    #     self.name = name

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        print("Calling the setter")
        if name.islower():
            raise ValueError("name cannot all be lower case")
        self._name = name

    @age.setter
    def age(self, age: int):
        if age < 0:
            raise ValueError("Age cannot be less than zero")
        self._age = age


h1 = Human()
# print(h1.getName())
# print(h1.name)
print(h1.name)
print(h1.age)
h1.name = "Rachel"
h1.age = 43
print(h1.name)
print(h1.age)
