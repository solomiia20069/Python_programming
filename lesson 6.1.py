import string

input_str = input("Enter the diaposon of charachters to be filled:")

first_input, second_input = input_str.split('-')
fill_letters = string.ascii_letters

start_index = fill_letters.index(first_input)
end_index = fill_letters.index(second_input)

result = fill_letters[start_index:end_index + 1]
print("Characters between:", result)


##################second version of the program ##############

input_str = input("").split("-")

beginning = string.ascii_letters.find(input_str[0])
ending = string.ascii_letters.find(input_str[-1])

if beginning == 1 or ending == -1:
    print("error")
else:
    print(string.ascii_letters[beginning:ending + 1])



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

#letters = input("enter the diaposon of charachters to be filled:")
#remove_from_letters = letters.replace("-", )
#
#fill_letters = string.ascii_letters()


#print(fill_letters)




