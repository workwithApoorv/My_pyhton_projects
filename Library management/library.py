import csv
from csv import DictReader as dr
import smtplib
from email.message import EmailMessage
smtpobj = smtplib.SMTP('smtp.gmail.com',587)  # creating a connection obj  
smtpobj.starttls()  # initilize HTTPS Communication
smtpobj.login('dummyunused20@gmail.com','yash12345')

book_header=["Book Name","Book SN","Rented"]
user_header=["Name","Email","Phone no.","Book SN","Cost per day","Days of Rent"]
#Addition of Book in book.csv file
def add_book():
    """to add a book in book.csv with there default values.
    output:
    there will be a success message after the addition of book.
    """

    book_name=str(input("Enter the name of Book: "))
    book_sn=str(input("Enter the book Serial Number: "))
    rent=0
    row=[book_name,book_sn,rent]
    with open("book.csv","a") as book:
        data=csv.writer(book,lineterminator='\n')
        data_insert=data.writerow(row)
        book.close()
    print("Book added succesfully")    


#Addition of User in user.csv file
def add_user():
    """to add a user in user.csv
    output:
    there will be a message for succesfully adding a user.
    """
    user_name=  str(input("Enter the name of User: "))
    user_email=str(input("Enter Email "))
    user_phone=str(input("Enter phone no. "))
    book_sn=""
    cost_per_day=0
    days=0
    row=[user_name,user_email,user_phone,book_sn,cost_per_day,days]
    with open("user.csv",'a') as user:
        data=csv.writer(user,lineterminator='\n')
        user_writer=data.writerow(row)
        user.close()
    print("User added succesfully")

#Renting a Book
def rent_book():
    """to rent a book by user and to change the value of rent from 0 to 1 in book.csv
        and to update the value of book serial number,cost per day and rent per day in user.csv.

    output:
    If book is already rented then printing the message of book already rented.
    Print the message of succefully completion of renting the book.
    Email a message for succesfully renting a book,cost of the book and the days of rent.


    
    """
    book_sn=input("Enter the SN of book you want to rent: ")
    user_name=input("Enter the user name: ")
    cost_per_day=int(input("Enter the cost of book: "))
    rent=int(input("Enter the number of days you want to rent the book: "))
    with open("book.csv","r") as book:
        data=csv.reader(book)
        data_lst=[]
        
        for list in data:
            if len(list)>0:
                data_lst.append(list)   
        book.close()
    
    # print(list(data_lst))
    for line in data_lst:
        
        if line[1]==book_sn:
            if line[2]==1:
                print("Book is already Rented,Please try to rent other book")
                break
            else:           
                line[2]=1
        else:
            continue      
    # print(list(data_lst))                    
    with open("book.csv","w") as book:
        data=csv.writer(book)
        data_writer=data.writerows(data_lst)
        book.close()
    with open("user.csv","r") as user:
        data=csv.reader(user)
        user_lst=[]
        for dictionary in data:
            if len(dictionary)>0:
                user_lst.append(dictionary)
        for dictionary in user_lst:
            if dictionary[0]==user_name:
                if dictionary[3]!='':
                    print("User already rented a book.")
                    break
                else:    
                    dictionary[3]=book_sn
                    dictionary[4]=cost_per_day
                    dictionary[5]=rent
            else:
                continue
        user.close()    
    with open("user.csv","w") as user:
        data=csv.writer(user)
        user_writer=data.writerows(user_lst)
        user.close()
    print("Book Rented Succesfully.")
    message=f"You have Rented Book with serial Number: {book_sn}| Cost of the book :{cost_per_day} | Day of Rent are : {rent}"
    msg = EmailMessage()

    msg['From'] = "dummyunused20@gmail.com"
    msg['To'] = "dummyunused20@gmail.com"
    msg['Subject'] = "New Book Rented"

    body = message
    msg.set_content(body)
    smtpobj.send_message(msg)       
