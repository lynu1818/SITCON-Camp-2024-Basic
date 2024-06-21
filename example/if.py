### if-else statement


price = 150
if price < 100:
    print("Let's go have some ramen!")
else:
    print("I'm about to go bankrupt.")
# output: I'm about to go bankrupt.



price = 150
location = "Hsinchu"
if price < 100 and location == "Hsinchu":
    print("Let's go have some ramen!")
else:
    print("Oh No :(")
# output: Oh No :(



price = 150
if price < 100:
    print("Let's go have some ramen!")
elif price < 150:
    print("Find some friends to hang out with!")
else:
    print("I'm about to go bankrupt.")
# output: I'm about to go bankrupt.



price = 150
if price < 100:
    print("Let's go have some ramen!")
else:
    if price < 150:
        print("Find some friends to hang out with!")
    else:
        print("I'm about to go bankrupt.")
# output: I'm about to go bankrupt.


