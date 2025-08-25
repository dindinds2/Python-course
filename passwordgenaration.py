import random

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','S','Y','Z']
alphalow = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','S','Y','Z']
num = ['1','2','3','4','5','6','7','8','9','10']
low = [item.lower() for item in alphalow]
result = random.choice(alpha)
result2 = random.choice(low)
result = random.choice(alpha)
result3 = random.choice(num)
result = random.choice(alpha)
pas = result+result2+result2+result3+result+result
print(pas)