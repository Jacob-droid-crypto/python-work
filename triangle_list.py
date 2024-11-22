'''
Author:Jacob Thomas
Date:22/11/2024
Description:
'''

row1 = int(input("Enter the number:"))
#increasing triangle
for i in range(0,row1):
    for j in range(0,i+1):
        print("*",end="")
    print('')

#Decreasing triangle
row2=int(input("Enter the number of row:"))
for k in range(row2,0,-1):
    for l in range(k,0,-1):
        print("*",end="")
    print('')

#Hill pattern
row3=int(input("Enter the number of rows:"))
for m in range(1,row3+1):
    for n in range(row3-m):
        print(" ",end=" ")
    for o in range(2*m-1):
        print("*",end=" ")
    print('')
#Reverse Hill pattern
row4=int(input("Enter the number of rows:"))
for p in range(row4,0,-1):
    for q in range(row4-p,0,-1):
        print(" ",end=" ")
    for r in range(2*p-1,0,-1):
        print("*",end=" ")
    print('')
