import csv
from csv import DictReader as DR
import re
header = ["rakesh@python.com","apoorv@python.com"]
with open('participant_list.csv','w') as csvfile:
    data = csv.writer(csvfile,lineterminator='\n')
    data.writerow(header)
    csvfile.close()