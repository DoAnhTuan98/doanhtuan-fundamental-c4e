

items = ["com","pho","bun"]
while True:
 cmd = input("what do youn want (C,R,U,D,E)?").upper()
 if cmd == "C":
    n = str(input("ban muon them gi:"))
    items.append(n)
    print(items)
 elif cmd == "R":
    for index, item in enumerate(items):
        print(index + 1, item,sep=".")

 elif cmd == "U":
    d = int(input("vi tri can sua:"))
    c = str(input("noi dung can sua:"))
    items[d] = c
    print(items)

    



 elif cmd == "D" :
    a = int(input("xoa theo vi tri:"))
    items.pop(a)
    print(items)
 elif cmd == "E":
    break
    


    



