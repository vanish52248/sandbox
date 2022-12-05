n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_ = max(a)
temporary = []

for i, v in enumerate(a):
    if max_ == v:
            temporary.append(i+1)
            

for i in temporary:
    if i in b:
        print("Yes")
        exit()
    
print("No")