class computer:
    def __init__(self):
        self.__maxprice = 2000
    def sell(self):
        print("selling price{}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice = price

c = computer()
c.sell()
c.__maxprice = 2200
c.sell()
c.setmaxprice(2200)
c.sell()