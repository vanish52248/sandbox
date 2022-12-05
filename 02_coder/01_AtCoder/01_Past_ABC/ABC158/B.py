N, A, B = map(int,input().split())
q = N // (A+B)
r = N % (A+B)
print(q*A+min(r,A))