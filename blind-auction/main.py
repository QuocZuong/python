import art
print(art.logo)


def addPeople(name, bid, dictionary):
    dictionary[name] = bid


should_continue = True
print("Welcome to the secret auction program.")
dictionary = {}
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    check = input("Are there any ohter bidders? Type 'yes' or 'no'.\n")
    dictionary[name] = bid
    if check == "no":
        should_continue = False
max = 0
for person in dictionary:
    if max < dictionary[person]:
        max = dictionary[person]
        winnerName = person
        winnerBid = dictionary[person]
print(f"The winner is {winnerName} with a bid of ${winnerBid}.")
