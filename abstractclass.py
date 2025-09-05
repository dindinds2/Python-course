from abc import ABC,abstractmethod
class abcclass(ABC):
    def print(self,x):
        print("Pass value",x)
    @abstractmethod
    def task(self):
        print("We are inside abcclass")

class test_class(abcclass):
    def task(self):
        print("We are in side test class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)