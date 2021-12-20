def replace_commas_by_dots(s: str) -> str:
    if s.count(','):
        new_s = s.replace(',', '.')
        print(new_s)
    else:
        print(s)


if __name__ == '__main__':
    lst = ['Hello, World!', '3,456,344']
    for x in lst:
        print(x)
        replace_commas_by_dots(x)
