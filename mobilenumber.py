'''
Author:Jacob Thomas
Date:29/11/2024
Description:Program to check whether the given number is a valid mobile number or not using functions.

Rules:

    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9
'''
def mobile_number(number):
    number_length=len(number)
    if number_length==10 and number[0] in "987":
        return True
n=str(input("Enter the number"))
if mobile_number(n):

    print("Valid")
else:
    print("Not valid")




