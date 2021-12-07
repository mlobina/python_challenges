import time


# the fastest way
def remove_nth_character(s: str, n: int) -> str:
    start_time = time.time()
    if (len(s) == 0) or (n >= len(s)):
        print(s)
    else:
        print(s.replace(s[n], ""))
    print("--- %s seconds ---" % (time.time() - start_time))


def remove_nth_character_other_way(s: str, n: int) -> str:
    start_time = time.time()
    if (len(s) == 0) or (n >= len(s)):
        print(s)
    else:
        new_s = ""
        for i in range(len(s)):
            if i != n:
                new_s += s[i]
        print(new_s)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    dct = {"Hello": 1, "World": 3, "Dog": 15, "": 2}
    for k, v in dct.items():
        remove_nth_character(k, v)
        remove_nth_character_other_way(k, v)