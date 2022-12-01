#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    elements = len(sys.argv) - 1
    for count in range(1, elements + 1):
        sum = sum + int(sys.argv[count])

    print(sum)
