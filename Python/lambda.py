# about lambda function
# a lambda can take any number of arguments but have only one expression

x = lambda a : a +10
x=lambda a,b:a*b
print(x(5,6))
print(x(4,5))

def my_function(n):
    return lambda a: a*n
mytripler = my_function(3)

print(mytripler(11))

