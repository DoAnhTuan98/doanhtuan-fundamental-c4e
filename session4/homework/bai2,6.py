size = [5,7,300,90,24,50,75]
print("Hello, my name is tuan and here is my flock")
print(size)
print()
print("Now my biggest sheep has size ",max(size),end = " ")
print("let's shear it")
print("After shearing, here is my flock")
a = size.index(max(size))
size[a] = 8
print(size)
print()
print("MONTH1 :")
for i in range(2):
 a = 0
 for i in range(len(size)):
    
    size[a] = size[a] + 50
    a += 1
 print("One month has passed, now here is my flock")
 print(size)
 print("Now my biggest sheep has size",max(size),end = " ")
 print("let's shear it")
 print("Ater shearing, here is my flock")
 b = size.index(max(size))
 
 size[b] = 8
 print(size)
print("MONTH3:")
print("Now month has passed, now here is my flock")
b = 0
for i in range(len(size)):
 size[b] = size[b] + 50
 b += 1
print(size)
print("My flock has size in total:",sum(size))
print("I wold get :",sum(size)*2,"$")






