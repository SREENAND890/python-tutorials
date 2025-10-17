# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* fact(n - 1)
    
# print(fact(5))

# def i(n):
#     a=1
#     for i in range(1,n+1):
#         a=a*i
#     return a
    
# print(i(5))

def tail(n,a=1):
    if n==0 or n==1:

       return a
    else:
       return tail(n-1,a*n)
    
print(tail(6))    
