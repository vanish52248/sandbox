n = int(input())
h = list(map(int, input().split()))
t = h[0]

for i in range(n-1):
    if h[i+1] > t:
        t = h[i+1]
    else:
        break

print(t)