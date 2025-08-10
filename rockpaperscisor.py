import random
option = ["Rock","Paper","Scissor"]
user_choice = input("Chose Rock Paper or Scissor")
computer_choice = random.choice(option)
print("You chose",user_choice)
print("Computer chose",computer_choice)
if user_choice == computer_choice:
    print("its a tie")
elif user_choice == "Rock" and computer_choice == "Scissor":
    print("Rock smashes Scissor , you win")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper cover Rock , you win")
elif user_choice == "Scissor" and computer_choice == "Paper":
    print("Scissor cut Paper , you win")
else:
    print("You lose")