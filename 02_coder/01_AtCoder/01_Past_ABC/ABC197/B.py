h, w, x, y = map(int, input().split())

s = [list(input()) for _ in range(h)]
count = 1

# 上の条件
if x > 1:
    for i in range(x)[::-1]:
        print(i-1, y-1)
        if s[i-1][y-1] == ".":
            count += 1
        else:
            break

# 下の条件
# if x < h:
#     for i in range(x, h):
#         if s[i][x-1] == ".":
#             count += 1
#         else:
#             break

# # 左の条件
# if y > 1:
#     for i in range(y)[::-1]:
#         if s[x-1][i] == ".":
#             print(y-1, i)
#             count += 1
#         else:
#             break

# 右の条件
if y < w:
    pass
#     for i in range(x, w):
#         if s[y-1][i] == ".":
#             print(y-1, i)
#             count += 1
#         else:
#             break

# print(count)
