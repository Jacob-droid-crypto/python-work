'''
Author:Jacob Thomas
Date;21/11/2024
Description : : How to loop through a list and find the largest element.
► Instructions:
► Create a list of numbers: [12, 75, 34, 99, 45, 67].
► Write a loop to find the largest number in the list.
► Print the largest number.
'''
numbers=[12,75,34,99,45,67]
largest=numbers[0]
for num in numbers:
    if num > largest:
        largest=num
print("The largest number is ",largest)