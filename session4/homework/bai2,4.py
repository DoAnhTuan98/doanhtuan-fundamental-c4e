size = [5,7,300,90,24,50,75]
print("Hello, my name is tuan and here is my flock")
print(size)
print("Now my biggest sheep has size ",max(size),end = " ")
print("let's shear it")
a = size.index(max(size))
size[a] = 8

print("After shearing, here is my flock")
print(size)
b = 0
for i in range(len(size)):
    size[b]= size[b] + 50
    b += 1
print("One month has passed, now here is my flock")
print(size)



