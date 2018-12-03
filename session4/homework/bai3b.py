from random import randint

a = ["champion","meticulous","hexagon"]

b = randint(0,len(a)-1)
c = list(a[b])
for i in range(len(c)):
     d = randint(0,len(c)-1)
     print(c[d],end = " ")
     c.pop(d)
print() 
n = str(input("du doan:"))
if n == a[b]:
    print("Hura")
else:
    print(":(")

