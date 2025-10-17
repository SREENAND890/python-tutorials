import re 

pattern = re.compile(r"\d+")
text = "123 apples and 456 oranges"
print(pattern.findall(text))  