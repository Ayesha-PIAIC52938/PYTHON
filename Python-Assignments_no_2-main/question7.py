'''_____________________________________________________________________________________________________________________________________________________________________________________
                Question 7:  Generate a random number between 1-10 and make user guess the number (provide 3 chances only)
________________________________________________________________________________________________________________________________________________________________________________________'''

import random

rand_number = random.randint(1,10)
print("Guess the value of a random number 'X' between 1 to 10 you get 3 chances:\n")
for i in range(3):
    guess_number = int(input("Your guess: "))
    if guess_number==rand_number:
        print("Correct guess weldone")
    else:
        print("Sorry, guess again")
print("-"*100)
print(f"The number is {rand_number}")
print("Better luck next time ;)")