#Returning a book        
def return_book():
    """to return a book by user and to update the rent value in book.csv from 0 to 1.
        to update the user.csv by the default values.
        output:
        Printing a message of succefully completion of book return.
        Email a message for succesfully return of book and the bill amount.
        """


    email=str(input("Enter email: "))
    with open("user.csv","r") as user:
        data=csv.reader(user)
        user_lst=[]
        for list in data:
            if len(list)>0:
                user_lst.append(list)   
        user.close()
        
        for list in user_lst:
            if list[1]==email:
                book_sn=list[3]
                bill=int(list[4])*int(list[5])
                list[4]=0
                list[5]=0
                list[3]=''
        user.close()
    with open("user.csv","w") as user:
        data=csv.writer(user)
        user_writer=data.writerows(user_lst)
        user.close()    
    with open("book.csv","r") as book:
        data=csv.reader(book)
        book_lst=[]
        for line in data:
            if len(line)>0:
                book_lst.append(line)
        for line in book_lst:
            if line[1]==book_sn:
                line[2]=0
            else:
                continue
        book.close()
    with open("book.csv","w") as book:
        data=csv.writer(book)
        book_writer=data.writerows(book_lst)
        book.close()
    print("Book Returned Succesfully")
    message=f"You have Returning Book with serial Number: {book_sn}| Your Bill is: {bill}"
    msg = EmailMessage()

    msg['From'] = "dummyunused20@gmail.com"
    msg['To'] = "dummyunused20@gmail.com"
    msg['Subject'] = "Book Succefully Returned"

    body = message
    msg.set_content(body)
    smtpobj.send_message(msg)  


#Deleting a book from book.csv        
def delete_book():
    """ To delete a book in book.csv , and to check whether the book is already returned of not.
        if the book is already rented then book will not be returned.

        output:
        if book is rented already then printing a message that book cannot be deleted.
        if book is deleted then print a message for book deletion.

    """
    book_sn=str(input("Enter a Book SN to delete"))
    with open("book.csv","r") as book:
        data=csv.reader(book)
        book_lst=[]
        for line in data:
            if len(line)>0:
                book_lst.append(line)       
        for line in book_lst:
            if line[1]==book_sn:
                if int(line[2])==1:
                    count=1
                    print("It can't be deleted ")
                    break

                else:
                    count=0
                    delete=line
                    print("Succesfully Book deleted")
            else:
                continue
        if count==0:    
            book_lst.remove(delete)

        book.close()
    with open("book.csv","w") as book:
        data=csv.writer(book)
        book_writer=data.writerows(book_lst)
        book.close()
    

#Deleting a User from user.csv    
def delete_user():
    """to delete a user from user.csv, if user already rented a book then it will not be deleted.
    output:
    If user rented a book then
    """

    email=str(input("Enter the email to delete user"))
    with open("user.csv","r") as user:
        data=csv.reader(user)
        user_lst=[]
        for line in data:
            if len(line)>0:
                user_lst.append(line)
        delete=None        
        for line in user_lst:
            if line[1]==email:
                if line[3]!='':
                    count=1
                    print("It can't be deleted.")
                    break
                else:    
                    count=0
                    delete= line
                    print("Succesfully User deleted")
            else:
                continue
        if count==0:    
            user_lst.remove(delete)    
        user.close()
    with open("user.csv","w") as user:
        data=csv.writer(user)
        user_writer=data.writerows(user_lst)
        user.close()
      


print("\n\n**** Welcome to Library Management System ****")
while(True):            
    lst1 = ["Add a book","Add a User","Rent a Book","Return a Book","Delete a Book","Delete a User","Exit"]
    print("\n\n","MAIN MENU".center(50,'-'))
    for i in range(0,len(lst1)):
        print(f"[{i+1}] {lst1[i]}")
    try:
        user_input = int(input("Enter option No. to execute it:\t"))
    except:
        print("PLEASE ENTER NUMERIC VALUE ONLY!!!")
        continue
    if(user_input==1):
        add_book()
    elif(user_input==2):
        add_user()
    elif(user_input == 3):
        rent_book()
    elif(user_input == 4):
        return_book()
    elif(user_input == 5):
        delete_book()
    elif(user_input == 6):
        delete_user()
    elif(user_input==7):
        print("Exiting")
        break

    else:
        print("ENTER A VALID VALUE\n")