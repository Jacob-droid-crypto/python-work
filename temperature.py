'''
Author
'''


temp1=int(input("Enter  the temperature"))
scale=input("Is this in (C)elsius or (F)aranheit ")
if scale=='C':
    f=(9/5*temp1)+32
    print(f)
    print(temp1,"Celsius is",f)
else:
    c=(5/9)*(temp1-32)
    print(c)
print(temp1,"faranheit is",c)