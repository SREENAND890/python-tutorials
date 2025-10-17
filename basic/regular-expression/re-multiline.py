import re

text = """first line
second line
third line"""

print(re.findall(r"^s\w+", text, re.MULTILINE)) 

print(re.findall(r"\w+e$", text, re.MULTILINE)) 