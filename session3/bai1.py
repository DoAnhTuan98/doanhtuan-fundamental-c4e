loop = True
while loop:
    pwd = str(input("nhap password:"))
    if len(pwd) > 8:
        if (not pwd.islower()) and (not pwd.isupper()) and (not pwd.isdigit()): #  ko duoc toan chu hoa va toan chu thuong va toan chu so 
            loop = False
        else:
            print("mat khau toan chu hoa hoac toan chu thuong hoac toan so")
    else:
        print("mk qua ngan")
        
print("ok")

        
       

