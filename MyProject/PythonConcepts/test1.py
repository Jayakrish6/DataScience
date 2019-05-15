# -*- coding: utf-8 -*-

x1 = 4
x = 'Sally'
print(len(x))

print(x.strip())
print(x.lower())
print(x.upper())

print("Hello, World!")

a = "Hello, World!"
print(a.replace("H", "J"))

#print("Enter your name:")
#x = input()
#print("Hello, " + x)

print("-----------------------------------------------")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
print("-----------------------------------------------")
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print("-----------------------------------------------")
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print("-----------------------------------------------")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)

for x in thislist:
  print(x)
  
if "cherry1" in thislist:
    print("Yes, 'cherry' is in the fruits list")
else:
    print("No, 'cherry1' is not in the fruits list")
    
print(len(thislist))

thislist.append("orange")
print(thislist)
print(len(thislist))

thislist.insert(1, "orange")
print(thislist)

thislist.insert(2, "Banana")
print(thislist)
#thislist.remove("Banana")
print(thislist)


thislist.pop()
print(thislist)

del thislist[0]
thislist.insert(0, "Apple")
print(thislist)


thislist1 = ["apple", "banana", "cherry"]
#del thislist1

thislist1.clear()
print(thislist1)

thislist2 = list(("apple", "banana", "cherry")) 
print(thislist2)

print("=====================TUPPLEs============================")

mylist = list(("list1", "list2", "list3", "list4"))
print(mylist)

mylist2 = ["test1", "test2", "test3", "test4"]
print(mylist2)


thistuple = ("apple", "banana", "cherry")
print(thistuple)

#thistuple = ("apple", "banana", "cherry")
#thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

thistuple = ("apple", "banana", "cherry")
if "apple1" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No, 'apple' is not in the fruits tuple")

thistuple5 = ("apple", "banana", "cherry")
del thistuple5
#print(thistuple5)

print("======================SETs===========================")

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

myset = set(("apple", "banana", "orange"))
print(myset)


print("======================Dictionary===========================")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["brand"]
print(x)

x = thisdict.get("Mustang")
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

for x in thisdict:
  print(x)
  
for x in thisdict.values():
  print(x)
  
for x, y in thisdict.items():
  print(x, y)
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "year" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("No, it's not an key")
    
print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#del thisdict["model"]
print(thisdict)

#del thisdict
print(thisdict)

#thisdict.clear()
print(thisdict.get("model"))

thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

print("======================if ... else ... ===========================")

a = 200
b = 200
print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


print("============================LAMBDA========================")

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))