class student:
    school = "Abhyudaya techno"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def info(self):
        return self.school
s1=student(78,89,99)
s2=student(78,65,89)
s2.school="narayana"
print(s1.avg())
print(s2.avg())
print(s1.info())
print(s2.info())
