thisset = {"apple", "banana", "cherry"}
print(thisset)

#---------------------------------------------

# Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#---------------------------------------------

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#---------------------------------------------

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#---------------------------------------------

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#---------------------------------------------

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#---------------------------------------------
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#---------------------------------------------
# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#---------------------------------------------
# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)



