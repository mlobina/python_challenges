from decorator import check_time


@check_time
def multiply(start: list, factor: int) -> list:
    final = []
    for i in start:
        i = i * int(factor)
        final.append(i)
    print(final)


@check_time
def multiply_in_other_way(my_list: list, factor: int) -> list:
    for i, elem in enumerate(my_list):
        my_list[i] = elem * factor
    print(my_list)


if __name__ == '__main__':
    dct = {2: [3, 4, 5, 6], 3: ['a', 'b', 'c']}
    for x, y in dct.items():
        multiply(y, x)
        multiply_in_other_way(y, x)


