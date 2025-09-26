mytuple = ("apple", "banana", "cherry")
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


#---------------------------------------------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


#---------------------------------------------
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


#---------------------------------------------
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


#---------------------------------------------
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#---------------------------------------------
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#---------------------------------------------
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


#---------------------------------------------
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# count() - Returns the number of times a specified value occurs in a tuple
# index() - Searches the tuple for a specified value and returns the position of where it was found






