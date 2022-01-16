
def print_in_line(my_list: list) -> str:
    my_str = ''
    for i, elem in enumerate(my_list):
        my_str += (str(my_list[i]) + ' ')
    my_str.rstrip()
    print(my_str)


def print_in_line_in_other_way(my_list: list) -> str:
    for elem in my_list:
        print(elem, end=' ')


def print_in_line_in_new_other_way(my_list: list) -> str:
    print(*my_list, sep=' ')


if __name__ == '__main__':
    lst = [[3, 4, 5, 6], ['a', 'b', 'c']]
    for x in lst:
        print_in_line_in_new_other_way(x)