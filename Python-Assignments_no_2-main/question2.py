'''_____________________________________________________________________________________________________________________________________________________________________________________
                Question 2:  Take a number from user and print a table from 1-10 using loops
________________________________________________________________________________________________________________________________________________________________________________________'''


flag = True
while flag :
    number = input("Please enter any number: ")
    if number.strip().isdigit():
        print(f"Number: {number}")
        flag = False
    else:
        print("Please enter a valid number")

number=int(number)
for i in range(1,11):
    print(f'{number} X {i} = {number * i}')