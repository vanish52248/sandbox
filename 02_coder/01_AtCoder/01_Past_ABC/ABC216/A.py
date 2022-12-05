x, y = map(int, input().split("."))

print(f"{x}-" if 0 <= y <= 2 else f"{x}" if 3 <= y <= 6 else f"{x}+")