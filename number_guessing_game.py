import random as rd

number_to_guess = int(rd.randint(1, 100))
attempts = 0

guess = int(input("Guess a number between 1 and 100: "))
attempts += 1

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1  

    if guess > number_to_guess:
        print("Too high! Try again.")
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts!")
        break








