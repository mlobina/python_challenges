def is_empty(my_lst):
    if my_lst:
        print("Not empty")
    else:
        print("Empty")


if __name__ == '__main__':
    lst = [[], [4], [4, 5, 6, 7]]
    for x in lst:
        is_empty(x)