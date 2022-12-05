a,b,k=map(int, input().split())

lst = set()

for i in range(a,min(a+k-1,b)+1):
    lst.add(i)

for i in reversed(range(max(a,b-k+1),b+1)):
    lst.add(i)
lst = list(lst)
lst.sort()
for c in lst:
    print(c)
