'''_____________________________________________________________________________________________________________________________________________________________________________________
                Question 5: Generate 100 random numbers between 10-90 and find
                                a. sum
                                b. mean, median and mod
                                c.minimum and maximum value
 
________________________________________________________________________________________________________________________________________________________________________________________'''

#______________________________generating 100 random numbers b/w 10 - 90____________________________________
import random 
random_number_list = []
for count in range(1, 101):
    random_number_list.append(random.randint(10,90))
print("Random number list:\n")
print(random_number_list,"\n")

#______________________________Sorting them in ascending order______________________________________________

for i in range(len(random_number_list)):
    for j in range(i,len(random_number_list)):
        if random_number_list[i] >= random_number_list[j] :
            a = random_number_list[j]
            random_number_list[j] = random_number_list[i]
            random_number_list[i] = a
print("Random number list in ascending order:\n")
print(random_number_list,"\n")

#_______________minimum and maximum of 100 random numbers b/w 10 - 90________________________________________
print(f"Minimum of random number list in ascending order:{random_number_list[0]}\n")
print(f"Maximum of random number list in ascending order:{random_number_list[-1]}\n")
