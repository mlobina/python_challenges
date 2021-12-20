from decorator import check_time

@check_time
def check_suffix(s: str, suffix: str) -> bool:
    if len(suffix) > len(s):
        print(False)
    else:
        print(s[-len(suffix):] == suffix)


@check_time
def check_suffix_another_way(s: str, suffix: str) -> bool:
    if len(suffix) > len(s):
        print(False)
    else:
        print(s.endswith(suffix))


if __name__ == "__main__":
    dct = {"Hello": "ello", "Coding": "eng", "Nora": "rowing"}
    for k, v in dct.items():
        check_suffix(k, v)
        check_suffix_another_way(k, v)
