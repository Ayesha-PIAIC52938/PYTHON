'''_______________________________________________________________________________________________________________________
                                        practicing Python print statement
   ______________________________________________________________________________________________________________________'''

print("Printing the string: Hello! World")                    # Printing a string:
print("printing numbers: ", 12345)                            # Printing Numbers and a string message
print(f'The number {2} comes after number {1}')               # f string in Python/ Literal string interpolation

#_______________________Print with white space characters_________________________________________________________________

print("Hello,",'',"my name is Sarah")                         # Printing space: ''
print("Hello,",'\t',"my name is Sarah")                       # Printing horizontal tab: '\t'
print("Hello,",'\n',"my name is Sarah")                       # Printing new line: '\n'
print("Hello,",'',"my name is Sarah" )                        # Printing space: ''

#_______________________Printing strings having double/single quotations within____________________________________________

#               RULE: Use single quotation if the string has double quotation and vice versa

print("it's a book")                                          # Printing strings having single quotations within
print('Ayesha said to tell you "OK"')                         # Printing strings having double quotations within

#_______________________Print tabels using tabulate & list______________________________________________________________________________

from tabulate import tabulate                                #importing tabulate() function from tabulate liberary

print(tabulate([["Ayesha", "6", "D", 50],["Amnaa", "2", "C", 90],["Saad", "11", "A", 99]], headers=["Name", "Class", "Section", "Percentage"]))