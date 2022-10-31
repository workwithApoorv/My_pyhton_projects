import csv
header=["Book Name","Book SN","Rented"]
with open("book.csv",'w') as book:
    data=csv.writer(book,lineterminator='\n')
    book_writer=data.writerow(header)
    book.close()