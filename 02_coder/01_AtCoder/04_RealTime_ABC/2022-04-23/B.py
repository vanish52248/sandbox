import re
s = input()
lst = []
upper_ = re.search(r"[A-Z]", s)
lower_ = re.search(r"[a-z]", s)

if upper_ and lower_:    
    for i in s:
        if i in lst:
            print("No")
            exit()
        lst.append(i)
    print("Yes")
else:
    print("No")