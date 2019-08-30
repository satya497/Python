class student:
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age
        self.lap=self.laptop()
    def details(self):
        return (f'{self.name,self.roll,self.age}\n {self.lap.lapdetails()}')
        # return(self.lap.lapdetails())
        # print(self.lap.lapdetails())
    class laptop:
        def __init__(self):
            self.brand="dell"
            self.ram="8gb"
        def lapdetails(self):
            return(self.brand,self.ram)
s1=student("satya",497,22)
s2=student("akhil",498,23)
print(s1.details())
print(s2.details())
