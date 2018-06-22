import random

youBusted = False
IBusted = False

originalCardInt = random.randint(1, 13)
if originalCardInt == 1:
    originalCardStr = "A"
elif originalCardInt == 11:
    originalCardStr = "J"
elif originalCardInt == 12:
    originalCardStr = "Q"
elif originalCardInt == 13:
    originalCardStr = "K"
else:
    originalCardStr = str(originalCardInt)

print("Your first card is " + originalCardStr)

total = originalCardInt
while True:
    wantsAnotherCard = input("Do you want another card? ")
    if wantsAnotherCard == "Yes" or wantsAnotherCard == "yes":
        newCard = random.randint(1, 13)
        cardInt = newCard
        cardStr = str(newCard)
        if  newCard== 1:
            cardStr = "A"
        if newCard == 11:
            cardStr = "J"
        if newCard == 12:
            cardStr = "Q"
        if newCard == 13:
            cardStr = "K"
        total = total + cardInt
        print("Your card was a " + str(cardStr))
        print("Your total is " + str(total))
        if total > 21:
            print("Busted")
            youBusted = True
            break

    elif wantsAnotherCard == "No" or wantsAnotherCard == "no":
        print("Okay. My turn.")
        break

    else:
        print("This is a yes or no question")


myOriginalCardInt = random.randint(1, 13)
if myOriginalCardInt == 1:
    myOriginalCardStr = "A"
elif myOriginalCardInt == 11:
    myOriginalCardStr = "J"
elif myOriginalCardInt == 12:
    myOriginalCardStr = "Q"
elif myOriginalCardInt == 13:
    myOriginalCardStr = "K"
else:
    myOriginalCardStr = str(myOriginalCardInt)

print("My first card is " + myOriginalCardStr)
myTotal = myOriginalCardInt

while True:
    if IBusted == False:
        print("Thinking...")
        counter = 0
        for i in range(1, 30000000):
            counter += 1
    if (21-myTotal)/13 > 5/13 and IBusted == False:
        print("I want another card.")
        newCard = random.randint(1, 13)
        cardInt = newCard
        cardStr = str(newCard)
        if newCard == 1:
            cardStr = "A"
        if newCard == 11:
            cardStr = "J"
        if newCard == 12:
            cardStr = "Q"
        if newCard == 13:
            cardStr = "K"
        myTotal = myTotal + cardInt
        print("My card was a " + str(cardStr))
        print("My total is " + str(myTotal))
        if myTotal > 21:
            print("I'm Busted")
            IBusted = True

    elif IBusted == True or not ((21-myTotal)/13 > 5/13):
        if IBusted == False:
            print("I don't want another card")
        if IBusted == True and youBusted == True:
            print("We both got busted")
            break
        if IBusted == True and youBusted == False:
            print("You won")
            break
        if IBusted == False and youBusted == True:
            print("I win")
            break
        if total > myTotal:
            print("You win")
            break
        if total < myTotal:
            print("I win")
            break
        if myTotal == total:
            print("We tied")
            break