# CONTACT LIST
import csv
from csv import DictReader as DR
import re
import smtplib
header = ['Contact_ID','Name','Phone_Number','Email','City']
user_header = ['Name','Phone Number','Email']
### it only takes dictionary as its parameter###
###Implementing login with SMTP
smtpobj = smtplib.SMTP('smtp.gmail.com',587)  # creating a connection obj  
smtpobj.starttls()  # initilize HTTPS Communication
smtpobj.login('dummyunused20@gmail.com','yash12345')

def display_entry(entry):
    print(f"Contact ID:{entry['Contact_ID'].center(2)}|Name:{entry['Name'].center(10)}| Phone Number: {entry['Phone_Number']} | Email: {entry['Email'].center(20)} | City: {entry['City'].center(15)}")

def duplicate_check(lst):
    with open('contact_list.csv','r') as fh:
            data = DR(fh)
            for lineAsDictionary in data:
                index = 0
                for key in lineAsDictionary:
                    if(key=='Contact_ID'):
                        index += 1
                        continue
                    elif(key == 'City'):
                        break
#                     print(lineAsDictionary[key], lst[index])

                    if(lineAsDictionary[key] == lst[index]):
                        print(f"{key}: {lineAsDictionary[key]} already exists in the Directory")
                        return False
                    index += 1
            return True
            fh.close()


#  TO   ADD A NEW CONTACT
def add_contact():
#     CREATING A UNIQUE ID EVERYTIME THE USER WANTS TO CREATE A NEW CONTACT
    with open('contact_list.csv','r') as fh:
        data = DR(fh)
        ID = 0
        for line in data:
            while(ID<int(line['Contact_ID'])):
                ID += 1
                
        fh.close()
    
    print("ADD NEW CONTACT MENU".center(40,'-'))
    lst = []
    flag =0
    ID += 1
    lst.append(ID)
    
    for entry in header:
        if(entry!="Contact_ID"):
            value = input(f"Enter {entry}:\t")
        
        if(entry == "Name"):
            if(re.search("[^a-zA-z ]",value)):
                print("Please Enter alphabetic characters only".center(40))
                break
            else:
                name=''
                temp = value.split()
                for word in temp:
                    name += ' ' + word.capitalize()
                lst.append(name.strip())
        
        if(entry =="Phone_Number"):
            if(re.search("[^0-9]",value)):
                print("Please Enter numeric values only".center(40))
                break
            elif(re.search("^[0-9]{10}$",value)):
                lst.append(value)
            else:
                print("Only 10 digits numbers are valid".center(40))
                break
        
        if(entry =="Email"):
            if(re.search("^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+$",value)):
                lst.append(value)
            else:
                print("Please enter valid email address".center(40))
                break
                
        if(entry == "City"):
            if(re.search("[^A-Za-z 3-9]+",value)):
                print("Please use alphanumeric characters only".center(40))
            else:
                lst.append(value.capitalize().strip())
                flag = 1
                
    if(flag == 1):
        if(duplicate_check(lst)):
            with open('contact_list.csv','a') as fh:
                data = csv.writer(fh,lineterminator='\n')
                data.writerow(lst)
                fh.close()
            print("OPERATION SUCCESSFUL")
            print("NEW CONTACT ADDED:")
            
            for i in range(len(header)):
                print(f"{header[i]}:\t{str(lst[i])}" )
              
              
    else:
        print("OPERATION FAILED\tALL FIELDS SHOULD BE FILLED CORRECTLY")
    
    
# TO LIST ALL CONTACTS
def list_contacts():
    with open('contact_list.csv','r') as fh:
        data = DR(fh)
        for line in data:
            display_entry(line)
        fh.close()
        
#  TO SEARCH FOR A CONTACT       
def search_contacts():
    with open('contact_list.csv','r') as fh:
        tmp_data = DR(fh)
        data=[]
        for line in tmp_data:
            data.append(line)
        fh.close()
    ## DIRECTORY DATA IN data[]

    print("SEARCH MENU".center(40,'-'))
    for i, val in enumerate(user_header,1):
        print(f'[{i}] {val}')
        
    try:
        value = int(input("\nSelect a value from the menu:\t"))
    except:
        print("OPERATION FAILED\tPLEASE ENTER NUMERIC VALUES ONLY")
        return
    
    if(value == 1):
        name = input("Enter contact name:\t").strip()

        for line in data:
            if( name.lower() == line['Name'].lower() ):
                print( "CONTACT FOUND:\n" )
                display_entry(line)
                return
        print("FIELD NOT FOUND!!!")
        
    elif(value == 2):
        number = int(input("Enter Phone number:"))
        
        for line in data:
            if(number == int(line['Phone_Number'])):
                print("CONTACT FOUND:\n")
                display_entry(line)
                return
        print("FIELD NOT FOUND!!!")
        
    elif(value == 3):
        email = input("Enter email").lower().strip()
        for line in data:
            if(email == line['Email']):
                print("CONTACT FOUND:\n")
                display_entry(line)
                return
        print("FIELD NOT FOUND!!!")
        
    else:
        print("OPERATION FAILED\t PLEASE ENTER VALID INPUT")


