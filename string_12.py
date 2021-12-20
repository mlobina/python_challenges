from decorator import check_time


@check_time
def check_prefix(s: str, prefix: str) -> bool:
    if len(prefix) > len(s):
        print(False)
    else:
        print(s[:len(prefix)] == prefix)


@check_time
def check_prefix_third_way(s: str, prefix: str) -> bool:
    if len(prefix) > len(s):
        print(False)
    else:
        print(s.startswith(prefix))


if __name__ == "__main__":
    dct = {"Hello": "He", "Coding": "Con", "Nora": "Circum", "Mersy": "mer", "front": "ont"}
    for k, v in dct.items():
        check_prefix(k, v)
        check_prefix_third_way(k, v)