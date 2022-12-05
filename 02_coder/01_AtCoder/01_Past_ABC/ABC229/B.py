a,b = map(int,input().split())

while a>0 and b>0:
    # print(a,b)
    # print(f"a%10:{a%10}, b%10:{b%10}")
    if a%10 + b%10 >=10:
        print("Hard")
        exit()
    a = a//10
    b = b//10
print("Easy")
