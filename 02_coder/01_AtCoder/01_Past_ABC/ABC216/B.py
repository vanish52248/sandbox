n = int(input())
st = set()

for i in range(n):
    s, t = map(str, input().split())
    st.add(tuple([s, t]))

print("No" if n==len(st) else "Yes")