s1 = input()
s2 = input()
s3 = input()
s4 = ""
t = list(map(int, input()))

for i in range(len(t)):
    s4 += s1 if t[i] == 1 else s2 if t[i] == 2 else s3

print(s4)
