x, y, n = map(int, input().split())

price = 0
if x * 3 < y:
    price = x * n
else:    
    price = ((n//3)*y)+((n%3)*x)
    
print(price)
