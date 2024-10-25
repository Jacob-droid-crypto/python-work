'''
Author; Jacob Thomas
Date:25/10/2024
Description:
'''
number=int(input("Enter a number"))
sum_of_digits=0
while number>0:
    remainder=number%10
    sum_of_digits = sum_of_digits+remainder
    number =number//10
print("sum of the given number is :", sum_of_digits)
