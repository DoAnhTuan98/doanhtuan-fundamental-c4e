# person = {}
# print(person)
# print(type(person))
# person = {
#     "name": "H.Duc",
# }
# print(person)
person = {
    "name": "H.Duc", #key : value 
    "city": "Hai Phong", # kieu du lieu cua key la string
    "age": 25 # ben phai kieu du lieu tuy 
}
print(person["name"])
# print("name" in person)

if "status" in person:
    print("yes")
else:
    print("No")