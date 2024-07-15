# exercise1

num = int(input("Please input a 3-digit number: "))


hundreds = num // 100
tens = num % 100 // 10
ones = num % 10
product = hundreds * tens * ones
sum_digits = hundreds + tens + ones
print(f"The result of the product minus the sum of the digits is: {product - sum_digits}.")