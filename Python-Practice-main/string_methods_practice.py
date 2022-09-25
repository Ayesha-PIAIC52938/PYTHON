'''_______________________________________________________________________________________________________________________
                                        More about strings and string methods
   ______________________________________________________________________________________________________________________'''

#---------------------------------------------All String Methods-------------------------------------------------------                 
'''
Method	                Description

capitalize()	        Converts the first character to upper case

casefold()	            Converts string into lower case

center()	            Returns a centered string

count()	                Returns the number of times a specified value occurs in a string

encode()	            Returns an encoded version of the string

endswith()	            Returns true if the string ends with the specified value

expandtabs()	        Sets the tab size of the string

find()              	Searches the string for a specified value and returns the position of where it was found

format()	            Formats specified values in a string

format_map()	        Formats specified values in a string

index()	                Searches the string for a specified value and returns the position of where it was found

isalnum()	            Returns True if all characters in the string are alphanumeric

isalpha()	            Returns True if all characters in the string are in the alphabet

isdecimal()	            Returns True if all characters in the string are decimals

isdigit()	            Returns True if all characters in the string are digits

isidentifier()	        Returns True if the string is an identifier

islower()	            Returns True if all characters in the string are lower case

isnumeric()         	Returns True if all characters in the string are numeric

isprintable()	        Returns True if all characters in the string are printable

isspace()	            Returns True if all characters in the string are whitespaces

istitle()	            Returns True if the string follows the rules of a title

isupper()           	Returns True if all characters in the string are upper case

join()	                Joins the elements of an iterable to the end of the string

ljust()             	Returns a left justified version of the string

lower()	                Converts a string into lower case

lstrip()	            Returns a left trim version of the string

maketrans()	            Returns a translation table to be used in translations

partition()	            Returns a tuple where the string is parted into three parts

replace()	            Returns a string where a specified value is replaced with a specified value

rfind()	                Searches the string for a specified value and returns the last position of where it was found

rindex()	            Searches the string for a specified value and returns the last position of where it was found

rjust()	                Returns a right justified version of the string

rpartition()	        Returns a tuple where the string is parted into three parts

rsplit()	            Splits the string at the specified separator, and returns a list

rstrip()	            Returns a right trim version of the string

split()	                Splits the string at the specified separator, and returns a list

splitlines()        	Splits the string at line breaks and returns a list

startswith()	        Returns true if the string starts with the specified value

strip()	                Returns a trimmed version of the string

swapcase()	            Swaps cases, lower case becomes upper case and vice versa

title()	                Converts the first character of each word to upper case

translate()	            Returns a translated string

upper()	                Converts a string into upper case

zfill()	                Fills the string with a specified number of 0 values at the beginning

'''
#----------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------
#----------------------------------Multiline strings-------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# We can assign a multiline string to a variable by using three single or double quotes
print('Multiline strings')
print('')

# Using single quotes:
print('Multiline strings using 3 single quotes')
print('')

string_text = ''' My name is Ayesha.
I live in Pakistan.
sI love programming and
currently I am learning Python Dynamic Language.'''
print("-"*100)
print(string_text)

#  Using double quotes:
print('Multiline strings using 3 double quotes')
print('')

string_text = """ My name is Ayesha.
I live in Pakistan.
sI love programming and
currently I am learning Python Dynamic Language."""
print(string_text)
print("-"*100)



#----------------------------------------------------------------------------------------------------------------------
#-----------------------------Strings are Array------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# Strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print('Accessing strings chaacters of:',a)
print('')

print(f'string length: {len(a)} indexed from 0 - 12')
print(a[0])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[11])
print(a[12])
print("-"*100)

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------Checking Strings for words/characters----------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

print('Checking Strings for words/characters')
print('')

# if present in a string 

print('words/characters present in a string ')
print('')

txt = "The best things in life are free!"
print("free" in txt)                        # in checks "free" in the txt string variable and print True if free is present otherwise prints False
print("Free" in txt)
print("-"*100)

# if not present in a string 
print('words/characters not present in a string ')
print('')

txt = "The best things in life are free!"
print("free" not in txt)                        # in checks "free" in the txt string variable and print True if free is not present otherwise prints False
print("Free" not in txt)
print("-"*100)


#----------------------------------------------------------------------------------------------------------------------
#-----------------------------Slicing Strings--------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
print('Slicing Strings')
print('')

a = "Hello, World!"
print(f'string length: {len(a)} indexed from 0 - 12')

#   slicing from start to some index:-
print('from start to some index')
print('')

print(a[:5])               # prints characters from indes 0 to index 5 not including index five element (thats why ',' not printed)

#   slicing from some index till end:-
print('from some index till end')
print('')

print(a[5:])               # prints characters from index 5 to end of characters in dtring variable 'a'

#   slicing from some starting index till some end index:-
print('from some start index to some enfing index')
print('')

print(a[6:13])               # prints characters from index 5 to end of characters in dtring variable 'a'

print("-"*100)


#----------------------------------------------------------------------------------------------------------------------
#-----------------------------String Modification--------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

print('String Modification')
print('')

a = "Hello, WoRld!"

# upper case using upper() string method
print('Upper case')
print('')

print(a.upper())

# lower csce using lower() string method
print('Lower case')
print('')
print(a.lower())

# title  using title() string method
print('Title')
print('')
print(a.title())
print("-"*100)

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------removing white spaces in a String variable-----------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

#  he strip() method removes any whitespace from the beginning or the end of string:

a = "   Hello, WoRld!   "
print('removing white spaces in a String variable')
print('')

print(a)
print(a.strip()) 
print("-"*100)

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------Replacing characters/words in a String variable------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# The replace() method replaces a string with another string:
print('Replacing characters/words in a String variable')
print('')

a = "Hello, World!"
print(a.replace("H", "J"))

print(a.replace("Hello", "Fello"))
print("-"*100)

#----------------------------------------------------------------------------------------------------------------------
#-----------------------------splitting a String variable into list of elements----------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# The split() method returns a list where the text between the specified separator becomes the list items.

a ="hello, Fello  jolly world "
print('splitting a String variable into list of elements')
print('')

print('splitting a String wtih default seperator being space')
print(a.split())                  # The split(seperator) method splits the string into substrings if it finds instances of the separator. Default seperator being space
print('splitting a String wtih default seperator being ,')

print(a.split(','))   
print("-"*100)


#----------------------------------------------------------------------------------------------------------------------
#-----------------------------String format method---------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# String cannot be combined with numbers but we can combine strings and numbers by using the format() method
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are

print('inserting numbers into a strings')
print('')


age = 28
txt = "My name is Ayesha, and I am {}"
print(txt.format(age))
print('')
# The format() method takes multiple arguments, and  place them into their respective placeholders
print('inserting multiple numbers into a strings')

quantity = 3
item_no = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, item_no, price))
print('')

#  To be sure the arguments are placed in the correct placeholdersou we can use index numbers {0} 
print('inserting multiple numbers into a strings using indexing')
quantity = 3                   # {0}
itemno = 567                  # {1}
price = 49.95                  # {2}  
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("-"*100)


#----------------------------------------------------------------------------------------------------------------------
#-----------------------------Escape Characters------------------------------------------------------------------------
'''
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\xhh	Hex value

'''
#----------------------------------------------------------------------------------------------------------------------

#  To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
