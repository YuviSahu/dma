import sys
import math

def pythagoras(a, b):
    aa = math.pow(a, 2)
    bb = math.pow(b, 2)
    cc = aa + bb
    c = math.sqrt(cc)
    return c

def main():
    command = sys.argv[1]

    if command == "add":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x+y)

    if command == "sub":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x-y)

    if command == "times":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x*y)

    if command == "div":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x/y)

    if command == "exp":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x**y)

#    if command == "base":
#        x = int(sys.argv[2])
#        y = int(sys.argv[3])
#
    if command == "countto":
        x = int(sys.argv[2])

        for i in range(x):
            print(i)

    if command == "hypot":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(pythagoras(x, y))
#    for item in ['apples', 'bananas', 'oranges']:
#        print(item)

#    i = 1
#    while i < 4:
#        print(i)
#        i += 1


main()