import re

text = "HELLO world"
print(re.search(r"hello", text, re.IGNORECASE))