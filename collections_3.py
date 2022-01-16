def find_numbers(my_lst):
    if my_lst:
        print(max(my_lst), min(my_lst))
    else:
        print(None)

if __name__ == '__main__':
    lst = [[3, 4, 5, 6], [-1, -2, -3, -4], [0, 0, 0, 0], []]
    for x in lst:
        find_numbers(x)