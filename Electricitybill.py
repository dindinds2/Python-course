Unit = int(input("Enter the number unit consume by user: "))
if (Unit < 50):
    amount = Unit * 2.60
    tax = 25
elif (Unit <= 100):
    amount = Unit * 3.25
    tax = 35
elif (Unit <= 200):
    amount = Unit * 5.26
    tax = 45
else:
    amount = Unit * 8.45
    tax = 75
total = amount+tax
print("Electricity bill ",total)