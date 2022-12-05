n = int(input())
s = input()
temp_num = 0
max_num = 0

for i in s:
    if i == "I":
        temp_num += 1
        max_num = max(max_num, temp_num)
    else:
        temp_num -= 1
        max_num = max(max_num, temp_num)
print(max_num)