import csv
from csv import DictReader as DR
import re
header = ['Meeting_Id','Date of Meeting','Start Time','End Time','Participants Email']
with open('meeting_list.csv','w') as csvfile:
    data = csv.writer(csvfile,lineterminator='\n')
    data.writerow(header)
    csvfile.close()