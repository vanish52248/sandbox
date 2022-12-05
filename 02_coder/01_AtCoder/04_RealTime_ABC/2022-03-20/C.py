n = int(input())
choice_num = []
choiced_num = []
player = "takahashi"
for i in range(1, ((2*n)+1)+1):
    choice_num.append(i)
    
while True:
    if player == "takahashi":
        for i in choice_num:
            if i not in choiced_num:
                print(i, flush=True)
                choiced_num.append(i)
                player = "aoki"
                break
            elif i in choiced_num and i == len(choice_num):
                exit()
    elif player == "aoki":
        m = int(input())
        choiced_num.append(m)
        player = "takahashi"