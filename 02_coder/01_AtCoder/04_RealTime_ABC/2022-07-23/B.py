n = int(input())

a = [list(map(str, list(input()))) for _ in range(n)]

ans = "correct"
for i in range(n):
    for j in range(n):
        if a[i][j] == "W" and a[j][i] != "L":
            ans = "incorrect"
            break
        elif a[i][j] == "L" and a[j][i] != "W":
            ans = "incorrect"
            break
        elif a[i][j] == "D" and a[j][i] != "D":
            ans = "incorrect"
            break
        
print(ans)