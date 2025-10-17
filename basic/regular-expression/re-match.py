import re

text="hello world"
a=re.match(r"hello",text)
b=re.match(r"world",text)
print(a)
print(b)