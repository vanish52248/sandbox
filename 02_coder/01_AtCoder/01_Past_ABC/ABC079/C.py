a = list(input())

# + + +
temp = 0
lst = ["+", "+", "+"]
for i in a:
    temp += int(i)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
# + + -
temp = 0
lst = ["+", "+", "-"]
for i, v in enumerate(a):
    if i == 3:
        temp -= int(v)
    else:
        temp += int(v)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
# + - +
temp = 0
lst = ["+", "-", "+"]
for i, v in enumerate(a):
    if i == 2:
        temp -= int(v)
    else:
        temp += int(v)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
# - + +
temp = 0
lst = ["-", "+", "+"]
for i, v in enumerate(a):
    if i == 0:
        temp = int(v)
    elif i == 1:
        temp -= int(v)
    else:
        temp += int(v)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
# - - -
temp = 0
lst = ["-", "-", "-"]
for i, v in enumerate(a):
    if i == 0:
        temp = int(v)
    else:
        temp -= int(v)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
# - - +
temp = 0
lst = ["-", "-", "+"]
for i, v in enumerate(a):
    if i == 0:
        temp = int(v)
    elif i == 3:
        temp += int(v)
    else:
        temp -= int(v)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
# - + -
temp = 0
lst = ["-", "+", "-"]
for i, v in enumerate(a):
    if i == 0:
        temp = int(v)
    elif i == 2:
        temp += int(v)
    else:
        temp -= int(v)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
# + - -
temp = 0
lst = ["+", "-", "-"]
for i, v in enumerate(a):
    if i == 0:
        temp = int(v)
    elif i == 1:
        temp += int(v)
    else:
        temp -= int(v)
if temp == 7:
    print(a[0]+lst[0]+a[1]+lst[1]+a[2]+lst[2]+a[3] + "=7")
    exit()
