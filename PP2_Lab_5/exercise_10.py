import re

with open("exercise_10_row.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()  

snake = re.sub(r'(?<!^)(?=[A-Z])', '_', data).lower()

print(snake)

