# 4-datatype.py

# type()
print(type(20))     # <class ‘int’>
print(type(5.9))    # <class ‘float’>
print(type("Lily")) # <class ‘str’>
print(type(True))   # <class ‘bool’>


# escape sequence
print("Hello, I'm Lily.")           # Hello, I'm Lily.
print('He said, "Hi".')             # He said, "Hi".

print('Hello, I\'m Lily.')          # Hello, I'm Lily.
print("He said, \"Hi\".")           # He said, "Hi".

# raw string (補充)

print("He said, \"Hi\".")           # He said, "Hi".
print(r"He said, \"Hi\".")          # He said, \"Hi\".

# 常用 str 方法

# str.lower()
print("Hello, World!".lower())
# hello, world!

# str.upper()
print("Hello, World!".upper())
# HELLO, WORLD!

# str.split()
text = "Hello World"
words = text.split()
print(words)            
# ['Hello', 'World']
print(words[0])
# Hello
print(words[1])
# World

date = "2023-05-16"
parts = date.split('-')
print(parts)
# ['2023', '05', '16']
print(parts[1])
# 05

# str.strip()
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)
# Hello, World!

text = "###Hello, World!###"
stripped_text = text.strip('#')
print(stripped_text)
# Hello, World!




# type conversion


# 浮點數轉換為整數
a = 3.14
b = int(a)
print(b)        # 3
print(type(b))  # <class 'int'>


# 整數轉換為浮點數
a = 10
b = float(a)
print(b)        # 10.0
print(type(b))  # <class 'float'>


# 整數轉換為字串
a = 10
b = str(a)
print(b)        # '10'
print(type(b))  # <class 'str'>

# 整數轉換為布林
a = 0
b = bool(a)
print(b)        # False
print(type(b))  # <class 'bool'>


# 為什麼要有資料型態
print(0.1 + 0.1 + 0.1 == 0.3)
print(0.1 + 0.2)
# False