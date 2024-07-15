# exercise4

while True:
    user_input = input("Please input a number or type 'exit' to leave: ")
    sum_digits = 0
    product = 1
    if(user_input == 'exit'):
        break
    else:
        num = int(user_input)
        while(num):
            last_digit = num % 10
            sum_digits += last_digit
            product *= last_digit
            num //= 10

        print(f"The result of the product minus the sum of the digits is: {product - sum_digits}")