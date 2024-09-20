# ##Create a dictionary where the keys are student names and the values are their grades. For example:
# #python
# grades = {"Alice":85,"Bob":90,"Charlie":78}
# print(grades ["Bob"])

##
##Add and Remove Key-Value Pairs:Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary.


# grades = {"Alice":85,"Bob":90,"Charlie":78}
# grades["David"] = 92
# print(grades)
# del grades["Charlie"]
# print(grades)

##Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

# grades = {"Alice":85,"Bob":90,"Charlie":78}
# grades["Bob"]= 95
# print(grades)

##Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
for key,values in students.items():
print(key,value)