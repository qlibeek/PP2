import re
with open("exercise_9_row.txt") as f:
    data=f.read()
print(re.findall(r"[A-Z][a-z]*", data))