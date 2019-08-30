class myclass:
    def __init___(self):
        self.a=1
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            val=self.a
            self.a+=1
            return val
        else:
            raise StopIteration
values = myclass()
myiter=iter(values)
for x in myiter:
    print(x)
    