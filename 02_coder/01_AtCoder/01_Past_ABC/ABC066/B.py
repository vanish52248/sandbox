s = input()[:-1]

while True:
    if len(s) % 2 == 0:
        if s[0:((len(s)//2)-1)] == s[((len(s)//2)):-1]:
            print(len(s))
            break
        s = s[:-1]
    else:
        s = s[:-1]
        