# exercise3

num = int(input("Please input a number: "))
sum_digits = 0
product = 1

while(num):
    last_digit = num % 10
    sum_digits += last_digit
    product *= last_digit
    num //= 10

print(f"The result of the product minus the sum of the digits is: {product - sum_digits}")
