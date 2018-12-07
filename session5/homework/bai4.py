print("Answer the following algebra question:")
p1 = {
    "1": 35,
    "2": 36,
    "3": 40,
    "4": 44,

}
p2 = {
    "1." : "About 55",
    "2." : "About 65",
    "3." : "About 75",
    "4." : "About 85",

}
right_answer = 0
print("If x = 8, then what is the value of 4(x + 3) ?")
for k,v in p1.items():
    print(k,v,sep = ".")
n = int(input("your choice:"))
if n == 4:
    print("bingo")
    right_answer += 1
else:
    print(":(")
print("Estimate this answer (exact calculation not needed):")
print("Jack scored these marks in 5 math tests:49,81,72,66 and 52. What is the mean?")
for k,v in p2.items():
    print(k,v,sep = ".")
m = int(input("your choice:"))
if m == 2:
    print("bingo")
    right_answer += 1
else:
    print(":(")
print("you correctly answer",right_answer,"out of 2 questions")

