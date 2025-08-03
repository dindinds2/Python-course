for x in range(10):
    if x % 20 == 0:
        print("Twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("Fizz")
    elif x % 3 == 0:
        print("Buzz")
    elif x % 2 == 0:
        print("Twothree")
    else:
        print(x)