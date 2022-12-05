n, m = map(int, input().split())

c = [list(map(str, input().split())) for _ in range(m)]

for i in range(1, n+1):
    temp = ""
    for j in range(len(c)):
        if i % int(c[j][0]) == 0:        
            temp += c[j][1] + " "
    if temp == "":
        temp += str(i)
    temp= temp.rstrip()
    temp = temp.replace(",", "")
    print(temp)
