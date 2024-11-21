'''
Author;Jacob Thomas
Date:21/11/2024
Description:
'''
list1=[11,12,15,84,99,75,44]
list2=[32,98,46,25,75,13]
combined_list=list1+list2
even_num=[]
odd_num=[]
for i in combined_list:
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
new_list=even_num+odd_num
print(new_list)

