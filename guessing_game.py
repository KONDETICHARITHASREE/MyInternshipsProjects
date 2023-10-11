import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print(f"Guess the secret number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break


if attempts == max_attempts:
    print(f"Game over! The secret number was {secret_number}. Try again!")