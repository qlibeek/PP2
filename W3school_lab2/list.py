mylist = ["apple", "banana", "orange"]
print(len(mylist))

list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

thislist = ["Eldar", "Tanik", "Erke", "Doshik", "Tima", "Aisha", "Zhansaya", "Aiya"]
print(thislist[1]) # Tanik
print(thislist[-1]) # Tima
print(thislist[2:5]) # Erke, Doshik, Tima
print(thislist[:4]) # Eldar, Tanik, Erke, Doshik
print(thislist[2:]) # from Erke to the end



#---------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#---------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#---------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#---------------------------------------------
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#---------------------------------------------
# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#---------------------------------------------
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#---------------------------------------------
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#---------------------------------------------
# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#---------------------------------------------
# The del keyword can also delete the list completely.
# The clear() method empties the list.

# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#---------------------------------------------
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#---------------------------------------------
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#---------------------------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#---------------------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#---------------------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#---------------------------------------------
# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#---------------------------------------------
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


#---------------------------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
