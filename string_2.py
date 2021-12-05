
def print_character_by_index(s: str, i: int) -> str:
    if not s:
        print("Empty String")
    elif i < len(s):
        print(s[i])
    else:
        print("i is out of range")


if __name__ == "__main__":
    d = {"Hello": 2, "Pizza": 4, "": 3, "World": 15}
    for k, v in d.items():
        print_character_by_index(k, v)