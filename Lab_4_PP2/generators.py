#1
def square_generator(n):
    result = []  
    for i in range(n):
        
        k = (i+1)**2
        result.append(k)
    return result

n = int(input())
squares = square_generator(n)

for square in squares:
    print(square)



#2
def evens(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(i) for i in evens(n)))



#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
for num in divisible_by_3_and_4(n):
    print(num)



#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for num in squares(a, b):
    print(num)



#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in countdown(n):
    print(num)