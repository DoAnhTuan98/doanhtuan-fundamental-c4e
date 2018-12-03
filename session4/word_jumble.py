from random import randint
word = "hexagon"
characters = list(word) # (chuyen doi thanh list)
print(word)
print(characters)

for i in range(len(characters)):
  a = (randint(0,len(characters)-1))

  print(characters[a],end=" ")
  characters.pop(a)
print()
n = str(input("du doan :"))

if n == "word":
     print("Hura")
else:
    print(":(")
  
