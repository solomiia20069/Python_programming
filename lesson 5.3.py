value_str = input("Enter the string:")
new_value = ""
value_title = value_str.title()
for symb in value_title:
    if not symb.isspace():
        new_value += symb


print(("#") + new_value)


