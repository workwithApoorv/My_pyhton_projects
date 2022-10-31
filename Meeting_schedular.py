import csv
from csv import DictReader as DR
import re
import smtplib
from email.message import EmailMessage
smtpobj = smtplib.SMTP('smtp.gmail.com',587)  # creating a connection obj  
smtpobj.starttls()  # initilize HTTPS Communication
smtpobj.login('dummyunused20@gmail.com','yash12345')

row=[]

def schedule():
    meeting=[]
    mId=1
    for id in range(len(row)):
        mId+=1
    for elements in range(1):
        meeting.append(mId)
        meeting.append(str(input("Enter the date of meeting[yyyy-mm-dd]: " )))
        meeting.append(str(input("Enter the time you want to start: ")))
        meeting.append(str(input("Enter the end time: ")))
        with open("participant_list.csv",'r') as openfile:
            for line in openfile:
                meeting.append(line)
        row.append(meeting)
    csv_input=str(input("Enter the file name you want to input "))    
    with open(csv_input, 'a') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(row)
        csvfile.close()
    print("Meeting Id: ",mId)
    for id in range(len(row)):
        message=f"Your meeting Id {row[mId-1][0]}\n Date of Meeting: {row[mId-1][1]}\n Start Time{row[mId-1][2]}\n End Time : {row[mId-1][3]}\n Participants email: {row[mId-1][4]}"

    msg = EmailMessage()

    msg['From'] = "dummyunused20@gmail.com"
    msg['To'] = "dummyunused20@gmail.com"
    msg['Subject'] = "New Meeting Alert!"

    body = message
    msg.set_content(body)
    smtpobj.send_message(msg)   
             
def reschedule():
    pass

def cancel():
    meeting_id=input("Enter the meeting id you want to delete: ")
    with open('meeting_list.csv','r') as csvfile:
        for line in csvfile:
            if line[0]==meeting_id:
                csvfile.remove(line)
                message=f"You have canceled the meeting of meeting Id {meeting_id}" 
                msg = EmailMessage()

                msg['From'] = "dummyunused20@gmail.com"
                msg['To'] = "dummyunused20@gmail.com"
                msg['Subject'] = "New Meeting Alert!"

                body = message
                msg.set_content(body)
                smtpobj.send_message(msg)    
            else:
                print("you have entered the wrong meeting Id")
                


print("\n\n**** Welcome to Meeting Schedular ****")
while(True):            
    lst1 = ["Schedule a new Meeting","Reschedule an old meeting","Cancel meeting","Exit"]
    print("\n\n","MAIN MENU".center(50,'-'))
    for i,line in enumerate(lst1,1):
        print(f"[{i}] {line}")
    try:
        user_input = int(input("Enter option No. to execute it:\t"))
    except:
        print("PLEASE ENTER NUMERIC VALUE ONLY!!!")
        continue
    if(user_input==1):
        schedule()
    elif(user_input==2):
        reschedule()
    elif(user_input == 3):
        cancel()
    elif(user_input == 4):
        print("EXITING")
        break
    else:
        print("ENTER A VALID VALUE\n")
        







