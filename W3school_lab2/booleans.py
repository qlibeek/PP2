print(10 > 9) # True
print(10 < 9) # False
print(10 == 10) # True

a = 100
b = 200

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

print(bool("Hello"))
print(bool(10))

# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool(())) # False
print(bool([])) # False

def myFunction() :
  return True
print(myFunction())

x = 200
print(isinstance(x, int))






