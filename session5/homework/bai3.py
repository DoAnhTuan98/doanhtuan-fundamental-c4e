result = [35,36,40,44]
print("Answer the following algebra question:")

print("If x = 8, then what is the value of 4(x + 3) ?")
a= 4*(8+3)

for index, item in enumerate(result):
    print(index +1, item,sep = "." )
while True:
    n = int(input("Your choice:"))
    if n == 4:
        print("Bingo")
        break
    else:
        print(":(")
