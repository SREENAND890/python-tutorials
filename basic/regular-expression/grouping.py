import re

text = "John: 34, Alice: 45, Bob: 23"
print(re.findall(r"(\w+): (\d+)", text)) 