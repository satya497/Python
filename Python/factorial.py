def fact(n):

    a=1
    for i in range(1,n+1):
        a=i*a
    print(a)
in_fact =int(input("enter a value : "))
fact(in_fact)