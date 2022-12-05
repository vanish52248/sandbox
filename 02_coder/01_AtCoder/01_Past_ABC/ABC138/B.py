from fractions import Fraction

n = int(input())

a = list(map(int, input().split()))

calc = 0
for i in a:
    calc += Fraction(1, i)
    
print(calc.denominator / calc.numerator)
