def types_of_buses(): 
                
        myfile=open(r"types of buses.txt","w+")
        print("this file contains data about types of bus available in our service")
        myfile.write("This file contains data about types of bus available in our service\n")
        myfile.write("TYPES OF BUSES AVAILABLE ARE.......\n")
        myfile.write("1. NON AC BUS\n")
        myfile.writelines(["\t","i)NORMAL BUS","\n","\t","ii)SLEEPER BUS","\n"])
        myfile.write("2. AC BUS\n")
        myfile.writelines(["\t","i)NORMAL BUS","\n","\t","ii)SLEEPER BUS","\n"])
        myfile.write("3. LOCAL BUS\n")
        myfile.write("4.TIRTHA YATRA BUS\n")
        myfile.writelines(["\t","i)NORMAL BUS"])
        myfile.write("4. BUS for PRIVATE BOOKING\n")
        myfile.writelines(["\t","i)NORMAL BUS(AC and NON AC)","\n","\t","ii)SLEEPER BUS(only AC)","\n"])
        myfile.flush()      #sending from buffer
        myfile.close()

        print("MENU...........")
        print("1.know the type of buses available")
        print("2.update the record if you are manager")

        l=int(input("enter your choice 1/2"))
        if l==1 :
                file=open(r"types of buses.txt","r")
                str=" "
                while str:
                    str=file.read(1)
                    print(str,end=" ")
                file.close()

        elif l==2 :
                print("If you are authorised then only you can make changes in file......")
                name=input("enter your name...")
                password=input("enter the password...")
                if (name in ['Ankur','Kushagra','Ujjwal']) and (password=='BOSS' or password=='boss') :
                    print("********ACESS GRANTED***********")
                    print("you can add more type")
                    while True :
                        file2=open(r"types of buses.txt","a+")
                        t2=input("enter the type you want to add")
                        file2.write(t2)
                        file2.write("\n")
                        file2.flush()
                        a=input("want to add moreY/N")
                        if a=='n' or a=='N' :
                             print("dispalying updated file......")
                             file2.seek(0)
                             t3=file2.read()
                             print(t3)
                             break
                        file2.close()
                  
                    
                else:
                     print("*******ACESS DENIED**********")
                     print("######NOT ALLOWED#######")
        else :
                print("WRONG CHOICE.....")


#main


import csv
import random
import mysql.connector as sqltor
def filereader() :
    file1=open("details_buses.csv","r",newline="")
    outfile=csv.reader(file1)
    for rec in outfile :                                                   #reading entire file
        print(rec)
    file1.close()

