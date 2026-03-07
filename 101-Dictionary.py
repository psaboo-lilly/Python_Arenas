'''
Created on: 08-Mar-2026
Author: @parth

#1. ENUMERATE funtionality
#2. Grouping and Sorting Dictionary
#3. Usage of ItemGetter method from Operator library
'''

import operator

def key_val(school):
    print("<----Exploring ENUMERATE() func---->\n")
    for key, val in enumerate(school):
        print(f"Key-{key} & F_Name- {val[1]} & Age - {val[2]}")

def dict_operations(school):
    print("\n<----#Grouping the students based on AGE---->\n")
    age_dict = {}
    for student in school:
        age = student[2]
        if age in age_dict:
            age_dict[age]+= 1
        else:
            age_dict[age] = 1
    print(age_dict,"\n")
    return age_dict
    
def sort_dict(age_dict):
    print("<----Sorting the Dictionary based on Key or Value pairs---->\n")
    
    sort_age = sorted(age_dict.items())
    sort_age_desc = sorted(age_dict.items(), reverse = True)
    print(f"Sorted based on Age in Asending Order-> {sort_age}")
    print(f"Sorted based on Age in Descending order -> {sort_age_desc}\n")
    
    sort_student = sorted(age_dict.items(), key=operator.itemgetter(1))
    sort_student_desc = sorted(age_dict.items(), key=operator.itemgetter(1), reverse=True)
    print(f"Sorted based on #students in Ascending Order-> {sort_student}")
    print(f"Sorted based on #students in Descending Order-> {sort_student_desc}")
    
    
        
if __name__ == '__main__':
    school = [
        ['Mike', 'Thomson', '20', 'M'], 
        ['Robert', 'Bustle', '32', 'M'], 
        ['Andria', 'Bustle', '30', 'F'], 
        ['Andria', 'Ble', '20', 'F'], 
        ['Randria', 'Hustle', '32', 'F']
    ]
    
    #For understanding ENUMERATE() - use it when INDEX-Value pair is required from dict
    key_val(school)
    
    #Grouping the students based on AGE
    age_dict = dict_operations(school)
    
    #Sorting the Dictionary based on Key or Value pairs
    sort_dict(age_dict)
