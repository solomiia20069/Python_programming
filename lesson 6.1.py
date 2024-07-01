#import string

#result = string.ascii_letters
#user_input = input("enter the two extream letters:")
#rem_hyphen = user_input.strip("-")
#ins_letters = rem_hyphen.
#print(rem_hyphen)



#def splitString(string):
 #   string = input("enter the two extream letters:")
  #  splt_input = string.split('-')
#
 #   return splt_input
#

import string

input_str = input("Enter two letters separated by hyphen: ")

first_input, second_input = input_str.split('-')
all_letters = string.ascii_letters

start_index = all_letters.index(first_input)
end_index = all_letters.index(second_input)

result = all_letters[start_index:end_index + 1]
print("Characters between:", result)







#letters = input("enter the diaposon of charachters to be filled:")
#remove_from_letters = letters.replace("-", )
#
#fill_letters = string.ascii_letters()

#ord()

#print(fill_letters)




