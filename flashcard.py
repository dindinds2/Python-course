class Flashcard:
    def __init__(self, word, meaning):
     self.word = word
     self.meaning = meaning
    def __str__(self):
     return f"{self.word} : {self.meaning}"

flashcards = []

while True:
  word = input("Enter a word (or type 'quit' to stop): ")
  if word.lower() == "quit":
     print("\nYou chose to quit. Displaying all flashcards...\n")
     break
  meaning = input(f"Enter the meaning of '{word}': ")
  card = Flashcard(word, meaning)
  flashcards.append(card)

if flashcards:
  print("📒 All Flashcards:")
  i = 0
  while i < len(flashcards):
   print(flashcards[i])
   i += 1
else:
   print("No flashcards were created.")