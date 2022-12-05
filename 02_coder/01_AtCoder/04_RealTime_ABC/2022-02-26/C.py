N=int(input())
S=[list(input()) for _ in range(N)]

for i in range(N):
  for j in range(N-5):
    R=[]
    C=[]
    for k in range(6):
      R.append(S[i][j+k])
      C.append(S[j+k][i])
      if R.count("#")>=4 or C.count("#")>=4:
        print("Yes")
        exit()
for i in range(N-5):
  for j in range(N-5):
    D=[]
    U=[]
    for k in range(6):
      D.append(S[i+k][j+k])
      U.append(S[i+5-k][j+k])
    if D.count("#")>=4 or U.count("#")>=4:
      print("Yes")
      exit()
print("No")