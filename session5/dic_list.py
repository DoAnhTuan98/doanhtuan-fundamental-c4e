p1 = {
    "name" : "H Duc",
    "age" : 25,
    "city" : "Hai Phong",
}

p2 = {
    "name" : "Huong",
    "age" : 26,
    "city" : "hai duong",

}
p3 = {
    "name" : "long",
    "age" : 19,
    "city " : "hanoi"
}

p_list = [
   {
    "name" : "H Duc",
    "age" : 25,
    "city" : "Hai Phong",
   },
   {
    "name" : "Huong",
    "age" : 26,
    "city" : "hai duong",

   },
   {
    "name" : "long",
    "age" : 19,
    "city " : "hanoi"
   },
]
# print(p_list)
# p = p_list[0]
# print(p)
# print(p["name"])
# print(p["age"])


for p in p_list:
    
    print(p["name"])
    print(p["age"])
