'''
Author:Jacob Thomas
Date;21/11/2024
Description: Remove duplicate elements from a list using a loop or set.
► Approach:
► Create an empty list to store unique elements.
► Loop through the original list, and for each element, check if it is already in the new
list.
► If the element is not in the new list, add it.
'''
list1=[15,66,87,455,99,15,95,78,87]
unique_element=[]
for i in list1:
    if i not in unique_element:
        unique_element.append(i)

print( "list without duplicates",unique_element)
