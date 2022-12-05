n = int(input())
c = 0

# 1から指定した数までを奇数分ループ
for i in range(1, n+1, 2):
    b = 0
    # 1から奇数分ループして約数を求める
    for j in range(1, i+1):
        if i % j == 0:
            b += 1
        
print(1 if b==8 else 0)