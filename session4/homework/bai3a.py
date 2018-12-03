from random import randint
m = "champion"
a = list(m)
print(a)
for i in range(len(a)):
     x = randint(0,len(a)-1)
     print(m[x],end = " ")
     a.pop(x)
print()
c = str(input("du doan:"))
if c == m:
    print("Hura")
else :
    print(":(")

