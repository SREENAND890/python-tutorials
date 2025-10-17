
from collections import Counter
s = "aabbbccde"
char_counts = Counter(s)
top_three = char_counts.most_common()
top_three.sort(key=lambda x: (-x[1], x[0]))
for char, count in top_three[:3]:
    print(f"{char} {count}")