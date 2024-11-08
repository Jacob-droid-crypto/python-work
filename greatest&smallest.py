'''
Author:Jacob Thomas
Date:08/11/2024
Description:A program that helps to find the largest and smallest of a given set of numbers
'''
limit=int(input("Enter the limit"))
number= int(input("Enter the  number"))
big=number
small=number
second_big=number
second_small = number
while limit>1:
    number=int(input("Enter the number"))
    if(number> big):
        second_big = big
        big=number
    elif(number>second_big):
        second_big=number
    elif(number<small):
        second_small = small
        small=number
    elif(number<second_small):
        second_small=number
    limit = limit - 1
print("The second largest number is:",second_big)
print("The second smallest number is:",second_small)






