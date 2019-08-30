class report:
    def __init__(self,name,rollno,eng,mat,sci,total,percent):
        self.name=name
        self.rollno=rollno
        self.eng=eng
        self.mat=mat
        self.sci=sci
        self.total=total
        self.percent=percent
    def progress(self):
        self.total=self.eng+self.mat+self.sci
        self.percent=(self.total/300)*100
        print("Student : "+self.name)
        print("Roll No : "+self.rollno)
        print("English : "+str(self.eng))
        print("Maths : "+str(self.mat))
        print("Science : "+str(self.sci))
        print("Total : "+str(self.total))
        print("Percentage : "+str(self.percent))
        print(" ")
p1=report("satya","497",98,96,89,0,0)
p2=report("akhil","498",92,89,56,0,0)
p3=report("santosh","499",94,78,91,0,0)
p1.mat=100
p1.progress()
p2.progress()
p3.progress()