n = int(input())

for i in range(31):
    for j in range(31):
        if j == 0 or j == i:
            print(1)
        else:
            print(i-1+j-1+i-1*j)
