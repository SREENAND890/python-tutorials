import re

text = "I have 2 apples and 5 oranges."
print(re.findall(r"\d+", text))  

text = "The price is 45 dollars, 30 cents, and 50 rupees."
print(re.findall(r"\d+", text))  