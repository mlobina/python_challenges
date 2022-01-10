def count_repeat(s: str):
    repeated_count = 0
    repeated_chars = []
    for char in s:
        if (s.count(char) > 1) and (char not in repeated_chars) :
            repeated_count += 1
            repeated_chars.append(char)
    print(repeated_count)

    if repeated_count:
        print(*sorted(repeated_chars), sep=" ")
    else:
        print(None)


if __name__ == '__main__':
    lst = ['Hello', 'Corporation', 'Python']
    for x in lst:
        print(x)
        count_repeat(x)

