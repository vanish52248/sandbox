s = list(input())
start = (len(s) - 1) // 2 # 3
end = (len(s) + 3) // 2   # 5
temp_s = ""
temp_e = ""

for i in range(start):
    temp_s += s[i]

# リスト内の文字列を逆順に処理する方法 level → el
for i in range(end-1, len(s)): # 5から7文字目をそのまま処理
    temp_e += s[i]

print("Yes" if temp_s == temp_e else "No")