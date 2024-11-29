'''
Author:Jacob Thomas
Date:29/11/2024
Description:A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.
'''
def right_triangle(sides):
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        return True
    return False

sides=[]
sides.append(int(input("Enter side 1: ")))
sides.append(int(input("Enter side 2: ")))
sides.append(int(input("Enter side 3: ")))
if right_triangle(sides):
    print("The given sides are part of a right triangle")
else:
    print("Not a right triangle")

