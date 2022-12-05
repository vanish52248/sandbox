n = int(input())

unique_st = set()
ans = 0
index = 0
for i in range(1, n+1):
    s, t = map(str, input().split())
    len_ = len(unique_st)
    unique_st.add(s)
    if len_ + 1 == len(unique_st):
        if ans < int(t):
            ans = int(t)
            index = i

print(index)