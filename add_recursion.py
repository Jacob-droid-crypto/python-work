'''
Author:Jacob Thomas
Date:29/11/2024
Description:Recursive function to add two positive numbers
'''
def add_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return add_numbers(num1+1,num2-1)
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number:"))
add_numbers(num1,num2)
print("The sum of two numbers is:",add_numbers(num1,num2))