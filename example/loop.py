### loop



### for-loop
for i in range(3):
    print(i)


### while-loop
i = 0
while i < 3:
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




