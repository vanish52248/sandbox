from collections import Counter

n = int(input())
a = [input() for _ in range(n)]
counter = Counter(a)

# 出現回数順に要素を取得: most_common()メソッド
print(counter.most_common()[0][0])