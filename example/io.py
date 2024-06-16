### io

print(123)                      # 123
print("Hello, World!")          # Hello, World!
print('Hello, World!')          # Hello, World!
print("Hello", "World", 123)    # HelloWorld123
print(1+2+3)                    # 6
print("Hello" + "World")        # HelloWorld
print(abc)                      # NameError

## escape sequence
print("Hello, I'm Lily")        # Hello, I'm Lily
print('Hello, I\'m Lily')       # Hello, I'm Lily

print("Hello", "World", sep="---")
# output: Hello---World

print("Hello", "World", end="!")
# output: HelloWorld!



## input
# version 1
print("What's your name?")
name = input()
print("Hello, ", name)

# version 2 - 合併的寫法
name = input("What's your name?")
print("Hello, ", name)
