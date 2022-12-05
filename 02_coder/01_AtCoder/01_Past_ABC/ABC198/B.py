# 回文か判定する処理
import sys

n = list(input())
ans = []
ans_r = []

for i in n:
    ans.append(i)

for i in ans[::-1]:
    ans_r.append(i)
    
if ans == ans_r:
    print("Yes")
    sys.exit()
    
for _ in n:
    ans.insert(0, "0")
    ans_r.append("0")
    if ans == ans_r:
        print("Yes")    
        sys.exit()

print("No")