n, q = map(int, input().split())
s = list(input())
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        num_ = (x//t) + (x%t)
        for i in range(num_):
            temp = s.pop()
            s.insert(0, temp)
    elif t == 2:
        print(s[x-1])
        
        