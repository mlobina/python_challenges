def reverse_word(s: str) -> str:
    if all(i.isalpha() or i.isspace() for i in s):
        new_s = "".join(reversed(s)).swapcase()
        print(new_s)
    else:
        print('bad')


if __name__ == '__main__':
    lst = ['Hello World', 'Python is Awesome', '']
    for x in lst:
        print(x)
        reverse_word(x)