#Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014

from datetime import datetime



x = datetime(2024, 11, 12)

y = x.strftime("%m / %d / %Y ")

print("The examination will start from: ",y)