myfile=open("details_buses.csv","w",newline="")
print("...............HELLO USER...............")
print("This file provides every detail you want to know about the BUS in which you want to travel....")
infile=csv.writer(myfile)
l=["DETAILS ABOUT BUSES"]
infile.writerow(l)
record=["SR NO.","BUS NAME","VEHICLE NO.","STARTS FROM","DESTINATION","TIMINGS","RUNTIME","AC","WIFI","FOOD SERVICE"]
infile.writerow(record)
r1=["B01","LUCKNOW EXPRESS","UP 78 DJ 5678","KANPUR","LUCKNOW","10:00 AM","2-2:30 HR","AC","NO","NA"]
infile.writerow(r1)
r2=["B02","AGRA EXPRESS","UP 72 RJ 1228","KANPUR","AGRA","18:00 PM","3-3:30 HR","AC","YES","NA"]
infile.writerow(r2)
r3=["B03","UNNAO LOCAL","UP 76 CW 7652","UNNAO","LUCKNOW","17:00 PM","0-0:30 HR","NON AC","NO","NA"]
infile.writerow(r3)
r4=["B04","GURUGRAM EXPRESS","UP 72 GH 3628","LUCKNOW","GURUGRAM","21:00 PM","5-6 HR","AC","YES","AVAILABLE"]
infile.writerow(r4)
r5=["B05","SHATABADI EXPRESS","UP 78 KW 4020","KANPUR","NEW DELHI","18:00 PM","5 HR","AC","YES","AVAILABLE"]
infile.writerow(r5)
r6=["B06","SAMBAD EXPRESS","UP 72 KL 7690","LUCKNOW","AHEMDABAD","23:00 PM","10-12HR","AC","YES","AVAILABLE"]
infile.writerow(r6)
r7=["B07","KNP LOCAL","UP 78 HK 3628","KANPUR","BANTHARA","08:00 AM","1-1:30 HR","NON AC","NO","NA"]
infile.writerow(r7)
r8=["B08","GORAKHPUR DEPO","UP 82 HH 4529","KANPUR","GORAKHPUR","10:00 AM","6-8 HR","NON AC","NO","NA"]
infile.writerow(r8)
r9=["B09","AYODHYA DHAM EXPRESS","UP 80 LA 3248","KANPUR","AYODHYA","06:00 AM","5 HR","AC","YES","AVAILABLE"]
infile.writerow(r9)
r10=["B10","BHOPAL DEPO","UP 82 OP 2398","LUCKNOW","BHOPAL","23:00 PM","14-16 HR","AC","YES","AVAILABLE"]
infile.writerow(r10)
r11=["B11","BASTI DEPO","UP 76 LK 6732","LUCKNOW","BASTI","20:00 PM","6-7 HR","NON AC","NO","NA"]
infile.writerow(r11)
r12=["B12","KRANTI EXPRESS","UP 45 UJ 7798","FAIZABAD","BHUBANESHWAR","12:00 AM","8-10 HR","AC","NO","AVAILABLE"]
infile.writerow(r12)
r13=["B13","KOLKATA DELUXE EXP","UP 56 GH 5628","LUCKNOW","KOLKATA","21:00 PM","9-10 HR","AC","YES","AVAILABLE"]
infile.writerow(r13)
r14=["B14","J&K EXPRESS ","UP 72 KL 9923","KANPUR","SRINAGAR","23:00 PM","15-16 HR","AC","YES","AVAILABLE"]
infile.writerow(r14)
myfile.close()
print("MENU................")
print("1.TO DISPLAY THE ENTIRE DETAILS ABOUT AVAILABLE BUSES....")
print("2.TO FIND A PARTICULAR BUS.....")
print("3.TO GENERATE A PNR NUMBER......")
print("4.TO ADD MORE BUSES......")
print("5.TO GENERATE BILL.........")
print("6.TO GO TO TICKET RESERVATION SYSTEM")
print("7.TO KNOW TYPES OF BUSES")
ch=int(input("enter your choice ...."))
if ch==1 :
    filereader()

elif ch==2 :
    while True :
        pickup=input("enter your pickup point....(IN UPPERCASE)")
        dest=input("enter your destination....(IN UPPERCASE)")
        file2=open("details_buses.csv","r",newline="")
        outfile=csv.reader(file2)
        flag=1
        for rec in outfile :
            if (pickup in rec) and (dest in rec) :
                print("BUS AVAILABLE FOR YOUR TRAVEL...........")
                print(record)
                print(rec)
                flag=0
    
        if flag :
                print("SORRY....")
                print("NO BUS AVAILABLE ON THIS ROUTE.......")
        file2.close()
        k=input("want to search for more buses? Y/N")
        if k=='n' or k=='N' :
            print("THANK YOU!!!!!!!")
            break

elif ch==3 :
    print("To generate PNR number you need to enter your destination and pickup place....")
    while True :
        pickup=input("enter your pickup point....(IN UPPERCASE)")
        dest=input("enter your destination....(IN UPPERCASE)")
        file3=open("details_buses.csv","r",newline="")
        outfile=csv.reader(file3)
        flag=1
        for rec in outfile :
            if (pickup in rec) and (dest in rec) :
                name=input("enter your name......")
                k=str(random.randint(100,999))
                pnr=rec[0]+name+k
                print(name)
                print("your PNR number is.........")
                print(pnr)
                print("In the bus ...........",rec[1])
                print("Now you can book a ticket using this PNR")
                print("Then you can check whether your ticket is confirmed or not!!!!!")
                flag=0
        a=1
        if flag :
            print("############     PNR NOT GENERATED   ##########")
            print("due to unavailability of required bus")
            print("TRY AGAIN......")
            s=input("WANT TO TRY AGAIN???? Y/N")
            a=0
            if s=='n' or s=='N' :
                print("UNSUCCESSFULL.........")
                print("TRY LATER!!!!!!!!")
                break
        
        file3.close()
        if a :
            break
