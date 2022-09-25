'''_____________________________________________________________________________________________________________________________________________________________________
            Question 3:   Repeat task 2 for five users and print |Name | Percentage| in table form
   ____________________________________________________________________________________________________________________________________________________________________'''

dummy = True
subject_names = ['Maths', 'Physics', 'Chemistry', 'English', 'History']
Name_percentake = []
user = 1

while user < 6:
    
    while dummy:
            user_name = input("\n Please enter your full name:")
            if user_name.strip().isdigit():
                print("\n Please enter a valid name")
            else:
                dummy = False

    
    total_marks_obtained = 0
    i = 0

    while not(dummy):
            a = input(f"\n Please enter marks obtained in {subject_names[i]}:")

            if a.strip().isdigit():
                total_marks_obtained += float(a)
                i +=1
                if i == len(subject_names):
                        dummy = True
            else: 
                print("\n Please enter  valid subject marks")
    
            percentage = (total_marks_obtained*100)/(100*len(subject_names))
    Name_percentake.append([user_name, percentage])
    user +=1


from tabulate import tabulate                       # for printing in table form
print("-"*46 )      
print(tabulate(Name_percentake, headers = ['Student name','percentage']))
print("-"*46 )      
 
