n,q = map(int,input().split())
A = sorted(list(map(int,input().split())))

for i in range(q):
    x = int(input())
    print(f"x:{x}")
    # 左側
    l = 0
    print(f"l:{l}")
    # 右側は人数ー1
    r = n - 1
    print(f"r:{r}")
    # ans は 人数
    ans = n
    print(f"ans:{ans}")
    
    # 右が左以上の時true 
    while l <= r:
        print("------------ループ開始------------")
        # 中央値は右側から左側を引いて左側を足したもののわる２
        mid = (l+(r-l)//2)
        print(f"mid:{mid}")
        # Aの中央値がｘ以上なら
        if(A[mid] >= x):
            # ansは中央値にする
            ans = mid
            print(f"ans:{ans}")
            # 右側は中央値ひく１
            r =  mid - 1
            print(f"r:{r}")
        else:
            # それ以外は中央値たす１
            l = mid + 1
            print(f"l:{l}")
    # 人数から数値をひく
    print(n - ans)