elif ch==4 :
    print("If you are authorised then only you can make changes in file......")
    name=input("enter your name...")
    password=input("enter the password...")
    if (name in ['Ankur','Kushagra','Ujjwal']) and (password=='BOSS' or password=='boss') :
            print("********ACESS GRANTED***********")
            print("you can add more type")
            while True :
                file4=open("details_buses.csv","a",newline="")
                infile=csv.writer(file4)
                print("Enter the record in this form.....")
                print(record)
                ab=input("ENTER THE DETAILS SEPARTED BY COMMAS.......")
                lst=ab.split(",")
                infile.writerow(lst)
                file4.close()
                m=input("want to add more???  Y/N")
                if m=='n' or m=='N' :
                    print("DISPLAYING UPDATED FILE...............")
                    print()
                    filereader()
                    break
            print("THANK YOU..........")

    else :
        print("*******ACESS DENIED**********")
        print("######NOT ALLOWED#######")

elif ch==5 :
    mycon=sqltor.connect(host="local",user="root",passwd="MyPass",database="BILLING_SYSTEM")
    print("\nWELCOME!TO BILL GENERATION PORTAL\n")
    if mycon.is_connected()=="False" :
        print("\nSERVER ERROR\n")
        print("\nTRY LATER........\n")
    else :
      
            cursor=mycon.cursor()
            cursor.execute("SELECT * FROM PRICES")
            data=cursor.fetchall()
            j=random.randint(1,2)
            print("\nTO GENERATE YOUR BILL ENTER YOUR PNR NUMBER\n")
            pnr=input("Enter your PNR number.....")
            name=input("Enter your name...")
            age=int(input("Enter your age...."))
            sex=input("Enter your gender......M/F")
            print("\nBILL\n")
            print()
            print("PNR :",pnr)
            print("NAME :",name,end="\t\t\t")
            print("AGE :",age)
            print("BUS NO :",rec[0],end="\t\t\t")
            print("BUS NAME :",rec[1])
            print("FROM :",rec[3],end="\t\t\t")
            print("TO :",rec[4])
            print("VEHICLE NO :",rec[4])
            print("SEAT NO :",random.radint(1,60))
            if j==1 :
                print("STATUS : CONFIRMED")
            else :
                print("STATUS : PENDING")
            print()
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

            for bus in data :
                if rec[1] in bus :
                    ticket_cost=bus[2]
                    gst=bus[3]
                    total_cost=ticket_cost + ((gst/100)*ticket_cost)
                    final_cost=total_cost*people
                    break
                    
            print("TICKET COST :","Rs.",final_cost)
            print("GST APPLIED :",gst,"%")
            print("TOTAL COST :","Rs.",total_cost)
            print()
            print()
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("/nTHANK YOU FOR USING ONLINE BILL GENERATOR!!!")
    mycon.close()
elif ch==6:
    print("redirect to ticket reservation system")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n WELCOME!TO TICKET RESERVATION PORTAL\n")
    import random
    recurse=('Y')
    j=random.randint(1,2)
    while recurse!=('N','NO','n','no'):
       print("1.check your PNR status")
       print("2.ticket reservation")
       option=int(input("\nENTER YOUR OPTION\n"))
    
       if option==1:
         if j==1:
            print("your reservation status is confirmed")
         else:
            print("your reservation is still in waiting list")
         break
   
       elif option==2:
          people=int(input("\nenter the no. of tickets you want\n"))
          name1=[]
          age1=[]
          sex1=[]
          contactno1=[]
        
          for p in range(people):
             name=str(input("\nname : "))
             name1.append(name)
             age=int(input("\nage : "))
             age1.append(age)
             sex=str(input("\nMale or Female : "))
             sex1.append(sex)
             contactno=int(input("\nenter contact no. : "))
             contactno1.append(contactno)
            
          recurse=str(input("do you want to review details,yes/no"))
          if recurse in ('n','NO','no','No'):
             recurse=('N')
          else:
             x=0
             print("\nTotal tickets :",p)
             for p in range(1,people+1):
                print("Ticket : ",p)
                print("Nmae : ",name1[x])
                print("Age : ",age1[x])
                print("gender : ",sex1[x])
                print("contact : ",contactno1[x])
                
                x=x+1
          final=str(input("do you want to submit.y/n"))
          if final in ('n','no','No','No'):
           print("please refill the form")
          else:
           print("your booking has been confirmed.THANK YOU FOR VISITING US")
          break
elif ch==7:
    types_of_buses()
    
else:
    print("wrong choice")