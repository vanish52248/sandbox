def calc(n):
    f = n * (n-1)
    return f

n = int(input())


print(0 if n == 0 else calc(n))


