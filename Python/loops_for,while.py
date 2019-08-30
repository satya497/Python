# this program about loops
# loops are used for iterations

# while loop
i=1
while i<5:
    print(i)
    i += 1

j=1                      # break in loop
while j<5:
    print(j)
    if j==3:
        break
    j +=1

k=0                     # continue in loop
while k<6:
    k+=1
    if k==3:
        continue
    print(k)

l=5
while l>=5:
    print("*"*l)
    l = l-1


# for loop
for x in "banana":
    print(x)

fruits = {"apple","banana","orange","mango"}
for x in fruits:
    print(x)
    if x=="orange":
        break

for x in fruits:
    if x == "orange":
        continue
    print(x)


for x in  range(6):
    for y in range(6):
        print(x,y)

if None:
    print("hello")
i=1
for x in range(5):
    print(x*5)




