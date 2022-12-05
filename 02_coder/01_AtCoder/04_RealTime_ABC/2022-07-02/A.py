k = int(input())


if k < 10:
    print(f"21:0{k}")
elif k < 60:
    print(f"21:{k}")
elif k-60 < 10:
    print(f"22:0{k-60}")
else:
    print(f"22:{k-60}")
