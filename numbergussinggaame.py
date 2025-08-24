import random
def number_guessing_game():
    number = random.randint(1,5)
    attempts = 0
    print("Welcome to number guessing game")
    print("Guess a number between 1 and 100")
    while True:
        try:
            guess = int(input("Enter your guess"))
            attempts += 1
            if guess < number:
                print("Too low try again")
            elif guess > number:
                print("Too high try again")
            else:
                print(f"congratulation you guessed it in{attempts}attempts")
                break
        except ValueError:
            print("Please enter the valid number")
number_guessing_game()