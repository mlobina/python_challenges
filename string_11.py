def print_without_spaces(s):
    new_s = s.replace(' ', '')
    print(new_s)


if __name__ == '__main__':
    lst = ['Hello, World!', 'Have a great day', 'Hello', '1 AD sddd']
    for x in lst:
        print(x)
        print_without_spaces(x)
