'''_____________________________________________________________________________________________________________________________________________________________________________________
                Question 7:  Type a code that prints the following outputs:

                    
                    a.  1 2 3 4 5 6 7      
                        1 2 3 4 5 6
                        1 2 3 4 5
                        1 2 3 4
                        1 2 3
                        1 2
                        1
                                                                                  spaces
                    b.            5                                            8     0     8
                                4   4                                          6     3     6
                              3       3                                        4     7     4
                            2           2                                      2     11    2
                          1               1                                    0     15    0
                            2           2                                      2     11    2
                              3       3                                        4     7     4
                                4   4                                          6     3     6
                                  5                                            8     0     8 
________________________________________________________________________________________________________________________________________________________________________________________'''

a = 8
for i in range(7):
    for j in range(1,a):
        print(j, end=" ")
    print(" ")
    a = a-1    


b = 5
bb=1
no_of_spaces = 8

for i in range(10):
  if i<1 and i<5 :
    print(" "*no_of_spaces,b)
    no_of_spaces-=2
    b-=1
  if i>1 and i<5 :
    print(" "*no_of_spaces,b," "*bb,b)
    no_of_spaces-=2
    bb = bb+4
    b-=1
  if i==5: 
    no_of_spaces+=2
    bb = bb-4
    b+=1
  if i>5 and i<8:
    no_of_spaces+=2
    bb = bb-4
    b+=1
    print(" "*no_of_spaces,b," "*bb,b)
  if i==8:
    no_of_spaces+=2
    b+=1
    print(" "*no_of_spaces,b)
    
   