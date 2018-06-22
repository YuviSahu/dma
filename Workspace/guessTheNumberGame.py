import random

while True:

    y = int(input("The range is 0 to "))
    print()

    x = random.randint(0, y)

    while True:
        z = int(input("What's your guess? "))
        print()
        if z == x:
            print("Correct!")
            print()
            break
        elif z < x:
            print("More")
            print()
        elif z > x:
            print("Less")
            print()