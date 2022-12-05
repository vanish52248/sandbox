n = int(input())

ans = []
for i in range(n):
    temp = input()
    count = ans.count(temp)
    if  temp in ans:
        print(f"{temp}{'' if count == 0 else '(' + str(count) + ')'}")
    else:
        print(temp)
    ans.append(temp)
    