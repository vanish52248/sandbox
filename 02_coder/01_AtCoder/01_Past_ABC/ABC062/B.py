h, w = map(int, input().split())
a = [input() for _ in range(h)]

print("#"*(w+2))
for i in a:
    print(f"#{i}#")
print("#"*(w+2))
