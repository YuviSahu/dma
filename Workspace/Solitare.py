import random

board = [["", "", "", "", "", "", ""],
         ["", "", "", "", "", ""],
         ["", "", "", "", ""],
         ["", "", "", ""],
         ["", "", ""],
         ["", ""],
         [""]]
usedCards = []
numCards = 7
repeated = True
for r in range(7):
    for c in range(numCards):
        repeated = True
        while repeated == True:
            xx = ""
            x = random.randint(1, 13)
            if x == 1:
                xx = "A"
            elif x == 11:
                xx = "J"
            elif x == 12:
                xx = "Q"
            elif x == 13:
                xx = "K"
            else:
                xx = str(x)
            suite = random.randint(1, 4)
            if suite == 1:
                suite = "S"
            elif suite == 2:
                suite = "H"
            elif suite == 3:
                suite = "C"
            elif suite == 4:
                suite = "D"
            board[r][c] = xx
            for i in usedCards:
                if xx == usedCards[i]:
                    break
                else:
                    repeated = False
    numCards -= 1


def print_board():
    numCards = 7
    for r in range(7):
        for c in range(numCards):
            print(board[r][c] + "  ", end="")
        numCards -= 1
        print("")


print_board()

print("Hello")
