### loop


### for-loop
for i in range(101):
    print(i)
    print("SITCON")


### range
for i in range(1, 5, 2):
    print(i)
# output: 1 3

for i in range(5, 0, -1):
    print(i)
# output: 5 4 3 2 1


stmt = "Hello, I'm Lily"
for s in stmt.split():
    print(s)

stmt = "Hello, I'm Lily"
for s in ["Hello,", "I'm", "Lily"]:
    print(s)
# output: Hello,I'mLily

### while-loop
i = 0
while i <= 100:
    print(i)
    i += 1


### continue
for i in range(6):
    if i == 3:
        continue
    print(i)
# output 0 1 2 4 5


### break
for i in range(6):
    if i == 3:
        break
    print(i)
# output 0 1 2



