def convert_str(s: str) -> str:
    new_s = ''
    for word in s.split(' '):
        new_s += (''.join(sorted(word.lower())) + ' ')
    new_s.rstrip()
    print(new_s)


if __name__ == '__main__':
    lst = ['Hello World', 'Wonderful World']
    for x in lst:
        print(x)
        convert_str(x)