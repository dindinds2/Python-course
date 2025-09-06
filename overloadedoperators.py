class a:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if (self.a < other.a):
            return "ob 1 is less then ob2"
        else:
            return "ob2 is less then ob1"
    def __eq__(self,other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Both are mot equal"

ob1 = a(2)
ob2 = a(3)
print("Pass value",ob1.a,ob2.a)
print(ob1 < ob2)
print(ob1 == ob2)