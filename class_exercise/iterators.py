lst = [1, 2, 3, 4, 5]
# it = iter(lst)
# print(next(it))
# print(next(it))
# print(list(it))


def custom_for(iterable, func):
    ite = iter(iterable)

    while True:
        try:
            func(next(ite))
            # print(next(ite))

        except StopIteration:
            print("End of loop")
            return


custom_for(lst, print)
