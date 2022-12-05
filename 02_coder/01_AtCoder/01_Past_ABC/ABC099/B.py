a, b = map(int, input().split())

ans = 0
flg = True
for i in range(1, 999):
    ans += i
    print("========", ans)
    if flg and ans >= a:
        flg = False
        if ans - a <= 0:
            continue
        else:
            print(ans - a)
            exit()
    elif not flg and ans >= b:
        print(ans - b)
        exit()
