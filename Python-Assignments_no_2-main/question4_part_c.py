'''_____________________________________________________________________________________________________________________________________________________________________________________
                Question 4:  Generate 100 random numbers between 10 -90 and 
                                    a. Sort them in ascending order
                                    b. find all numbers grater than 40
                                    c. filter out numbers grater then 40 using continue statement
________________________________________________________________________________________________________________________________________________________________________________________'''

#______________________________Ascending order____________________________________

import random 
random_number_list = []
for count in range(1, 101):
    random_number_list.append(random.randint(10,90))
for i in range(len(random_number_list)):
    for j in range(i,len(random_number_list)):
        if random_number_list[i] >= random_number_list[j] :
            a = random_number_list[j]
            random_number_list[j] = random_number_list[i]
            random_number_list[i] = a
print("Random number list in ascending order:\n")
print(random_number_list,"\n")

#_____All numbers grater then 40 filtered out using continued statement___________

grater_than_40_filtered_out_list = []
for loop in random_number_list:
    if loop < 40:
        grater_than_40_filtered_out_list.append(loop)
    else:
        continue

print("list of numbers grater then 40:\n")
print(grater_than_40_filtered_out_list,'\n')