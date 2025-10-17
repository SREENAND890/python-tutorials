# a=0
# if a>0:
#     print("it is a positive number")
# elif a==0:
#     print("Zero")
# elif a<0:
#     print("it is negative number")
# else:
#     print("it is not valid")


import json as js
data = '{"name":"john","age":30}'
pd=js.loads(data)
print(pd)