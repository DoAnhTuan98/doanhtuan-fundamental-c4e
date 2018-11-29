from random import randint
n = randint(1,100)

while True:
    a = int(input("Guess my number (1-100)?"))
    if a<n:
        print("too small")
    elif a>n:
        print("A little too large")
    else :
        print("Bingo")
        break