#in statement
#if, operator == 1 or operator == 2:

 #  and
 #weather = "cold"
#match weather
 #   case ("hot")
  #  print("cvvvv")
   # case_:
    #print("kdsiks")

#щвиткодія if else
#if something easy to do it is
#list змінний тип данних та і індексований. в кожного із елементів ми можемо достукатися через індекс
#як не змінні працюють інекс
#value_list = [1, 2, 3]

#value_list.append(4)
#print(value_list)
#copy
#append
#insert
#function can be used for every element
#    method would be working only with a specific element we will call it in




#string = non changable list = changable methods = functions but not all functions are methord
############## string methods ###############


# value_email = "email@gmail.com" when in some phones they put upper case, where as in computer is
#value_email = "Email@gmail.com"
# how to check values for upper cases
#"
#value_email = "email"
#value_upper = value_email.upper()
#value_lower = value_email.lower()
#print(value_upper)
#print(value_lower)


#value_name = "nick nick nick hdjjsns" #when user entered with lowercase and feedback needs to be done with first symbol, it will change
#only first character
#value_capital = value_name.capitalize()
#print(value_capital)

#print(value_name[0]) #print the charachter needed
#print(value_name[:]) # print all the object / same method as copy


#value_title = value_name.title() # each single first charachter of the word would be changed for the upper case
#print(value_title)

#value_name = "nick Nick"
#value_swap = value_name.swapcase()



#name with ' '
#value_name = "_____  Nick  ____"
#value_strip_1 = value_name.strip(" ")
#value_strip = value_name.strip("_").strip("ck")
#value_rstrip = value_name.rstrip("_")
#value_lstrip = value_name.lstrip("_")

#print(value_strip, value_rstrip, value_lstrip)





#how to check if the user enter only int so for e.g 12 not m12
# is at the begining of the method, they return us boolean meaning we are checking is that is true or false

#value_int = "12m"
#print(value_int.isdigit())

#if value_int.isdigit():
 #   value_int = float(value_int)

#print(value_int, type(value_int))

# with for we can split each object into indexes

#value_int = "12kfjff"
#new_val = ""

#for symb in value_int:
   #if symb.isdigit():
   # new_val += symb   # take out evrything that is not digits
    #if not symb.isdigit():  # take out all the digits but do not take out characters
     #   new_val += symb
 #   if symb.isalpha():
#        new_val += symb     # take out all the digits but do not take out characters

stack = [3, 4, 5]
stack.append(10)
stack.pop(0)
print(stack)

