class word:
    def __init__(self,w=""):
        self.w = w

    def reverse(self):
        return self.w[::-1]


ask = input("Enter the word: ")
obj = word(ask)
print(obj.reverse())