n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
lv = 0

for i in range(n):
    t = a[i]
    lv += b[t-1]
    if i < (n-1) and a[i+1] == a[i] + 1:
      lv += c[t-1]

print(lv)