x = input()

lst = "123456789012345678901"

if x[0] == x[1] == x[2] == x[3]:
    print("Weak")
elif x in lst:
    print("Weak")
else:
    print("Strong")