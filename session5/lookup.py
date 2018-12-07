tudien = {
    "name" : "ten",
    "city" : "thanh pho",
    "age" : "tuoi",
    "work" : "lam viec",

}
while True:
 print(*tudien)
 a = str(input("your code:"))
 if a in tudien:
  print(tudien[a])
  update = input("Do you want to update(Y/N)?").upper()

  if update == "Y":
    new_translation = str(input("yous translation:"))
    tudien[a] = new_translation
    print(tudien)
    print("done")
  else:
    print("Not fount")
    m = input("Do you want to contribute(Y/N)?").upper()
    if m == "y":
     b = input("Your translation:")
     tudien[a] = b
     print("Done")
 





