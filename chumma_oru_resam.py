'''
Author:Jacob Thomas
Date:29/11/2024
Description:Recursive function to multiply two positive numbers
'''
def multiply_num(num1,num2):
    if num2==1:
        return num1
    else:
        return  num1+multiply_num(num1,num2-1)
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number:"))
print("The product  of two numbers is:",multiply_num(num1,num2))




