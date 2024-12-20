def is_cymetric(str: str):
    arr = []

    for i in str:
        if i == "(" or i == "{" or i == "[":
            arr.append(i)

        else:
            if len(arr) > 0 and arr[len(arr) - 1] == "(" and i == ")":
                arr.pop()

            if len(arr) > 0 and arr[len(arr) - 1] == "{" and i == "}":
                arr.pop()

            if len(arr) > 0 and arr[len(arr) - 1] == "[" and i == "]":
                arr.pop()

    if len(arr) > 0:
        return False

    return True

def main():
    strs = ["( ){[ 1 ]( 1 + 3 )( ){ }}",
            "( 23 ( 2 - 3);",
            "( 11 }"]

    for i in strs:
        if is_cymetric(i):
            print(f"{i} is cymetric")
        else:
            print(f"{i} is not cymetric")


if __name__ == "__main__":
    main()