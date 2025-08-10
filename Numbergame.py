import random
playing = True
number = str(random.randint(10,20))
print("I will genarate number from 0 to 9")
print("the game end when you get 1")
while playing:
    guess = input("Enter your best guess: ")
    if number == guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("The number wasn't queit right , Try again")
        