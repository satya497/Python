# this program about collections
""" it inludes lists
               Tuples
               Sets
               Dictionaries """

# about dictionaries
# dictionaries are changeable and unordered and indexed
# these are contains keys and values
# dictionaries can be written in curly braces {}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
mydict = {
    "name":"satya",
    "roll":"497",
}
print(mydict)
x= mydict["name"]
print(x)
x=mydict.get("roll")
print(x)
mydict["branch"]="ECE"
print(mydict)
y = mydict.get("branch")
print(y)
for a,b in mydict.items():
    print(a,b)
print(len(thisdict))
tempdict = mydict.copy()
temp1dict = dict(thisdict)
print(temp1dict)
print(tempdict)
mydict.pop("roll")
thisdict.popitem()
del thisdict["model"]
del thisdict
mydict.clear()
tempdict = dict(rank=1,grade="A")
print(tempdict)
x=tempdict.setdefault("name","ravi")
print(x)
print(mydict)


# about sets
# sets can be written in curly braces {}
# sets are unordered and unindexed and changeable

myset = {"item1","item2"} 
myset.update({"item3","item4"})
print(myset)
myset.discard("item1")
myset2 = set(("item6","item7",10))
print(myset2)
myset2.add("satya")
print(myset2)
myset3 = myset.difference(myset2)
print("myset3 is"+str(myset3))


# about tuples
# tuples can be written in round braces ()
# these are unchangeable and ordered and indexed
# we cannot add or delete items to tuple
# but we can delete tuple

mytuple = ("satya","item 3", "item 5")
print (mytuple)
print(mytuple[1])
for x in mytuple:
  print(x)
if "satya" in mytuple:
  print("yes")
  print(len(mytuple))       # length of a tupple
mytuple1 = tuple(("song1","song1","song2","song3"))
print (mytuple1)
x=mytuple1.count("song1")   #getting count of item in tuple
print(x)
x=mytuple1.index("song2")   # getting index of item
print(x)


# about lists
# lists are changeable and ordered and allows duplicate members

mylist = ["apple","banana","cat"]
print(mylist)
mylist[2] = "bat"
print(mylist)
for x in mylist :
  print(x)
print(mylist[2])        # print a specific item in list
if "apple" in mylist:
  print("yes")
print(len(mylist))      #length of the list
mylist.append("rat")    # appending into la list
mylist.insert(1,"dog")  # inserting into a list
print(mylist)
mylist.remove("banana") #removing from list
print(mylist)
mylist.pop
del mylist[0]
mylist1 = mylist.copy() # copying a list
mylist2 = list(mylist1) #new list
mylist.clear()           
mylist2 = list(("satya","sai","ravi")) # new list
print(mylist2)
mylist.extend(mylist1)   # extending a list
print(mylist)
mylist.reverse()         # reversing a list
print(mylist)
mylist.sort()            # sorting a list
print(mylist)
mylist.insert(1,"algo")
print(mylist)