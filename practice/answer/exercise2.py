# nested
year = int(input("Please input a year: "))
if year % 4 != 0:
    print("It's not a leap year")
else:
    if year % 100 != 0:
        print("It's a leap year")
    else:
        if year % 400 != 0:
            print("It's not a leap year")
        else:
            print("It's a leap year")


# flat
year = int(input("Please input a year: "))
if year % 4 != 0:
    print("It's not a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("It's a leap year.")
elif year % 100 == 0 and year % 400 != 0:
    print("It's not a leap year.")
else:
    print("It's a leap year.")


# flat
year = int(input("Please input a year: "))
if year % 4 != 0:
    print("It's not a leap year.")
elif year % 100 != 0:
    print("It's a leap year.")
elif year % 400 != 0:
    print("It's not a leap year.")
else:
    print("It's a leap year.")