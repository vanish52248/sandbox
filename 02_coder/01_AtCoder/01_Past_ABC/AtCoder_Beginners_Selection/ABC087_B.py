a = int(input()) # 500
b = int(input()) # 100
c = int(input()) # 50
x = int(input())
cnt = 0

for i in range(0, a+1):
    for j in range(0, b+1):
        for k in range(0, c+1):
            if x == (500*i + 100*j + 50*k):
                cnt += 1
print(cnt)