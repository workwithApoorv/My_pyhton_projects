import csv
from csv import DictReader as DR
import re
header = ['Contact_ID','Name','Phone_Number','Email','City']
with open('contact_list.csv','w') as fh:
    data = csv.writer(fh,lineterminator='\n')
    data.writerow(header)
    fh.close()