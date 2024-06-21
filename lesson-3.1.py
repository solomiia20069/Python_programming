number_1 = float(input("Enter your first number"))
number_2 = float(input("Enter your second number"))
operation = input("Enter a math operation  -, +, *, /:")

result = 0
if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    result = number_1 / number_2
else:
    print("Character inputted is not valid")

print(f"{number_1}{operation}{number_2}={result}")