import re

a, b = map(int, input().split())
s = input()

print(re.search(fr'[0-9]{{{a}}}-[0-9]{{{b}}}', s))
# print("Yes" if re.search(fr'[0-9]{{{a}}}-[0-9]{{{b}}}', s) else "No")
