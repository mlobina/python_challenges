
import time


# the fastest way
def remove_characters(s: str) -> str:
    start_time = time.time()
    if not s or len(s) == 1:
        print(s)
    else:
        new_s = s[1::2]
        print(new_s)
    print("--- %s seconds ---" % (time.time() - start_time))


def remove_characters_other_way(s: str) -> str:
    start_time = time.time()
    new_s = ""
    if len(s) == 1:
        print(s)
    else:
        for i in range(len(s)):
            if i % 2 != 0:
                new_s += s[i]
        print(new_s)
    print("--- %s seconds ---" % (time.time() - start_time))

def remove_characters_third_way(s: str) -> str:
    start_time = time.time()
    new_s = ""
    if len(s) == 1:
        print(s)
    else:
        for i in range(1, len(s), 2):
            new_s += s[i]
        print(new_s)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    lst = ['Coding', 'Pizza', 'Python', 'A', '']
    for s in lst:
        remove_characters(s)
        remove_characters_other_way(s)
        remove_characters_third_way(s)




