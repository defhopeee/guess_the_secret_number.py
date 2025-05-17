# guess_the_secret_number.py
import random

secret_number = random.randint(1, 100)
print("Welcome to the Secret Number Guessing Game!")

attempts = 0

while True:
    guess = input("Enter your guess (1-100): ")
    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the secret number in", attempts, "attempts.")
        break
