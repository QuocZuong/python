import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. type 'easy' or 'hard': ")
randomNumber = random.randint(1, 100)
life = 0
shouldContinue = True
if mode == 'easy':
    life = 10
else:
    life = 5

while life > 0:
    print(f"You have {life} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == randomNumber:
        print("You win")
        break
    elif guess < randomNumber:
        print("Too low.")
        print("Guess again.")
        life -= 1
    elif guess > randomNumber:
        print("Too high.")
        print("Guess again")
        life -= 1
if life == 0:
    print("You've run out of guesses, you lose.")
