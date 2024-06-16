### loop


print(100)

### for-loop
for i in range(101):
    print(i)


### range
for i in range(1, 5, 2):
    print(i)
# output: 1 3

for i in range(5, 0, -1):
    print(i)
# output: 5 4 3 2 1

### while-loop
i = 0
while i <= 100:
    print(i)
    i += 1


### continue
for i in range(1, 5):
    if i % 2 == 0:
        continue
    print(i)
# output: 1 3


### break
for i in range(1, 5):
    if i >= 3:
        break
    print(i)
# output: 1 2




