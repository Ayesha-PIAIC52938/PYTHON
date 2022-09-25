'''_____________________________________________________________________________________________________________________________________________________________________________________
                Question 5: Generate 100 random numbers between 10-90 and find
                                a. sum
                                b. mean, median and mode
                                c.minimum and maximum value
 
________________________________________________________________________________________________________________________________________________________________________________________'''

#______________________________generating 100 random numbers b/w 10 - 90____________________________________
import random 
random_number_list = []
for count in range(1, 101):
    random_number_list.append(random.randint(10,90))

#______________________________Sorting them in ascending order______________________________________________

for i in range(len(random_number_list)):
    for j in range(i,len(random_number_list)):
        if random_number_list[i] >= random_number_list[j]:
            a = random_number_list[j]
            random_number_list[j] = random_number_list[i]
            random_number_list[i] = a
print("Random number list in ascending order:\n")
print(random_number_list,"\n")

#_______________moad, median and mean of 100 random numbers b/w 10 - 90________________________________________


#---------------------------Mean---------------------------------------------------
sum = 0
for i in random_number_list:
    sum = sum+i
print(f"Mean of 100 random numbers b/w (10-90): {sum/100}\n")

# ---------------------------Median-------------------------------------------------
a = len(random_number_list)//2
b = (len(random_number_list)//2)+1
c = (len(random_number_list)-1)//2
if len(random_number_list)%2 == 0:
    # print("random number list is of even length so median will be mean of the middle two elements:")
    median = (random_number_list[a] + random_number_list[b])/2
else:
    # print("random number list is of odd length so median will be the middle remaning element:")
    median = (random_number_list[c]) 
print(f"Median of 100 random numbers b/w (10-90): {random_number_list[a],random_number_list[b]}/2 = {median}\n")

# ----------------------------Mode---------------------------------------------------

count_list = []
for i in range(len(random_number_list)):
    if random_number_list[i] != random_number_list[i-1]:
        x = random_number_list.count(random_number_list[i])
        count_list.append([random_number_list[i] ,x])
print(f"[random number , times repeated]: {count_list}")

for i in range(len(count_list)):
    for j in range(i,len(count_list)):
        if count_list[i][1] >= count_list[j][1]:
            a = count_list[j]
            count_list[j] = count_list[i]
            count_list[i] = a
print(f"the numver {count_list[i][0]} repeats the most in 100 random numbers b/w (10-90): Mode {count_list[i][1]} \n")