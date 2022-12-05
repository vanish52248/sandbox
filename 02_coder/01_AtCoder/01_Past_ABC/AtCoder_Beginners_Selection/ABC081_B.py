n = int(input())
a = list(map(int, input().split()))
cnt = 0
flg = True

while(flg):
    for i in range(n):
        if a[i] % 2 != 0:
            flg = False
        else:
            a[i] //= 2
    cnt +=1

print(cnt - 1)