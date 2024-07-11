# 7-loop.py


# for-loop
for i in range(101):
    print(i)

# range
for i in range(1, 5, 2):
    print(i)
# 1 3

for i in range(5, 0, -1):
    print(i)
# 5 4 3 2 1


# while-loop
i = 0
while i <= 100:
    print(i)
    i += 1


# continue
for i in range(6):
    if i == 3:
        continue
    print(i)
# output 0 1 2 4 5


# break
for i in range(6):
    if i == 3:
        break
    print(i)
# output 0 1 2



