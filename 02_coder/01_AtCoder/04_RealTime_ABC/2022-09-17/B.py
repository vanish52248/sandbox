s_list = [input() for _ in range(10)]

a = -1
b = -1
c = -1
d = -1

for i, s in enumerate(s_list):
  if c == -1:
    c = s.find('#')
    d = s.rfind('#')
  if c == -1:
    continue

  if a == -1:
    a = i
  if s.find('#') != -1:
    b = i

print(a + 1, b + 1)
print(c + 1, d + 1)
