# 5-op.py

# 算術運算子
print(4 + 2)  # 6
print(4 - 2)  # 2
print(4 * 2)  # 8
print(4 / 2)  # 2.0
print(4 ** 2) # 4 的 2 次方 = 16
print(4 // 2) # 商 = 2
print(4 % 2)  # 餘 = 0


print(1 + 2 * 3)
# = 1 + 6 = 7
print(6 - 2 % 3)
# = 6 - 2 = 4
print(6 // (2 + 1))
# = 6 // 3 = 2
print(9 ** 0.5 - 2)
# = 3.0 - 2 = 1.0



# 比較運算子
print(4 == 2)   # 4 是否等於 2 ?    -> False
print(4 != 2)   # 4 是否不等於 2 ?  -> True
print(4 > 2)    # 4 是否大於 2 ?    -> True
print(4 >= 2)   # 4 是否大於等於 2 ?  -> True
print(4 < 2)    # 4 是否小於 2 ?     -> False
print(4 <= 2)   # 4 是否小於等於 2 ? -> False


# 賦值運算子
num = 4

# 複合指定運算子
num = 4
num += 4      # num = num + 4 = 8
num -= 4      # num = num - 4 = 0
num *= 4      # num = num * 4 = 16
num /= 4      # num = num / 4 = 1
num //= 3     # num = num // 3 = 1
num %= 3      # num = num % 3 = 1
num **= 3     # num = num ** 3 = 64


# 邏輯運算子
print((3 <= 2) or (4 != 1))
# False or True = True
print((1 >= 1) and not (0 > 2))
# True and not False = True and True = True
print(not (2 == 0))
# not False = True
print((1 < 3) and (4 > 5))
# True and False = False