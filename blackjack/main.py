# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

import random
import art
print(art.logo)
play = True
while play:

    checkPlay = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if checkPlay == 'n':
        break
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    playerCard = [random.choice(cards), random.choice(cards)]
    computerCard = [random.choice(cards), random.choice(cards)]
    shouldContinue = True

    while shouldContinue:
        playerScore = 0
        computerScore = 0
        for card in playerCard:
            playerScore += int(card)
        for card2 in computerCard:
            computerScore += int(card2)
        print(f"    Your cards: {playerCard}, current score: {playerScore}")
        print(f"    Computer's first card: {computerCard[0]}")
        if playerScore > 21 or computerScore > 21:
            break
        if playerScore == 21 or computerScore == 21:
            print("Blackjacks")
            break
        anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
        if anotherCard == 'n':
            shouldContinue = False
        else:
            cardTemp1 = random.choice(cards)
            if cardTemp1 == 11 and playerScore + int(cardTemp1) > 21:
                cardTemp1 = 1
            cardTemp2 = random.choice(cards)
            if cardTemp2 == 11 and computerScore + int(cardTemp2) > 21:
                cardTemp2 = 1
            playerCard.append(cardTemp2)
            computerCard.append(cardTemp2)
    print(f"    Your final hand: {playerCard}, final score: {playerScore}")
    print(
        f"    Computer final hand: {computerCard}, final score: {computerScore}")

    if playerScore >= 22:
        print("You went over. You lose 😭")
    elif computerScore >= 22:
        print("Computer went over. You win :D")
    elif playerScore < computerScore:
        print("You lose")
    elif playerScore == computerScore:
        print("Draw")
    else:
        print("You win")
