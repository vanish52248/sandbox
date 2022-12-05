import math

x = int(input())
c = 0
r = 100

while True:
    c += 1
    r  += math.floor((r//100))
    # print(f"c: {c} | r:{r}")
    if r >= x:
        break
    
print(c)