n = int(input())
t = list(input())
current = "e"
x = 0
y = 0

for i in range(n):
    if current == "e":
        if t[i] == "S":
            x += 1
        else:
            current = "s"
    elif current == "s":
        if t[i] == "S":
            y -= 1
        else:
            current = "w"
    elif current == "w":
        if t[i] == "S":
            x -= 1
        else:
            current = "n"
    elif current == "n":
        if t[i] == "S":
            y += 1
        else:
            current = "e"
            
print(x, y)
