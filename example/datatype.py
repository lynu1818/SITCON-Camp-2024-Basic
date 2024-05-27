### datatype

# int
age = 20
print(age)       # 20
print(type(age)) # <class ‘int’>

# float
height = 5.9
print(height)       # 5.9
print(type(height)) # <class ‘float’>

# str
name = "Lily"     # 必須用雙引號或單引號包起來
print(name)       # ’Lily’
print(type(name)) # <class ‘str’>

# bool
is_student = True
print(is_student)       # True
print(type(is_student)) # <class ‘bool’>


### 常用 str 方法

# str.lower()
text = "Hello, World!"
lower_text = text.lower()
print(lower_text)       # 輸出: hello, world!

# str.upper()
text = "Hello, World!"
upper_text = text.upper()
print(upper_text)       # 輸出: HELLO, WORLD!

# str.split()
text = "Hello, World! Welcome to Python."
words = text.split()
print(words)            
# 輸出: ['Hello,', 'World!', 'Welcome', 'to', 'Python.']

date = "2023-05-16"
parts = date.split('-')
print(parts)
# 輸出: ['2023', '05', '16']


# str.strip()
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)
# 輸出: "Hello, World!"

text = "###Hello, World!###"
stripped_text = text.strip('#')
print(stripped_text)
# 輸出: "Hello, World!"


### f-string

name = "Lily"
message = f"My name is {name} and I am {19+1} years old."
print(message)
# 輸出: My name is Lily and I am 20 years old.


### raw string

path = r"C:\Users\Alice\Documents\file.txt"
print(path)
# 輸出: C:\Users\Alice\Documents\file.txt


### type conversion

x = 10               # int
y = 3.14             # float
result = x + y       # 隱式轉換
print(result)        # 13.14
print(type(result))  # <class 'float'>


# 浮點數轉換為整數
a = 3.14
b = int(a)      # 顯式轉換
print(b)        # 3
print(type(b))  # <class 'int'>


# 整數轉換為浮點數
a = 10
b = float(a)    # 顯式轉換
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