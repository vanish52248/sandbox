n = int(input())
r = 0

for i in range(n):
    if 2 ** i <= n:
        continue
    else:
        r = i-1
        break
    
print(r if n!=2 else 1)

# n = int(input())
# ans = 0
# while(2**ans <= n):
#     ans += 1
# print(ans-1)