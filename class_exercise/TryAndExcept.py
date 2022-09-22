def add(a: float, b: float) -> float | None:
    try:
        lst = [1,2,3]
        # lst[6]
        # file = open('file.txt', mode= 'r', encoding= 'utf-8')
        # print(file.read())
        # print("About to close")

        return a / b

    except (TypeError, ZeroDivisionError, NameError):
        print("Type error")


print(add(1, 0))
