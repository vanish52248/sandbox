n = int(input())

z = 0
for i in range(1, 555555+1):
    
    si = str(i)
    
    ok = True
    
    for s in si:
        if s != si[0]:
            ok = False
            
        if ok:
            z += 1
        
        if ok and z == n:
            ans = i
            
print(ans)