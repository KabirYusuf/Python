def decorate(func):
    def wrap():
        print("I am before decorate")
        print(func())
        print("i am after decorator")

    return wrap


# using decorators

# @decorate
def hello():
    return "hello world"


# or

hello = decorate(hello)

hello()


def decorate_with_param(func):
    def wrap_dec(arg):
        print("I am before decorate")
        print(func(arg))
        print("i am after decorator")

    return wrap_dec


# using decorators

# @decorate
def hello_dec(name):
    return f"hello{name}"


# or

hello_dec = decorate_with_param(hello_dec)

hello_dec("name")
