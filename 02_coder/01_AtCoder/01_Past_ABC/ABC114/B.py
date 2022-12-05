s = input()

ans =  10000000000
index = 0
while True:
    if index + 2 > len(s):
        break
    ans = min(ans, abs(int(s[index:index+3])-753))
    index += 1

print(ans)
