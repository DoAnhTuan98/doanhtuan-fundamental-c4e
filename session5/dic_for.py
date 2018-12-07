person = {
    "name" : "H Duc",
    "age" :  25,
    "city" : "Hanoi",
    "books" :["Sapiens","Tieu ngao giang ho","tam quoc"]
}

print(person["name"])
print(person["books"])
books = person["books"]
print(books)
for b in books:
    print(b)
print()



print(books[-1])
print(person["books"][1])
print()


for x in person:
     print(x)
print()


for v in person.values(): 
    print(v)
print()

for k,v in person.items():
        print(k,v)



