'''
Author:Jacob Thomas
Date:19/10/2024
Description: Python program  that helps tomCreate, concatenate, and print a string and access a sub-string from a given string.
'''

first_name=input("Enter your First Name")
last_name=input("Enter your Last  Name")
name=first_name+" "+  last_name
print(name)
first_name_length=len(first_name)
print(first_name_length)
extracted_first_name= name[first_name_length:]
print(extracted_first_name)