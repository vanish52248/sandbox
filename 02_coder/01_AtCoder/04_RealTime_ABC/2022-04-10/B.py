n = int(input())
result = []

for i in range(n):
    s, t = map(str, input().split())
    if s in result and t in result:
        print("No")
        exit()
    elif s in result:
        