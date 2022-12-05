ans = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
n, x = map(int, input().split())

a = ""
for i in range(26):
    a += (ans[i])*n
    
print(a[x-1])