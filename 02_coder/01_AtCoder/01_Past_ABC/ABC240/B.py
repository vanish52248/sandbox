n = int(input())
a = list(map(int, input().split()))
st = set()
for i in a:
    st.add(i)

print(len(st))