ascii = input("Enter the charecter to check ACSll vallue: ")
if len(ascii) != 1:
    print("Enter one charecter only")
else:
    ascii_val = ord(ascii)
    print (f"The ASCII value of \"{ascii}\"is {ascii_val}")