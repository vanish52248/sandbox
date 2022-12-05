a, b = map(str, input().split())

if a == "H":
    print("H" if b == "H" else "D")
elif a == "D":
    print("D" if b == "H" else "H")