import math

print("Input degree: ")
a=int(input())
print(f"Output radian: {math.radians(a)}")

print("Height: ")
h=int(input())
print("Base, first value: ")
fv=int(input())
print("Base, second value: ")
sv=int(input())
print(f"Expected Output: {0.5*(fv+sv)*h}")

print("Input number of sides: ")
ns=int(input())
print("Input the length of a side: ")
l=int(input())
print(f"The area of the polygon is {(l*l*ns)/(4*math.tan(math.pi/ns))}")

print("Length of base: ")
l=int(input())
print("Height of parallelogram: ")
h=int(input())
print(f"Expected Output: {l*h}")