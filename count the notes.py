Amount = int(input("Amount to withdraw: "))
note_1 = Amount // 100
note_2 = (Amount % 100)// 50
note_3 = ((Amount % 100)%50)//10
print(note_1)
print(note_2)
print(note_3)