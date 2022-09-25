"""______________________________________________________________________________________________________________________________________________

            question 1:  take an input fite (.txt file), create and save a new file each time you encounter an new line in the text within 
________________________________________________________________________________________________________________________________________________"""

# path = "f:\\repo\\assignment\\question_1\\Lorem_ipsum.txt"     # absolute path

path = ".\question_1\Lorem_ipsum.txt"     # relative path

with open(path, "r") as file:
# with open("Lorem_ipsum.txt", "r") as file:             
    a = 0
    for i in file:
        if i != "\n":        
            f = open(f"file_{a}.txt","w")  
            f.write(i)
            f.close()
            a +=1 
    print("-"*100)