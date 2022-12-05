from collections import Counter

n = int(input())
a = list(map(int, input().split()))

print(Counter(a).most_common()[-1][0])