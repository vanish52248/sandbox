import collections

# 改良前の処理(setdefault)
dict_ = {}
list_ = ["a", "a", "a", "b", "b", "c"]
for word in list_:
    # 1回目のループでは空dictの為 "a"がキーエラーになる。それを防止するための処理
    # if word not in dict_:
    #     dict_[word] = 0

    # 上記処理が下記でワンライナーで済む(wordのキーがない場合は {word:0}で初期化する処理)
    dict_.setdefault(word, 0)
    dict_[word] += 1
print(dict_)

# 改良後の処理→int の 0で初期化してくれる処理(defaultdict)
dict_ = collections.defaultdict(int)
list_ = ["a", "a", "a", "b", "b", "c"]
for word in list_:
    dict_[word] += 1
print(dict_)
