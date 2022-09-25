'''_______________________________________________________________________________________________________________________
                                        writing to / reading from json file
   ______________________________________________________________________________________________________________________'''

import json

# #--------------------------------------writing to json file/ creating a json sile-------------------------------------

  
# data = {
#     "name": "Ayesha Ayub",
#     "place": "Islamabad",
#     "skills": [
#         "Python",
#         "C++",
#         "Adobe Photoshop"
#         "Adobe Illustrator"
#         "Adobe Premere Pro"
#         "Clip studio paint"
#     ],
#     "email": "xyz@gmail.com",
# }
# # # path = "F:\\repo\\Python-Practice\\json_practice\\third_json_file.json"     # absolte path#

# path = "./json_practice/third_json_file.json"     # relative path

# with open( path , "w" ) as write:                         # for append mode just erite "a" instead of "w"
#     json.dump( data , write )  

# #----------------------------------------------------------------------------------------------------------------------


# sample_dictionary = {"first_name": "John", "last_name": "Doe", "Age": 34}

# # path = "F:\\repo\\Python-Practice\\json_practice\\secondk_json_file.json"     # absolte path#

# path = "./json_practice/second_json_file.json"     # relative path

# with open(path,"w") as file:
#    json.dump(sample_dictionary,file)

# #----------------------------------------------------------------------------------------------------------------------

# employees = [{"first_name": "John", "last_name": "Doe", "Age": 34},                    #   list of dictionaries
#             {"first_name": "Anna", "last_name": "Smith", "Age": 24},
#             {"first_name": "Sam", "last_name": "Smith", "Age": 44}
#             ]

# # path = "F:\\repo\\Python-Practice\\json_practice\\employees_file.json"     # absolte path#

# path = "./json_practice/employees_file.json"     # relative path

# with open(path,"w") as file:
#    json.dump(employees,file)

# #----------------------------------------------------------------------------------------------------------------------


#--------------------------------------Retreaving from a json sile-------------------------------------

# # path = "F:\\repo\\Python-Practice\\json_practice\\first_json_file.json"     # absolte path

# path = "./json_practice/first_json_file.json"     # relative path

# with open(path,"r") as file:
#    sample_list = json.load(file)
# print(sample_list)
# #----------------------------------------------------------------------------------------------------------------------

# # path = "F:\\repo\\Python-Practice\\json_practice\\secondk_json_file.json"     # absolte path#

# path = "./json_practice/second_json_file.json"     # relative path

# with open(path,"r") as file:
#    sample_dictionary = json.load(file)
# print(sample_dictionary)

# #----------------------------------------------------------------------------------------------------------------------

# # path = "F:\\repo\\Python-Practice\\json_practice\\employees_file.json"     # absolte path#

# path = "./json_practice/employees_file.json"     # relative path

# with open(path,"r") as file:
#    employees = json.load(file)
# print(employees)


#----------------------------------------------------------------------------------------------------------------------

# # path = "F:\\repo\\Python-Practice\\json_practice\\third_json_file.json"     # absolte path#

path = "./json_practice/third_json_file.json"     # relative path

with open( path , "r" ) as write:
   data =  json.load( write ) 

print(data)

#----------------------------------------------------------------------------------------------------------------------

