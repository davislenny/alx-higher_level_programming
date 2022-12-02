#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    elements = len(sys.argv) - 1
    if elements == 0:
        print("0 arguments.")
    elif elements == 1:
        print("1 argument:")
    else:
        print(f"{elements} arguments:")

    for count in range(1, elements + 1):
        print(f"{count}: {sys.argv[count]}")
