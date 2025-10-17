# import json as js
# data = '{"name":"john","age":30}'
# pars=js.loads(data)
# print(pars)   
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
            return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

def s(n):
    if n==0:
        return 0
    else:
        return fibonacci(n)+ s(n-1)    
print(s(6))

