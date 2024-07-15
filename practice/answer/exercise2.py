# exercise2

num = int(input("Please input a 3-digit number: "))

if 100 < num <= 999:
    hundreds = num // 100
    tens = num % 100 // 10
    ones = num % 10
    product = hundreds * tens * ones
    sum_digits = hundreds + tens + ones
    print(f"The result of the product minus the sum of the digits is: {product - sum_digits}.")
elif num < 100:
    print(f'Number of digits is less than 3.')
else:
    print(f'Number of digit is greater than 3.')