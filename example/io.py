### io

print(123)                      # 123
print("Hello, World!")          # Hello, World!
print("Hello", "World", 123)    # Hello World 123
print(1+2+3)                    # 6


## escape sequence
print("Hello, I'm Lily")        # Hello, I'm Lily
print('Hello, I\'m Lily')       # Hello, I'm Lily

print('"Hi," he said.')         # "Hi," he said.
print("\"Hi,\" he said.")       # "Hi," he said.

print("tonkotsu", "miso", "shoyu", sep="/")
# output: tonkotsu/miso/shoyu

print("Hello", "World")
# output: Hello World



## input
# version 1
print("What's your name?")
name = input()
print("Hello, ", name)

# version 2 - 合併的寫法
name = input("What's your name?")
print("Hello, ", name)
