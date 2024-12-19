'''
Author:Jacob Thomas
Date:19/12/2024
'''
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Traversiong a 2D array row by row:")
for row in arr:
    for element in row:
        print(element,end=" ")
    print()


