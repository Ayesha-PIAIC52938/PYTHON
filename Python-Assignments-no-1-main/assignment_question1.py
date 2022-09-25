'''_____________________________________________________________________________________________________________________________________________________________________
            Question 1:    Take two numbers from a user and check if the numbers are even or odd
   _____________________________________________________________________________________________________________________________________________________________________'''


dummy = True
while dummy:

    number_1, number_2 = input("\n please enter two numbers seperated by space:").split()

    if number_1.strip().isdigit() and number_2.strip().isdigit():

        if int(number_1) % 2 == 0 and int(number_2) % 2 == 0 :
            print('\n Both numbers are even')

        elif int(number_1) % 2 == 0 and int(number_2) % 2 != 0:
            print('\n First number is even but second number is odd')

        elif int(number_1) % 2 != 0 and int(number_2) % 2 == 0:
            print('\n First number is odd but second number is even')      
        else:
            print('\n Both numbers are odd')
 
        dummy = False
    else:
        print("\n please enter numbers only")

print("_"*25,"end","_"*50)
