'''_______________________________________________________________________________________________________________________
                                        practicing Python variable types
   ______________________________________________________________________________________________________________________'''

# Variables are in simple terms memory locations
# Variable types : Integers numbers , String , Floating numbers
# Python has no command for declaring a variable. Because Pthon is a dynamic language, a variable is created the moment we
#  first assign a value to it using the Assignment Operator ' = '.
# Variables do not need to be declared with any particular type, and can change type after they have been set.


                # Rules for declaring variable names:
                # 1. Must starts with alphabet or _
                # 2. No spacing between variable names use _ instead of spacing
                # 3. Variable names are case sensitive so ' A ' and ' a ' are different variables
                # 4. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

'''
In programming, data type is an important concept.Variables can store data of different types, and different types can do 
different things.Python has the following data types built-in by default, in these categories:

Text Type:	      str
Numeric Types:	   int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	   dict
Set Types:	      set, frozenset
Boolean Type:	   bool
Binary Types:	   bytes, bytearray, memoryview
None Type:	      NoneType

'''

#_______________________Declaring integer variables_________________________________________________________________

number_1 = 10                                       # declaring integer  variables 
number_2 = 20 
print(f'Number_1: {number_1}')                      # displaying number_1 & number_2 
print(f'Number_2: {number_2}')

#----------------------------------------------------------------------------------------------------------------------
#---------------------------------------Math Operators-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------


addition = number_1 + number_2                      #  adding number_1 & number_2 
print(f"Sum: {addition}") 

product = number_1 * number_2                       #  product of number_1 & number_2 
print(f"product: {product}") 

division = number_1 /  number_2                     #  division of number_1 by number_2 
print(f"Division: {division}")

modulous = number_1 % number_2                      #  Mod of number_1 by number_2 
print(f"Mod: {modulous}") 

addition = number_1 + number_2                      #  average of number_1 & number_2 
print(f"Average: {addition/2}") 

number_1 += 15                                      #  increment number_1 by 5
print(f'Number_1 after increment: {number_1}') 

number_2 -= 35                                      #  decrementing number_2 by 35
print(f'Number_2 after decrement: {number_2}') 

number_1 *= 15                                      #  multiplying number_1 by 5 & storing the result in the number_1 variable
print(f'Number_1 after multiplication: {number_1}') 

number_2 /= 2                                      #   dividing number_2 by 2 & storing the result in the number_2 variable
print(f'Number_2 after division: {number_2}') 


#_______________________Declaring floating variables_________________________________________________________________

print("*"*35,'\n')

number_3 = 10.25                                    # declaring floating variables  
number_4 = 20.20 
print(f'Number_3: {number_3}')                      # displaying number_3 & number_4 
print(f'Number_4: {number_4}')

#----------------------------------------------------------------------------------------------------------------------
#---------------------------------------Math Operators-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

addition = number_3 + number_4                      #  adding number_3 & number_4
print(f"Sum: {addition}") 

product = number_3 * number_4                       #  product of number_3 & number_4 
print(f"product: {product}") 

division = number_1 /  number_2                     #  division of number_1 by number_2 
print(f"Division: {division}")

modulous = number_3 % number_4                      #  Mod of number_3 by number_4
print(f"Mod: {modulous}") 

addition = number_3 + number_4                      #  average of number_3 & number_4
print(f"Average: {addition/2}") 

number_3 += 15                                      #  increment number_3 by 4
print(f'Number_3 after increment: {number_3}') 

number_4 -= 35                                      #  decrementing number_4 by 35
print(f'Number_4 after decrement: {number_4}') 

number_3 *= 15                                      #  multiplying number_3 by 5 & storing the result in the number_3 variable
print(f'Number_3 after multiplication: {number_3}') 

number_4 /= 2                                      #   dividing number_4 by 2 & storing the result in the number_4 variable
print(f'Number_4 after division: {number_4}') 


#_______________________Declaring string variables___________________________________________________________________

string_1 = 'Ayesha'                                # declaring string variabels
string_2 = ' is a student'
print(string_1,string_2)

#----------------------------------------------------------------------------------------------------------------------
#---------------------------------------string concatenation-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

string_concatenation = string_1 + string_2
# print("concatenated text string:", string_concatenation)
print("Ayesha" + string_2)

#----------------------------------------------------------------------------------------------------------------------
#---------------------------------------Type casting-------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

'''
  To specify the data type of a variable, type casting can be used.
  There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an
  object-orientated language, and as such it uses classes to define data types, including its primitive types.
  Casting in python is therefore done using constructor functions:

   1.   int() -   constructs an integer number from an integer literal a float literal (by removing all decimals), or
                a string literal (providing the string represents a whole number)

   2.   float() - constructs a float number from an integer literal, a float literal or a string literal (providing the 
                string represents a float or an integer)

   3.   str() -   constructs a string from a wide variety of data types, including strings, integer literals and float 
                literals
'''

string_text = str(32156)                     # string_text will be '32156'
integer_number = int(3)                      # integer_number will be 3
floating_number = float(3)                   # floating_number will be 3.0
print(f'string text is: {string_text}, integer number is: {integer_number} and floating numver is: {floating_number}')


#----------------------------------------------------------------------------------------------------------------------
#---------------------------------------Type and length of variable----------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

print(f'Type if string_text variable is: {type(string_text)} and its length is: {len(string_text)}')

#   integer numbers and floating numbers gives error when len() function used

print(f'Type if integer_number variable is: {type(integer_number)} ')
print(f'Type if floating_number variable is: {type(floating_number)} ')


#----------------------------------------------------------------------------------------------------------------------
#-----------------------Adding Multiple values to multiple variabels on the same command line--------------------------
#----------------------------------------------------------------------------------------------------------------------

a, b, c = 1, "apple", 18.435
print(a)
print(b)
print(c)
print("-"*100)                                 # printing  ' - ' 100 times 

#----------------------------------------------------------------------------------------------------------------------
#-----------------------same values to multiple variabels on the same command line-------------------------------------
#----------------------------------------------------------------------------------------------------------------------

a = b = c = "apple"
print(a)
print(b)
print(c)
print("-"*100)                           

#----------------------------------------------------------------------------------------------------------------------
#-----------------------Aunpacking list elements to multiple variabels on the same command line------------------------
#----------------------------------------------------------------------------------------------------------------------

list_1 = [1, "apple", 18.435]
a, b, c = list_1
print(a)
print(b)
print(c)
print("-"*100)



#----------------------------------------------------------------------------------------------------------------------
#---------------------------------------Extra--------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
'''
              Multi Words Variable Names
Variable names with more than one word can be difficult to read. There are several techniques you can use to make them more 
readable:

        1.  Camel Case:  Each word, except the first, starts with a capital letter r.g

                             myVariableName = "John"
        
        2.  Pascal Case: Each word starts with a capital letter e.g 

                              MyVariableName = "John"
          
        3.  Snake Case:  Each word is separated by an underscore character e.g

                              my_variable_name = "John"

'''
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------