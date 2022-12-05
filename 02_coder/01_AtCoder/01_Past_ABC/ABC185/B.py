n, m, t = map(int, input().split())
max_n = n

time_lst = [list(map(int, input().split())) for _ in range(m)]

if (n - time_lst[0][0]) <= 0:
    print("No")
    exit()
else:
    n -= time_lst[0][0]
    if m == 1:
        n = n+time_lst[0][1] - time_lst[0][0] if n+time_lst[0][1] - time_lst[0][0] < max_n else max_n
    else:        
        for i in range(m-1):
            n = n+time_lst[i][1] - time_lst[i][0] if n+time_lst[i][1] - time_lst[i][0] < max_n else max_n
            if n - (time_lst[i+1][0] - time_lst[i][1]) <= 0:
                print("No")
                exit()
            else:
                n -= (time_lst[i+1][0] - time_lst[i][1])
        n += (time_lst[m-1][1] - time_lst[m-1][0])


if n - (t-time_lst[m-1][1]) <= 0:
    print("No")
    exit()
else:
    print("Yes")
