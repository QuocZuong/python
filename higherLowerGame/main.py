import art
import game_data
import random
print(art.logo)
should_continue = True
mark = 0
compare_a = random.choice(game_data.data)
compare_b = random.choice(game_data.data)
while should_continue:
    if compare_a == compare_b:
        compare_b = random.choice(game_data.data)
    if (game_data.data == ''):
        print("You win this game!")
        break
    print(
        f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}")
    print(art.vs)
    print(
        f"Compare B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}")
    print(compare_a['follower_count'])
    print(compare_b['follower_count'])
    print("\n\n")
    chose = input("Who has more follower? Type 'A' or 'B': ")
    if (((chose == 'A' or chose == 'a') and compare_a['follower_count'] >= compare_b['follower_count'])) or (((chose == 'b' or chose == 'B') and compare_a['follower_count'] <= compare_b['follower_count'])):
        mark += 1
        print(f"You are right! Current score: {mark}")

    else:
        print("Sorry, that's wrong. ", end=" ")
        should_continue = False
    compare_a = compare_b
    compare_b = random.choice(game_data.data)
print(f"Final score: {mark}")

