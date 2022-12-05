r, d, x = map(int, input().split())
lst = []
current = 0

for i in range(10):
  if i == 0:
    current = (r * x) - d # 30
    x = current
  else:
    current = (r * x) - d
    x = current
  lst.append(current)
  
for i in lst:
  print(i)