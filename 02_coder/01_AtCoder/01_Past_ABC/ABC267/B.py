s = input()
pins = [[s[0]], [s[1], s[2]],[s[3], s[4], s[5]], [s[6], s[7], s[8], s[9]]]
ans = "No"

for i in range(len(pins)-1):
    if i == 0 and pins[i][i] == "1":
        break
        for j in range(len(pins[i])-1):
            if pins[i][j] == "0":
                
print(ans)
