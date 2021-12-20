
from decorator import check_time


@check_time
def remove_characters(s: str) -> str:
    if not s or len(s) == 1:
        print(s)
    else:
        new_s = s[1::2]
        print(new_s)


@check_time
def remove_characters_other_way(s: str) -> str:
    new_s = ""
    if len(s) == 1:
        print(s)
    else:
        for i in range(len(s)):
            if i % 2 != 0:
                new_s += s[i]
        print(new_s)


@check_time
def remove_characters_third_way(s: str) -> str:
    new_s = ""
    if len(s) == 1:
        print(s)
    else:
        for i in range(1, len(s), 2):
            new_s += s[i]
        print(new_s)


if __name__ == "__main__":
    lst = ['Coding', 'Pizza', 'Python', 'A', '']
    for s in lst:
        remove_characters(s)
        remove_characters_other_way(s)
        remove_characters_third_way(s)




