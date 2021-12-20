import string
from decorator import check_time


@check_time
def contain_abc(s):
    if s.isalpha:
        new_s = s.replace(' ', '').lower()
        set_s = set(new_s)
        #  if ' ' in set_s:
        #      set_s.remove(' ')
        print(set_s == set(string.ascii_lowercase))
    else:
        print('False')


@check_time
def contain_abc_another_way(s):
    is_pangram = True
    if s.isalpha:
        new_s = s.replace(' ', '').lower()
        for char in string.ascii_lowercase:
            if char not in new_s:
                is_pangram = False
                break # # Stop the loop immediately
        print(is_pangram)
    else:
        print('False')


if __name__ == '__main__':
    lst = ['abcdefghijklmnopqrstuvwxyz', 'The quick brown fox jumps over the lazy dog', 'Hello', '1 AD sddd']
    for x in lst:
        print(x)
        contain_abc(x)
        contain_abc_another_way(x)

