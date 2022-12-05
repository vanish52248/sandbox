# numpy
import numpy as np
h, w = map(int, input().split())
current_lst = []    
result_lst = np.zeros((h, w))

for i in range(h):
    current_lst.append(list(input()))
    
for i in range(h):
    for j in range(w):
        if current_lst[i][j] == "#":
            result_lst[i] = [True] * w
            result_lst[:h, j:j+1] = True
            
print(np.count_nonzero(result_lst))
    