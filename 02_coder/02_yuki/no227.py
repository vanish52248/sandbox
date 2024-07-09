from collections import Counter

a = list(map(int, input().split()))
st = set(a)

if len(st) == 2 and Counter(a).most_common()[0][1] == 3:
    print("FULL HOUSE")
elif len(st) == 4:
    print("ONE PAIR")
elif len(st) == 3:
    if Counter(a).most_common()[0][1] == 3:
        print("THREE CARD")
    else:
        print("TWO PAIR")
else:
    print("NO HAND")