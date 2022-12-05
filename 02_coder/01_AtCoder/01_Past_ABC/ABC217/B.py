l = ["ABC", "ARC", "AGC", "AHC"]
s1 = input()
s2 = input()
s3 = input()
s = [s1, s2, s3]
print("".join(set(l) - set(s)))