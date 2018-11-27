a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

dela = b*b - 4*a*c
if delta < 0:
    print("phuong trinh vo nghiem")
elif delta == 0:
    x = -b/(2*a)
    print("x = ", x)
else:
    print("2 nghiem")
    delta_sqrt = delta**0.5
    x1 = (-b+delta**0,5)/ (2*a)
    x2 = (-b-delta**0.5)/ (2*a)
    print("x1 =", x1)
    print("x2 = ", x2)