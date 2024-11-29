'''
Author:Jacob Thomas
Date:29/11/2024
Description:Program to find the factorial of a number using Recursion.
'''
def recursion_fac(n):
    if n==0:
        return 1
    else:
        return n*recursion_fac(n-1)
num=int(input("Enter the number"))
f= recursion_fac(num)
print(f)
