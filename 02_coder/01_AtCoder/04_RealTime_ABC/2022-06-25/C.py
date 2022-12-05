n = int(input())
s = list(input())
w = list(map(int, input().split()))

gender = []
count = 0
for i in s:
    if i == "0":
        gender.append("child")
    elif i == "1":
        gender.append("adult")

for i in range(10, 100, 10):
    ans = []
    tmp = 0
    for j in w:
        if j < i:
            ans.append("child")
        elif j >= i:
            ans.append("adult")
    for k, v in zip(gender, ans):
        if k == v:
            tmp += 1
        count = max(count, tmp)
print(count)