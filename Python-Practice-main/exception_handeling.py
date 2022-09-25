
'''_______________________________________________________________________________________________________________________
                                        Exception handeling
   ______________________________________________________________________________________________________________________'''

# # FileNotFoundError without exception handeling

# filename = input("What text file to open? ")
# with open(filename) as f:
#     print(f.read())
# #----------------------------------------------------------------------------------------------------------------------

# #FileNotFoundError with exception handeling
# try:
#     filename = input("What text file to open? ")
#     with open(filename) as f:
#         print(f.read())
# except FileNotFoundError:
#     print("Sorry, " + filename + " not found.")

# #----------------------------------------------------------------------------------------------------------------------


while True:
    idn = input("What is your ID number? ")
    try:
        n = int(idn)
    except ValueError:
        print(f"Please enter a number, not {idn}")
        continue
    if n in range(11):  # n in range(11): 0<= n <= 10
        print('Thank you, your ID number is ', n)
        break
    else:
        print('Bad value, try again')
        continue