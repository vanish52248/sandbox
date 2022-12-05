n , x = map(int, input().split())

ans = str(bin(x)[2:])

a = []
for _ in range(n):
    a.append(int(input()))

index = 0
for i in a:
    # reversed()だけでprintすると<reversed>オブジェクトになっていて使えないので更に外でlist()化することで配列に戻している
    print(list(reversed(ans))[a[index]-1])
    index += 1
