from art import logo
import random

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

def check_answer(guess, secret_number, number_of_guesses):
    if guess == secret_number:
        print(f"You got it! The number was {secret_number}")
    elif guess > secret_number:
        print("Too high.")
        return number_of_guesses-1
    elif guess < secret_number:
        print("Too low.")
        return number_of_guesses-1

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS



def game():
    print(logo)
    print("Welcome to the Number Guessing Game!"
          "I am thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)

    number_of_guesses = set_difficulty()

    guess = None
    while guess != secret_number:
        guess = int(input("Guess a number: "))
        number_of_guesses = check_answer(guess, secret_number, number_of_guesses)
        if guess == secret_number:
            break
        if number_of_guesses == 0:
            print("You run out of guesses!")
            break
        print(f"You have {number_of_guesses} attempts left")

game()


