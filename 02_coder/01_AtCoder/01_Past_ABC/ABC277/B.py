n = int(input())
lst = []
s = [list(map(str, input().split())) for _ in range(n)]

for i in range(len(s)):
    if s[i][0][0] == "H" or s[i][0][0] == "D" or s[i][0][0] == "C" or s[i][0][0] == "S":
        if s[i][0][1] == "A" or s[i][0][1] == "2" or s[i][0][1] == "3" or s[i][0][1] == "4" or s[i][0][1] == "5" or s[i][0][1] == "6" or \
           s[i][0][1] == "7" or s[i][0][1] == "8" or s[i][0][1] == "9" or s[i][0][1] == "T" or s[i][0][1] == "J" or s[i][0][1] == "Q" or s[i][0][1] == "K":
                if s[i] not in lst:
                  lst.append(s[i])
                else:
                    print("No")
                    exit()
        else:
            print("No")
            exit()
    else:
        print("No")
        exit()
    
print("Yes")
    