def highorder(a,b,subs):
    return subs(a,b)

def plus(a,b): 
    return a+b

def multiply(a,b):
    return a*b

def substraction(a,b):
    return a-b

def division(a,b):
    return a/b

print(highorder(2,7,plus))
print(highorder(3,4,multiply))
print(highorder(300,10,division))
print(highorder(40,5,substraction))