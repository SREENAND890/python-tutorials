import re

text = "Hello\nWorld"
print(re.search(r"Hello.*World", text)) 
print(re.search(r"Hello.*World", text, re.DOTALL))