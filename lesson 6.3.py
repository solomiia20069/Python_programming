import keyword

num = int(input("Enter an integer: "))

while num > 9:
    mult = 1
    while num > 0:
        mult *= num % 10
        num //= 10
    num = mult
print(f"The result is {num}")


#number = int(input(""))
#result = 1

#while > 9:
 #   for digit in str(number):
   #     result += int(digit)
 #   number = result
 ##   result = 1

#print(number)


#string
#result = eval("1+2")
#print(result)

number = int(input(""))

while number > 9:
    number = eval('*'.join(str(number)))
print(number)


