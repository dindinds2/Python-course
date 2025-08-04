try:
    num1,num2 = eval(input("Enter two number seperated by a comma: "))
    result = num1/num2
    print("Result is",result)
except ZeroDivisionError :
    print("Division by zero is error")
except SyntaxError:
    print("Comma is missing")
except:
    print("Wrong input")
else:
    print("No exception")
finally:
    print("This will excuted no matter what exception is")