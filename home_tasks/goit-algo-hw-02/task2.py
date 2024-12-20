from collections import deque

def define_palindrome(str: str):
    d = deque()

    for i in str:
        if i.isspace() or i == '.' or i == ',' or i == "'":
            continue

        d.append(i.lower())

    while len(d) > 1:
        a = d.popleft()
        b = d.pop()

        if a != b:
            return False

    return True


def main():
    strs = ["mam",
            "mama",
            "maam",
            "Drab as a fool, aloof as a bard",
            "araara",
            "A butt tuba",
            "ad",
            "dfgdfbfbnfgn",
            "Liam Stakes Edna's, Adam's, Otto's, Mada's and Esekat's mail.",
            "A car, a man, a maraca"]

    for i in strs:
        if define_palindrome(i):
            print(f"{i} is palindrome")
        else:
            print(f"{i} is not palindrome")


if __name__ == "__main__":
    main()