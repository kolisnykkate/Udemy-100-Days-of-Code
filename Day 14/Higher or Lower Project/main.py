# TODO-1 import and print logos (last one)
# TODO-2.1 import game data, random
# ~~ TODO-2.2 randomly choose A and B
# ~~ TODO-2.3 compile and print info Compare A, Against B
# ~~TODO-3 input Who has more followers? Type 'A' or 'B':
# ~x TODO-4.1 define number of followers
# ~~TODO-4.2 compare number of followers A and B
# ~~TODO-5 if: no --> exit (break, flag)
# ~~TODO-6.1 if: yes --> right choice becomes A
# ~~TODO-6.2 calc current score
# ~~TODO-6.3 print("You're right! Current score: ")
# TODO-7 start the while loop over

from game_data import data
import random
import art


def compare_followers(a, b):
    """Compare followers of a and b, return True, if a > b or False"""
    return a['follower_count'] > b['follower_count']

print(art.logo)
opt_a = random.choice(data)
score = 0
while True:
    opt_b = random.choice(data)
    if opt_a == opt_b:
        opt_b = random.choice(data)

    print(f"Compare A: {opt_a['name']}, a {opt_a['description']}, from {opt_a['country']}")
    print(art.vs)
    print(f"Against B: {opt_b['name']}, a {opt_b['description']}, from {opt_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(art.logo)

    if guess == "a" and compare_followers(opt_a, opt_b):
        score += 1
        print(f"You got it! The score is {score}")


    elif guess == "b" and not compare_followers(opt_a, opt_b):
        score += 1
        print(f"You got it! The score is {score}")
        opt_a = opt_b

    else :
        print(f"Sorry, that's wrong. Final score: {score}")
        break