# DELETE A CONTACT
def del_contact():
    
    with open('contact_list.csv','r') as fh:
        data = DR(fh)
        data_lst= []
        for adict in data:
            data_lst.append(adict)
        fh.close()
#     DIRECTORY DATA IN data_lst[]
    for i, val in enumerate(user_header,1):
        print(f'[{i}] {val}')
            
    value = int(input("Enter a value to select"))
    
    if(value == 1):
        name = input("Enter Contact Name:\t")
        
        for i,mini_dict in enumerate(data_lst):
            if(name.strip().lower() == mini_dict['Name'].lower()):
                index = i
                break
            index = -1
            
        if(index != -1):
            del(data_lst[index])
            print(f"ENTRY DELETED SUCCESSFULLY WITH NAME:{name}")
           
            smtpobj.sendmail('dummyunused20@gmail.com','dummyunused20@gmail.com' ,'Contact has been deleted')  # Send Email    
        else:
            print(f"CANNOT FIND ENTRY WITH NAME:{name}")
            return -1
        
    elif(value==2):
        number = int(input("Enter Contact Number:\t"))
        
        for i, mini_dict in enumerate(data_lst):
            if(number == int(mini_dict['Phone_Number'])):
                index  = i
                break
            index = -1
            
        if(index != -1):
            del(data_lst[index])
            print(f"ENTRY DELETED SUCCESSFULLY WITH PHONE NUMBER:{number}")
           
            smtpobj.sendmail('dummyunused20@gmail.com','dummyunused20@gmail.com' ,'Contact has been deleted')  # Send Email     
        else:
            print(f"CANNOT FIND ENTRY WITH PHONE NUMBER:{number}")
            return -1
    
    elif(value == 3):
        email = input("Enter email:\t").lower()
        for i, mini_dict in enumerate(data_lst):
            if(email == mini_dict['Email']):
                index = i
                break
            index = -1
            
        if(index != -1):
            del(data_lst[index])
            print(f"ENTRY DELETED SUCCESSFULLY WITH EMAIL: {email}")
            
            smtpobj.sendmail('dummyunused20@gmail.com','dummyunused20@gmail.com' ,'Contact has been deleted')  # Send Email
        else:
            print(f"CANNOT FIND ENTRY WITH EMAIL:{email}")
            return -1
                                
#     TODO: FIX THE local variable 'index' referenced before assignment                            
    else:
        print("Enter valid value")
        return -1
        
# REWRITING THE WHOLE CSV WITHOUT THE ENTRY 
    with open('contact_list.csv','w') as fh:
        
        data = csv.writer(fh,lineterminator="\n")
        data.writerow(header)
        
        for line in data_lst:
            lst=[]
            for val in line:
                lst.append(line[val])
            data.writerow(lst)
        fh.close()
        return 1

# MAIN LOOP  
print("\n\n**** Welcome to Contact Management System ****")
while(True):            
    lst1 = ["Add a new Contact","List all Contacts","Search for a Contact","Edit a contact","Delete a contact","Exit"]
    print("\n\n","MAIN MENU".center(50,'-'))
    for i,line in enumerate(lst1,1):
        print(f"[{i}] {line}")
    try:
        user_input = int(input("Enter option No. to execute it:\t"))
    except:
        print("PLEASE ENTER NUMERIC VALUE ONLY!!!")
        continue
    if(user_input==1):
        add_contact()
    elif(user_input==2):
        list_contacts()
    elif(user_input == 3):
        search_contacts()
    elif(user_input == 4):
        if(del_contact()==1):
            add_contact()
    elif(user_input == 5):
        del_contact()
    elif(user_input == 6):
        print("EXITING")
        break
    else:
        print("ENTER A VALID VALUE\n")
        