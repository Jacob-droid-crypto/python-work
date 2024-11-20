'''
Author:Jacob Thomas
Date:21/11/2024
Description: Print a Simple * Pattern
'''
row=int(input("Enter the number of rows"))
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end="")
    print('')