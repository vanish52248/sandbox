x = int(input())

for number1 in range(x,10**5):
    count=0
    for number2 in range(1,number1):
            number=number1%number2
            if number==0:
                count+=1
    if count==1:
        print(number1)
        exit()
    