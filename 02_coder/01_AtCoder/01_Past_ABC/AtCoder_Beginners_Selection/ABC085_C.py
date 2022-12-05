x,y = map(int, input().split())

for i in range(x+1):
  for j in range(x+1):
    k = x - (i + j)
    if i * 10000 + j * 5000 + k * 1000 == y and k >= 0:   
      if x == i + j + k:
        print(i,j,k)        
        exit()
else:
    print(-1, -1, -1)
