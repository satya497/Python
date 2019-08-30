def largerstring(name,num):
    result=""
    for i in range(num):
        result=result+name+"\n"
    return result
in_name = input("enter a name :")
in_num = int(input("enter a how many times copied :"))
with open('C:\\Users\\Admin\\Desktop\\Satya.txt', 'a') as f1:
    f1.write(largerstring(in_name,in_num))
with open('C:\\Users\\Admin\\Desktop\\Satya.txt',"w") as f2:
    f1.truncate()
with open('C:\\Users\\Admin\\Desktop\\Satya.txt',"w") as f3:
    print(f1.read())
