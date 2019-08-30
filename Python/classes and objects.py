# this program about objects and classes
# a class is like a object constructor
#The __init__() function is called automatically every time the class is being used to create a new object.
class classroom:
    def __init__(self, name, age):   # methods
        self.name=name
        self.age=age
    def myfunc1(self):
        print("my name is "+self.name)
        print(self.name+" age is "+str(self.age))
p1=classroom("satya",23)
p2=classroom("ravi",21)
p3=classroom("akhil",24)
p1.age=22
p1.myfunc1()
p2.myfunc1()
p3.myfunc1()

class myclass:
    def reversing(self,s):
        return ' '.join(reversed(s.split()))
print(myclass().reversing('my name is'))

str1 = "how are you"
str2=str1.split(" ")
output = ' '.join(str2)
print(reversed(str2))
