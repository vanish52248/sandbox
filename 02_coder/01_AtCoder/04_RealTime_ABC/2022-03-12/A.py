v, a, b, c = map(int, input().split())
r = ""

while True:
    if v >= a:
        v -= a
        if  v >= b:
            v -= b
            if v >= c:
                v -= c
                if v >= a:
                    continue
                else:
                    r = "F"
                    break
            else:
                r = "T"
                break
        else:
            r = "M"
            break
    else:
        r = "F"
        break
print(r)