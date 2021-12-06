def reverse(s: str) -> str:
    print(s[::-1])


def reverse_other_way(s: str) -> str:
    print("".join(reversed(s)))


if __name__ == "__main__":
    lst = ["", "Hello", "Wo"]
    for s in lst:
        reverse(s)
        reverse_other_way(s)