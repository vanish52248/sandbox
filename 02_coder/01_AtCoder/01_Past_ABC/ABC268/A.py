from collections import Counter

lst = list(map(int, input().split()))

print(len(Counter(lst).most_common()))
