items = ["com","pho","bun "]
for index , item, in enumerate(items):
    print(index, item)
for i in range(len(items)): #fori
    print(i + 1,items[i], sep = ",")


count = 1
for name in items: #foreach duyet theo noi dung
   print(count,name,sep = ",")
   count += 1
