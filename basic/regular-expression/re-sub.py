import re

t="hello123 world456!"
a=re.sub(r"\d+","number",t)
print(a)
