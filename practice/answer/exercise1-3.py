sec = int(input("Please input a number: "))
hour = sec // 3600
sec %= 3600
minute = sec // 60
sec %= 60
print(f"{hour} hour {minute} minute {sec} second")