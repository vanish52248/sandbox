n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cost_zero = 0
cost_goal = 0

for i in range(x, -1, -1):
    if i in a:
        cost_zero += 1

for i in range(x, n):
    if i in a:
        cost_goal += 1
        
print(min(cost_zero, cost_goal))