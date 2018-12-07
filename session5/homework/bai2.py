price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,

}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
for k in price:
    print(k)
    print("price:",price[k])
    for x in stock:
     if k == x:
         print("stock:",stock[x])

         money = price[k] * stock[x]
         total += money
print(total)

        


    