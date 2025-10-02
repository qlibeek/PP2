import math
import random

class Myclass:
    def __init__(self):
        self.strng = ""
    def getstring(self):
        self.strng = input()
    def printString(self):
        print(self.strng.upper())
a = Myclass()
a.getstring()
a.printString()


2

class Shape:
    def __init__(self):
        self._area: int = 0 

    def area(self) -> int:
        print(f"Shape area: {self._area}")


class Square(Shape):
    def __init__(self, length: int):
        super().__init__()  
        self._length = length
        self._area = self._length ** 2  

    def area(self) -> int:
        print(f"Square area: {self._area}") 

if __name__ == "__main__":
    shape = Shape()
    square = Square(10)

    shape.area(), square.area()


3

class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        super().__init__()  
        self._length = length
        self._width = width
        self._area = self._length * self._width  

    def area(self) -> int:
        print(f"Rectangle area: {self._area}") 

if __name__ == "__main__":
    rectangle = Rectangle(10, 5)

    rectangle.area()


4

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist(self, other: 'Point') -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 1/2


p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()
p2.show()

print("Distance:", p1.dist(p2)) 

p1.move(7, 8)
p1.show() 


5

class bankacc:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,sum):
        self.balance+=sum
    def withdraw(self,sum):
        if sum>self.balance or sum < 0:
            print("Impossible")
        else:
            self.balance-=sum
acc=bankacc("Ali",1000)
acc.deposit(123)
acc.withdraw(12)
print(acc.balance)   


6

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(lambda x: is_prime(x), numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("Prime numbers:", filter_primes(numbers))