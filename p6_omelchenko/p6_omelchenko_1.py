str1 = input("First string ")
str2 = input("Second string ")

str1_letters = set()
str2_letters = set()

str1_letters.add

for i in range(0, len(str1)):
    if(str1[i].isalpha()): str1_letters.add(str1[i].lower()) 

for i in range(0, len(str2)):
    if(str2[i].isalpha()): str2_letters.add(str2[i].lower()) 

print(str1_letters)
print(str2_letters)

if(str2_letters.issubset(str1_letters)): print("It is possible")
else: print("It is not possible")
