size = [5,7,300,90,24,50,75]
print("Hello, my name is tuan and here is my flock")
print(size)
print("MONTH1 :")
for i in range(3):
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
 print()
 
