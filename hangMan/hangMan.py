import random
import art
import word
word = random.choice(word.word_list)
randomWord = word.split(": ")

under = []
live = 6
previousGuess = ""
rightAnswer = 0
print(art.logo)
for i in range(len(randomWord[0])):
    under.append("_")
print("a random word has: ")

while rightAnswer < len(under) and live > 0:
    temp = 0

    for i in range(len(randomWord[0])):
        print(under[i], end=" ")
    guess = input("\nGuess a letter: ").lower()
    if guess == previousGuess:
        live -= 1
        print(f"You've already guesed {guess}")
        continue
    for position in range(len(randomWord[0])):
        if guess == randomWord[0][position]:
            rightAnswer += 1
            under[position] = guess
            temp += 1
            previousGuess = guess
    if temp == 0:
        print(f"You guess {guess}, that's not in the word.")
        print("You lose a life.")
        live -= 1
        print(art.stages[live])
    else:
        print("Nice... Keep going!")
if rightAnswer == len(under):
    for i in range(len(randomWord[0])):
        print(under[i], end=" ")
    print("\nYou win!")
    print(f"{randomWord[0]}: {randomWord[1]}")
else:
    print("You lose!")
    print(f"{randomWord[0]}: {randomWord[1]}")
