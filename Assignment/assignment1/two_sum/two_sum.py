def two_sum(lst, target):
    result_lst = [-1, -1]
    for i in range(0, len(lst), 1):
        for j in range(i + 1, len(lst), 1):
            if lst[i] + lst[j] == target:
                result_lst[0] = i
                result_lst[1] = j
                return result_lst

    print(result_lst)
    return [-1, -1]



my_list = [3, -1, 5, 4]
print(two_sum(my_list, 3))
