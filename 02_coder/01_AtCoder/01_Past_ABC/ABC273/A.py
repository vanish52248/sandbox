def f(x):
    # 再記関数の終了条件
    if x == 0:
        return 1
    else:
        return x * f(x-1)


n = int(input())
print(f(n))
