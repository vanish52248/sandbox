# s = input()

# print("No" if "oo" in s or "oxo" in s or "xxx" in s else "Yes")

t = "oxx" * 100
s = input()
print("Yes" if s in t else "No")