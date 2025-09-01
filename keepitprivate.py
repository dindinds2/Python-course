class myclass:
    __privateVar = 52;
    def __privMeth(self):
        print("I am inside my class")
    def hello(self):
        print("Private varible value",myclass.__privateVar)

hi = myclass()
hi.hello()
hi.__privMeth