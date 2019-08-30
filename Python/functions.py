# program about functions

def myfunction(name):
    print("hello "+name)
myfunction("ravi")
myfunction("satya")
myfunction("sai")

def my_function(country="Norway"):
  print("I am from " + country)
nation = {1,2,3}
for x in nation:
    my_function(x)

            #OR
nation = {1,2,3}
def my_function(country):
    for x in country:
        print(x*5)
my_function(nation)

#or
num = {1,2,3,4,5}
def myfunction(nums):
    return 5*nums
for y in num:
    print(myfunction(y))   

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)     
