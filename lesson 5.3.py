import string

value_str = input("Enter the string:")
new_value = ""
value_title = value_str.title()
for symb in value_title:
    if not symb.isspace():
        new_value += symb

new_value = ""

for char in value_str:
    if char not in string.punctuation:
        new_value += char

print(("#") + new_value)


