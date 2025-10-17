import re

text = "I have 2 apples and 5 oranges."
for match in re.finditer(r"\d+", text):
    print(match.group(), "at", match.start())