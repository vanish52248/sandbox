h, w  = map(int, input().split())

g = [list(input()) for _ in range(h)]
judge_lst = set()

i, j = 1, 1
while True:
    if g[i-1][j-1] == "U" and i != 1:
        i -= 1
        j = j
        judge_lst.add(g[i-1][j-1])

        if "RDLU" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "LURD" in ("").join(judge_lst) or \
        "URDL" in ("").join(judge_lst) or \
        "UDRL" in ("").join(judge_lst) or \
        "RLUD" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "DURL" in ("").join(judge_lst) or \
        "RDUL" in ("").join(judge_lst) or \
        "RUDL" in ("").join(judge_lst) or \
        "LDRU" in ("").join(judge_lst) or \
        "LDRU" in ("").join(judge_lst) or \
        "UDLR" in ("").join(judge_lst) or \
        "RDUL" in ("").join(judge_lst) or \
        "LRUD" in ("").join(judge_lst) or \
        "LRDU" in ("").join(judge_lst) or \
        "ULDR" in ("").join(judge_lst) or \
        "RULD" in ("").join(judge_lst) or \
        "DRUL" in ("").join(judge_lst):
            print(-1)
            exit()
    elif g[i-1][j-1] == "D" and i != h:
        i += 1
        j = j
        judge_lst.add(g[i-1][j-1])
        
        if "RDLU" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "LURD" in ("").join(judge_lst) or \
        "UDLR" in ("").join(judge_lst) or \
        "LRDU" in ("").join(judge_lst) or \
        "RUDL" in ("").join(judge_lst) or \
        "URDL" in ("").join(judge_lst) or \
        "RDUL" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "LRUD" in ("").join(judge_lst) or \
        "DURL" in ("").join(judge_lst) or \
        "RLUD" in ("").join(judge_lst) or \
        "UDRL" in ("").join(judge_lst) or \
        "ULDR" in ("").join(judge_lst) or \
        "RULD" in ("").join(judge_lst) or \
        "DRUL" in ("").join(judge_lst):
            print(-1)
            exit()
    elif g[i-1][j-1] == "L" and j != 1:
        i = i
        j -= 1
        judge_lst.add(g[i-1][j-1])
        
        if "RDLU" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "LURD" in ("").join(judge_lst) or \
        "RDUL" in ("").join(judge_lst) or \
        "LRUD" in ("").join(judge_lst) or \
        "DURL" in ("").join(judge_lst) or \
        "UDRL" in ("").join(judge_lst) or \
        "UDLR" in ("").join(judge_lst) or \
        "URDL" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "RLUD" in ("").join(judge_lst) or \
        "LDRU" in ("").join(judge_lst) or \
        "LRDU" in ("").join(judge_lst) or \
        "ULDR" in ("").join(judge_lst) or \
        "RUDL" in ("").join(judge_lst) or \
        "RULD" in ("").join(judge_lst) or \
        "DRUL" in ("").join(judge_lst):
            print(-1)
            exit()
    elif g[i-1][j-1] == "R" and j != w:
        i = i
        j += 1
        judge_lst.add(g[i-1][j-1])
        
        if "RDLU" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "LURD" in ("").join(judge_lst) or \
        "RLUD" in ("").join(judge_lst) or \
        "UDLR" in ("").join(judge_lst) or \
        "URDL" in ("").join(judge_lst) or \
        "UDRL" in ("").join(judge_lst) or \
        "DLUR" in ("").join(judge_lst) or \
        "LDRU" in ("").join(judge_lst) or \
        "DURL" in ("").join(judge_lst) or \
        "LRUD" in ("").join(judge_lst) or \
        "RUDL" in ("").join(judge_lst) or \
        "ULDR" in ("").join(judge_lst) or \
        "LRDU" in ("").join(judge_lst) or \
        "RDUL" in ("").join(judge_lst) or \
        "RULD" in ("").join(judge_lst) or \
        "DRUL" in ("").join(judge_lst):
            print(-1)
            exit()
    else:
        break

print(i, j)
