import string, keyword

my_string = '_'
my_string = '__'
my_string = '___'
my_string = 'x'
my_string = 'get_value'
my_string = 'get value'
my_string = 'get!value'
my_string = 'some_super_puper_value'
my_string = 'Get_value'
my_string = 'get_Value'
my_string = 'getValue'
my_string = '3m'


result = True

if my_string[0].isdigit() or my_string in keyword.kwlist:
    result = False

elif my_string.count("_") == len(my_string) and len(my_string) > 1:
    result = False

else:
    for letter in my_string:
        if letter == "_":
            continue

        elif letter.isupper():
            result = False
            break

        elif (letter in string.punctuation or
              letter.isspace()):
            result = False
            break

print(result)


##################### second version ####################


#my_string = 'myString'
#result = False
#
#if my_string.isidentifier():
#    if my_string == "_" or my_string.islower():
#        result = True
#
#print(result)









#result = False

#if my_string.count("_") == len(my_string) and len(my_string) > 1:
 #   result = False


#if my_sting.isidentifier():
  #  if my_string == "_" or my_string.islower():
 #       result = True

#if my_string in keyword.kwlist:
 #   result = False


#print(result)





