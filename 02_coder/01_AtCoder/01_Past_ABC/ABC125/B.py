n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
total_value = 0
total_cost = 0

for v_, c_ in zip(v, c):
    if v_ > c_:
        total_cost += c_
        total_value += v_
        
    
print(total_value-total_cost)
