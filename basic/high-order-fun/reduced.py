from functools import reduce

num=[1,2,3,4,5,6,7,8,9,10]
reduuced=reduce(lambda a,b:a+b, num ,0)
print(reduuced)