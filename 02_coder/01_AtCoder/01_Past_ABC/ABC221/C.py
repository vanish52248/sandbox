from itertools import permutations

s = list(input())
lst = []

for i in permutations(s):
    lst.append(i)
print(lst)
