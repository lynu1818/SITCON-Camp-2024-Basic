print("Please enter three coefficient of the quadratic equation ax^2 + bx + c = 0")
a = int(input())
b = int(input())
c = int(input())
delta = b**2 - 4 * a * c
sol1 = (-b + delta**0.5) / (2 * a)
sol2 = (-b - delta**0.5) / (2 * a)
print(f"two root: {sol1}, {sol2}")