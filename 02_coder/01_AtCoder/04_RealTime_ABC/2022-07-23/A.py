l1, r1, l2, r2 = map(int, input().split())

ans = min(r1, r2) - max(l1, l2)
print(ans if ans > 0 else 0)
