items = ["T-shirt","Sweater"]
n = input("Welcome to our shop, what do you want (C, R, U, D)? ").upper()
if n == "R":
    for index, item in enumerate(items):
        print(index + 1, item,sep=".")
elif n == "C":
    new_items = input("Enter new items:")
    items.append(new_items)
    print(*items,end=",")
elif n == "U":
    a = int(input("Update position:"))
    b = str(input("new items:"))
    items[a] = b
    print(*items,end = ",")
elif n == "D":
    m = int(input("delete position:"))
    
    items.pop(m)
    print(*items,end = ",")


 