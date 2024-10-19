'''
Author:Jacob Thomas
Date:19/10/2024
Description:Familiarize time and date in various formats
'''
from datetime import datetime
current=datetime.now( )  #datetime.now() returns the current date and time
#print(current)
format_1=(current.strftime("%Y-%m-%d %H:%M:%S"))
print(format_1)