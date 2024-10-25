'''
Author: Jacob Thomas
Date; 25/10/2024
Description; Checking Whether a number is armstrong or not using python program
'''
number=int(input("Enter a number"))
sum=0
while  number>0 :
    number=number%10
    sum= sum+number^3
    number=number//10
if sum==number:
    print("Armstrog")
else:
    print('Not Armstrong')