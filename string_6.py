
def contains_numbers(s: str) -> str:
    print(s.isdigit())


def contains_numbers_other_way(s: str) -> str:
    print(s.isdecimal())


if __name__ == "__main__":
    lst = ["Hello", "4567", "Hello59", ""]
    for s in lst:
        contains_numbers(s)
        contains_numbers_other_way(s)
