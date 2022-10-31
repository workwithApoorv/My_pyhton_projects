import csv
header=["Name","Email","Phone no.","Book SN","Cost per day","Days of Rent"]
with open("user.csv",'w') as user:
    data=csv.writer(user,lineterminator='\n')
    user_writer=data.writerow(header)
    user.close()