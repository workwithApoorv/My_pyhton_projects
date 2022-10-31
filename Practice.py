import csv 

input_name = 'Adam Loewen'

output_name = 'Ram'

with open('sample2.csv') as file:
    file_handler = csv.reader(file)
    file_rows = list(file_handler)
#     print(file_handler)
    for row in file_rows:
        if row[0] == input_name:
            row[0] = output_name
            print(row)
        

with open('sample2.csv','w') as file:
    file_handler = csv.writer(file)
    
    file_handler.writerows(file_rows)