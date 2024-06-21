### operator

a = 4
b = 2
print(a + b)  # 6
print(a - b)  # 2
print(a * b)  # 8
print(a / b)  # 2.0
print(a ** b) # a 的 b 次方 = 16
print(a // b) # 商 = 2
print(a % b)  # 餘 = 0


a = 4
b = 2
print(a == b)   # a 是否等於 b?    -> False
print(a != b)   # a 是否不等於 b?  -> True
print(a > b)    # a 是否大於 b?    -> True
print(a >= b)   # a 是否大於等於b?  -> True
print(a < b)    # a 是否小於 b?    -> False
print(a <= b)   # a 是否小於等於 b? -> False



a = 4
a += 4      # a = a + 4 = 8
a -= 4      # a = a - 4 = 0
a *= 4      # a = a * 4 = 16
a /= 4      # a = a / 4 = 1
a //= 3     # a = a // 3 = 1
a %= 3      # a = a % 3 = 1
a **= 3     # a = a ** 3 = 64



a = (3 == 5) and (2 >= 2)  # False and True = False
b = (5 == 5) and 4         # True and True = True
c = (4 <= 2) or (5 >= 2)   # False or True = True
d = not -2                 # not True = False