n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]

for i in range(n) :
	a[i], b[i] = map(int, input().split())

res = 1000000000
for i in range(n) :
	for j in range(n) :
		res = min(res, a[i] + b[j] if i == j else max(a[i], b[j]))

print(res)

