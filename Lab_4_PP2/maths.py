#1
import math
k=float(input("Enter the number:"))
print("Radian:",math.radians(k))



#2
import math
h=float(input("Hight:"))
a=float(input("Base,first value:"))
b=float(input("Base,second value:"))
print("Trapazoide area:",(a+b)*0.5*h)



#3
import math
n=int(input("Input number of sides:"))
a=int(input("Input the length of a side:"))
area = (n * a**2) / (4 * math.tan(math.pi / n))
print("Area:",area)



#4
import math
b=int(input("a:"))
a=int(input("b:"))
print(float(a*b))