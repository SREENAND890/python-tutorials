import re

text = "apple, orange; banana, grape"
print(re.split(r"[;,]", text))  