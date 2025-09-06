
import random
class FruitQuiz:
  def __init__(self):
   self.fruits = {

   "apple": "red",

   "banana": "yellow",

   "grape": "purple",

   "orange": "orange",

   "mango": "yellow",

   "watermelon": "green"

}

  def start_quiz(self):
   fruit = random.choice(list(self.fruits.keys()))
   print(f"What is the colour of {fruit}?")
   answer = input("Your answer: ").lower()

   if answer == self.fruits[fruit]:
    print("✅ Correct! Well done.")
   else:
    print(f"❌ Wrong! The correct answer is {self.fruits[fruit]}.")

quiz = FruitQuiz()

quiz.start_quiz()