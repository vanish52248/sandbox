from fractions import Fraction


n = int(input())

def calc(n):
    f1 = Fraction(2,n)
    f2 = Fraction(3,n)
    ans = f1 + f2
    # print(ans)

print(calc(n))
