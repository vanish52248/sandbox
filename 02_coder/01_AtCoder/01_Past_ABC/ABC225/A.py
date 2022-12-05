from itertools import permutations
s = list(input())
st = set()
for i in permutations(s):
    st.add(i)
    
print(st)