main_value = None

result = 0

while True:
    number_1 = float(input("Enter your first number"))
    number_2 = float(input("Enter your second number"))
    operation = input("Enter a math operation  -, +, *, /:")

    if operation not in "+-/*" or len(operation) > 1:
        result = "ERROR invalid symbol"
    elif operation == '+':
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

    should_continue = input("Do you want to continue? Type 'y' for yes and 'n' for no: ")

    if should_continue.lower() in ['y', 'yes']:
        main_value = result
        continue
    else:
        print("Thank you for using my calculator!")
        break


