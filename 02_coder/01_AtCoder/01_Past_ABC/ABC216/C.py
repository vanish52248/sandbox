n = int(input())
c = []

for i in range(120):
        if n == 0:
            break
        elif n % 2 == 0:
            n //= 2
            c.insert(0, "B")
        else:
            n -= 1
            c.insert(0, "A")
       
print("".join(c))
    