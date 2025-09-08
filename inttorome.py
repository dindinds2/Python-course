class NumberToRome:
    def __init__(self, number):
        self.number = number

    def convert(self):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rome = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        num = self.number
        romenum = ""
        i = 0

        while num > 0:
            for _ in range(num // val[i]):   
                romenum += rome[i]           
                num -= val[i]
            i += 1
        return romenum


ask = int(input("Enter an integer: "))
obj = NumberToRome(ask)
print("Roman number:", obj.convert())
