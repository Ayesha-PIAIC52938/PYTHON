'''_______________________________________________________________________________________________________________________
                                        Practicing Python input() function
   ______________________________________________________________________________________________________________________'''


'''_______________________Take user's name and age as input and print it______________________________________________________________________________________________________________________'''

# user_name = input('Please enter your name: ')
# user_age = input('Please enter your age: ')
# print(f"User's name is {user_name} and his/her age is {user_age}")
# print('_'*100)

'''_______________________Take user's name and age as input. Add 5 to user's age and print it_________________________________________________________________________________________________'''

# user_name = input('Please enter your name: ')
# user_age = int( input('Please enter your age: ') )           #default value the input function retreive from user is of string type. age is a number so it must be an integer
# user_age += 5
# print(f"User's name is {user_name} and his/her age is {user_age}")
# print('_'*100)

'''_______________________Take user's name and age as input.Make sure user enter string ofr name and number for age and print it________________________________________________________________'''

# name_check_iterator = True
# while name_check_iterator:                                    # while loops until it encounters Strings is name and we set name_check_iterator to False 
#     user_name = input('Please enter your name: ')
#     if user_name.strip().isdigit():                         #.strip() removes starting and ending spaces from user_name and .isdigit() check if the value of user_name is string or number
#         print("Please enter a valid name")              
#     else:
#         name_check_iterator = False                          # else execuites iff user_name holds a string


# age_check_iterator = True
# while age_check_iterator:                                    
#     user_age = input('Please enter your age: ')
#     if user_age.strip().isdigit():                          
#         user_age = int(user_age)
#         age_check_iterator = False                                  
#     else:
#         print("Please enter valid age") 

# print(f"User's name is {user_name} and his/her age is {user_age}")
# print('_'*100)

'''_____________________Take 3 inputs from a userin one go and print it__________________________________________________________________________________________________________________'''


x,y,z = input("Please enter any three words:").split()                          # default seperator is space
print(f"first word is {x}, second word is {y} and third word is {z}")
print("-"*100)