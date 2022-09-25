'''_____________________________________________________________________________________________________________________________________________________________________________________
                Question 6: Ask users to provide 2 lists of fruits (same length). Compare the lists and see if it has common elements
________________________________________________________________________________________________________________________________________________________________________________________'''


fruits_list_1 = []
fruits_list_2 = []
similar_fruits_list = []

print("please seperate fruit names with comma "," \n")
for i in range(2):
    w,x,y,z = input(f"user {i} please enter any four fruit names:").split(",") 
    if i == 0:
        fruits_list_1 =[w,x,y,z]
    else:
        fruits_list_2 =[w,x,y,z]
print("-"*100)
print(fruits_list_1)
print(fruits_list_2)
print("-"*100)

for j in fruits_list_1:
    for k in fruits_list_2:
        if j==k:
            similar_fruits_list.append(j)
print(f"Similar fruits entered by both users: {similar_fruits_list}")
print("-"*100)

