import keyword

num = int(input("Enter an integer: "))

while num > 9:
    mult = 1
    while num > 0:
        mult *= num % 10
        num //= 10
    num = mult
print(f"The result is {num}")









