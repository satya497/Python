class remotecontrol:
    def __init__(self):
        self.channels=["HBO","ESPN","MAA","SUN"]
        self.index=-1
    def __iter__(self):
        return(self)
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration
        if self.channels[self.index] == "MAA":
            raise StopIteration
        return self.channels[self.index]
r=remotecontrol()
itr=iter(r)
for x in itr:
    print(x)