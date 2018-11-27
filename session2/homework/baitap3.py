n = int(input("can nang cua ban la bao nhieu kg ? "))
r = int(input("chieu cao cua ban la bao nhieu cm ? "))
r = r/100

BMI = n/(r*r)
print("BMI:",BMI)
if BMI < 16 :
    print("giam can nang")
elif BMI < 18.5 :
    print("thieu can")
elif BMI <= 25:
    print("binh thuong")
else:
    print("beo phi")


