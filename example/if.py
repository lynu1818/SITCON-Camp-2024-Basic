### if-else statement


### example 1
number = 10
if number > 5:
  print("Number is greater than 5.")
# output: Number is greater than 5.


### example 2
number = 3
if number > 5:
    print("Number is greater than 5.")
else:
    print("Number is not greater than 5.")


### example 3
number = -2
if number > 0:
    print("Number is positive.")
elif number < 0:
    print("Number is negative.")
else:
    print("Number is zero.")


### example 4
if number > 0:
    if(number % 2 == 0):
        print("Number is positive and even.")
    else:
        print("Number is positive and odd.")
elif number < 0:
    if(number % 2 == 0):
        print("Number is negative and even.")
    else:
        print("Number is negative and odd.")
else:
    print("Number is zero.")