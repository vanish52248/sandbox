x, y, z = map(int, input().split())
space = y + z
person = 0

while True:
    if x - space >= z:
        x -= space
        person += 1
    else:
        break

print(person)