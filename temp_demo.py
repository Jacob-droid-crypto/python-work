'''
Author:Jacob Thomas
Dare;'28/10/2024
Description:A menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
'''

while True:
    temp = int(input("Enter the temperature"))
    print("1.\t Convert Celsius to Fahreheit")
    print("2.\t Convert Fahrenheit to Celsius")
    print("3.\tExit the program")
    choice=int(input("Enter the choice"))
    if choice== 1:
        f = ((9 / 5) * temp) + 32
        print(f,"The given temperature  is coverted from Celsius to  Fahrenheit ")
    elif choice== 2:
        c = (5 / 9) * (temp - 32)
        print(c,"The given temperature is coverted from Fahrenheit to Celsius")
    elif choice== 3:
        break
    else:
        print("Invalid")




