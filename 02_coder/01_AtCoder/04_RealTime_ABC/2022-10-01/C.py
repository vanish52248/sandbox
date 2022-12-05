n = int(input())
a = sorted(list(map(int, input().split())))

if 1 not in a and len(a) <= 1:
    print(0)
    exit()
    
book = 0
count = 0
for i in range(len(a)):
    book += 1
    try:
        if a[i] != book:
            max_1 = a.pop(-1)
            max_2 = a.pop(-1)
            count = i
            a.append(i+1)
            a.sort()
    except:
        print(count)
        exit()
