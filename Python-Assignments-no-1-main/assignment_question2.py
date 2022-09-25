'''_____________________________________________________________________________________________________________________________________________________________________
            Question 2:   Take name and subject marks from a user and 
                            1. total marks obtained
                            2. percentage (each subject is worth 200 marks)
                            3. print it in a tabular form 
   ____________________________________________________________________________________________________________________________________________________________________'''

dummy = True
while dummy:
    user_name = input("\n Please entter your full name:")
    if user_name.strip().isdigit():
        print("\n Please enter a valid name")
    else:
        dummy = False

dummy = True
subject_names = ['Maths', 'Physics', 'Chemistry', 'English', 'History']
subject_marks = []
total_marks_obtained = 0
i = 0
while dummy:
    a = input(f"\n Please enter marks obtained in {subject_names[i]}:")

    if a.strip().isdigit():
        subject_marks = subject_marks+[float(a)]

        total_marks_obtained += subject_marks[i]
        i +=1
        if i == len(subject_names):
                dummy = False
    else: 
        print("\n Please enter  valid subject marks")
    
for_table = []
i = 1
j = 0
for x in subject_marks:
    subject_names.insert(i, x)
    subject_names.insert(i+1, x/2)
    for_table = for_table+[subject_names[j:i+2]]
    i += 3 
    j += 3

from tabulate import tabulate                       # for printing in table form

percentage = (total_marks_obtained*100)/(100*len(subject_marks))

print(f"{user_name} Result:" )      
print("-"*46 )      
print(tabulate(for_table, headers = ['subject name','obtained marks','percentage']))
print("-"*46 )      
print(f"Total"," "*15,"     ", total_marks_obtained ,"    ",percentage,"%")
