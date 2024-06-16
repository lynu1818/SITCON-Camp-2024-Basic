### if-else statement


price = 150
if price < 100:
    print("Let's go to have some ramen!")
else:
    print("I'm about to go bankrupt")
# output: I'm about to go bankrupt.



price = 150
people = 1
if price < 100 and people >= 2:
    print("Let's go to have some ramen!")
else:
    print("Oh No :(")
# output: Oh No :(



price = 150
people = 1
if price > 100:
    print("Too expensive.")
elif people < 2:
    print("I don't want to have ramen alone QQ")
else:
    print("Let's go to have some ramen!")
# output: Too expensive.


price = 150
people = 1
if price < 100:
    if people >= 2:
        print("Let's go to have some ramen!")
    else:
        print("Find some friends to hang out with!")
else:
    print("I'm about to go bankrupt")
# output: Find some friends to hang out with!

