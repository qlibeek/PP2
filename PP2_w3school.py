# 1
print("Hello world!")


# 2
if 5 > 2:
    print("Five is greater than two!")


x = 5
y = "Hello world!"

print(x, y)


# 3
# This is a comment
print("Hello, World!")


print("Hello, World!")  # It is a comment


print("Hello, World!")
# This is a comment

# This is a comment
# written in
# more than just one line
print("Hello, World!")


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# 4 Variables

x = 5
y = "John"
print(x)
print(y)


x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# is the same as
x = "John"


a = 4
A = "Sally"
# A will not overwrite a


# 4 Names


# legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


"""illegal
2myvar = "sssss"
my-var="dsada"
my var ="sdasda"
"""


# 4 Multiple values


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


x = y = z = "Orange"
print(x)
print(y)
print(z)


fruits = [1, "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# 4 Output variables

x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x, y)

# 4 Global variables

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


# 5
x = 1  # int
y = 2.8  # float
z = 1j  # complex


print(type(x))
print(type(y))
print(type(z))


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12e4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(1, 10))


x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'



# 6 strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


b = "Hello, World!"
print(b[2:5])


b = "Hello, World!"
print(b[:5])


b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])


a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"


a = "Hello, World!"
print(a.replace("H", "J"))


a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)
