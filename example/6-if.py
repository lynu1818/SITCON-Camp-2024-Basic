# 6-if.py


# if
price = 50
if price < 100:
    print("Let's go have some ramen!")
# Let's go have some ramen!


# if-else
price = 150
if price < 100:
    print("Let's go have some ramen!")
else:
    print("I'm about to go bankrupt.")
# I'm about to go bankrupt.



price = 120
if price < 100:
    print("Let's go have some ramen!")
elif price < 150:
    print("Find some friends to hang out with!")
else:
    print("I'm about to go bankrupt.")
# Find some friends to hang out with!



price = 150
if price < 100:
    print("Let's go have some ramen!")
else:
    if price < 150:
        print("Find some friends to hang out with!")
    else:
        print("I'm about to go bankrupt.")
# I'm about to go bankrupt.


