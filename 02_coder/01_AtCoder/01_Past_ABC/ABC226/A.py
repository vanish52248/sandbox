# 四捨五入 roundは偶数丸めなので42.5などは偶数の42が返ってきてしまう
# 繊細な計算が求められる時は下記の様に Decimalで行うのが良い
from decimal import *

print(Decimal(str(float(input()))).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
