# ----------------------------------------------------
# aとbをk進数でかけた値を出力 
# ----------------------------------------------------
# 一度 str で受け取ったのちにint(a, base=k)の第二引数にbase=として進数を割り当てる
# 2進数ならbase=2 今回はｋ進数の為 base=kとなる

k = int(input())
a, b = map(str, input().split())

a = int(a, base=k)
b = int(b, base=k)

print(a * b)

# ----------------------------------------------------
# 1以上ｎ以下の整数の内、10進法で表しても8進法で表しても”７”を含まない数の求め方
# ----------------------------------------------------
# n を 1からnまでループさせて、ひとつずつそれぞれ8進数か10進数の関数を処理して判定していく
def base_ten(num):
    num = str(num)
    if "7" in num:
        return True
    else:
        return False

def base_eight(num):
    s = ""
    while num > 0:
        s = str(num%8) + s
        num //= 8
    if "7" in s:
        return True
    else:
        return False
    
n = int(input())
ans = 0
for i in range(1, n+1):
    if not base_ten(i) and not base_eight(i):
        ans += 1

print(ans)