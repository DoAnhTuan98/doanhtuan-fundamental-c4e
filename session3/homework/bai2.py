
while True:
    n = int(input("Guess my number (1-100)?"))
    if n <= 50:
        print("too small")
    elif n > 51:
        print("A little too large")
    elif n == 51:
        print("Bingo")
        break