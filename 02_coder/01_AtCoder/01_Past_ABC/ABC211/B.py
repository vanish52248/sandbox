s1 = input()
s2 = input()
s3 = input()
s4 = input()

# リスト内包表記 → s = [input() for _ in range(4)]

l = set([s1, s2, s3, s4])
print("Yes" if len(l) == 4 else "No")
