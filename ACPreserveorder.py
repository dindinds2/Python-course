number = input("Enter the number: ")
count = 0
for char in number:
    if char.isdigit():
        count += 1
print("Total digit",count)