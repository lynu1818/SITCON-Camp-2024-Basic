# exercise3-4 質數判斷

n = int(input("Please input a number: "))
is_prime = True
for i in range(2, int(n**(0.5)+1)):
    if n % i == 0:
        print(f"{n} is not a prime")
        is_prime = False
        break
if is_prime:
    print(f"{n} is a prime")