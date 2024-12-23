def is_cymetric(str: str):
    arr = []

    brackets = { "(": ")", "{": "}", "[": "]" }

    for i in str:
        if i in brackets:
            arr.append(i)

        else:
            last = last_elem(arr)
            if last is not None and brackets[last] == i:
                arr.pop()

    if len(arr) > 0:
        return False

    return True

def last_elem(arr):
    if len(arr) > 0:
        return arr[len(arr) - 1]

    return None

def main():
    strs = ["( ){[ 1 ]( 1 + 3 )( ){ }}",
            "( 23 ( 2 - 3);",
            "( 11 }",
            "{}{}()((([{}])))",
            ")("]

    for i in strs:
        if is_cymetric(i):
            print(f"{i} is cymetric")
        else:
            print(f"{i} is not cymetric")


if __name__ == "__main__":
    main()