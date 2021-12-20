from decorator import check_time


@check_time
def replace_char(s: str, curr_char: str, new_char: str) -> str:
    if s.count(curr_char) != 0:
        new_s = s.replace(curr_char, new_char)
        print(new_s)
    else:
        print(s)


@check_time
def replace_char_another_way(s: str, curr_char: str, new_char: str) -> str:
    new_s = ''
    for char in s:
        if char == curr_char:
            new_s += new_char
        else:
            new_s += char
    print(new_s)


if __name__ == '__main__':
    dct = {'Hello': ('l', 's'), 'World': ('W', 'A'), 'Python_1': ('p', 'a'), 'Python': ('P', 'x'), 'Dog': ('D', 'B')}
    for k, v in dct.items():
        print(k, v)
        replace_char(k, v[0], v[1])
        replace_char_another_way(k, v[0], v[1])




