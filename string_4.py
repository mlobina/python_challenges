NUM_CHARS = 3

def choose_characters(s: str) -> str:
    if len(s) < NUM_CHARS * 2:
        print("")
    else:
        new_s = "".join([s[:NUM_CHARS], s[-NUM_CHARS::]])
        # new_s = s[:NUM_CHARS] + s[len(s) - NUM_CHARS:]
        print(new_s)


if __name__ == "__main__":
    lst = ['Blue', 'Wonderful', 'Amazing']
    for s in lst:
        choose_characters(s)
