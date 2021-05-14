import random

answer = random.randint(1, 100)
attempts = 0
is_game_over = False

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Invalid option.")

while is_game_over == False:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > answer:
        attempts -= 1
        print("Too high.")
    elif guess < answer:
        attempts -= 1
        print("Too low.")
    elif guess == answer:
        print(f"You got it! The answer was {answer}.")
        is_game_over = True
    else:
        print("Invalid guess. Not a number")

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        is_game_over = True





