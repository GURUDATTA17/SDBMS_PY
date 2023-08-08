#STUDENT DATABASE MANAGEMENT SYSTEM USING TKINTER AND CSV PACKAGES

from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import csv
def home_screen():
    homescreen = Tk()
    homescreen.title("Home Page")
    homescreen.minsize(width = 400, height = 400)
    homescreen.maxsize(width = 400, height = 400)
    l1 = Label(homescreen,text="Student Database",font=("Calibri",30))
    l1.pack(padx = 20)
    l2 = Label(homescreen,text="Choose Any Option below",font=("Calibri",18))
    l2.pack(ipady=20)
    b1 = Button(homescreen,text="Add a Student",height = 2, width = 20, font = (12),command=add_student)
    b1.pack(pady = 5)
    b2 = Button(homescreen,text="Display Student Data",height = 2, width = 20, font = (12),command=lambda:search_student(0))
    b2.pack(pady = 5)
    b3 = Button(homescreen,text="Remove Student",height = 2, width = 20, font = (12),command=lambda:search_student(1))
    b3.pack(pady = 5)
    #b4 = Button(homescreen,text="Update Student Data",height = 2, width = 20, font = (12),command=update_student())
    #b4.pack(pady = 5)
    homescreen.mainloop()
    
def add_student():
    window=Tk()
    window.title("ADD STUDENT INFORMATION")
    window.minsize(width=600,height=600)
    window.maxsize(width=600,height=600)
    dict_data={'Name': StringVar(window),'USN':StringVar(window),'Email':StringVar(window),'DOB':[StringVar(window),StringVar(window),StringVar(window)],'College':StringVar(window),'Branch':StringVar(window),'Section':StringVar(window),'Phno':StringVar(window),'Gender':IntVar(window)}
    dict_data['Branch'].set('Select Your Branch')
    dict_data['DOB'][0].set('DD')
    dict_data['DOB'][1].set('MM')
    dict_data['DOB'][2].set('YYYY')
    dict_data['Gender'].set(None)
    def store():
                        for x in dict_data:
                            if x == 'DOB':
                                if dict_data[x][0].get() == 'dd' or dict_data[x][1].get() == 'mm' or dict_data[x][2].get() == 'yyyy':
                                    #print("ERROR1")
                                    tkinter.messagebox.showerror("ERROR101","CHECK IF ALL THE DETAILS ARE FILLED PROPERLY ")
                                    #return None
                                    break
                                continue

                            #print(x)
                           # print (dict_data[x].get())
                            if dict_data[x].get() == '' or dict_data[x].get() == 'Select Your Branch':
                        #if(dict_data['Name'].get()=="" or emailId=="" or phoneno=="" or college=="" or branch=="" or section=="" or usn=="" or d=="" or m=="" or y=="" ):
                                #print("ERROR1")
                                tkinter.messagebox.showerror("ERROR101","CHECK IF ALL THE DETAILS ARE FILLED PROPERLY ")
                                #return None
                                break
                        else:
                         if (dict_data['Gender'].get()>2):
                                pass
                         elif(len(dict_data['Phno'].get()) != 10):
                                # print("ERROR")
                                 tkinter.messagebox.showerror("ERROR101","PHONE NUMBER SHOULD BE 10 DIGITS , ENTER APPROPRIATELY ")
                                 #return None          
                         else:
                                            result=tkinter.messagebox.askquestion("SUBMIT?","YOU ARE ABOUT TO SUBMIT THE DATA Ms/Mr "+dict_data['Name'].get())
                                            if(result=='yes'):
                                                                print("DONE")
                                                                with open('s_data.csv','a')as csvfile:
                                                                                    writer=csv.writer(csvfile)
                                                                                    #writer.writerow([name,emailId,phoneno,college,branch,section,usn,dob])
                                                                                    write_list = []
                                                                                    for x in dict_data:
                                                                                        if x == 'DOB':
                                                                                            dob=dict_data['DOB'][0].get()+"-"+dict_data['DOB'][1].get()+"-"+dict_data['DOB'][2].get()
                                                                                            write_list.append(dob)
                                                                                            continue
                                                                                        if x == 'Gender':
                                                                                            if dict_data[x].get() == 1:
                                                                                                write_list.append('Female')
                                                                                                continue
                                                                                            elif dict_data[x].get() == 2:
                                                                                                write_list.append('Male')
                                                                                                continue
                                                                                        write_list.append(dict_data[x].get())
                                                                                    writer.writerow(write_list)
                                                                                    clear()
                                                                csvfile.close()
                                            else:
                                                              return None
                        #add_student() 
    def clear():
                 for x in dict_data:
                     if x == 'DOB':
                        dict_data['DOB'][0].set('DD')
                        dict_data['DOB'][1].set('MM')
                        dict_data['DOB'][2].set('YYYY')
                        continue
                     if x == 'Gender':
                        dict_data['Gender'].set(None)
                     if x == 'Branch':
                        dict_data['Branch'].set('Select Your Branch')
                        continue
                     dict_data[x].set('')
    lstd=Label(window,text="STUDENT DATABASE MANAGEMENT",font=("canela",20))
    lstd.pack(pady = 10)
    #PERSONAL INFORMATION
    lpstd=Label(window,text="PERSONAL INFORMATION OF STUDENT",font=("canela",18))
    lpstd.pack(pady = 5)
    #label for students name and entry for name  
    lname=Label(window,text="STUDENT NAME:",font=("canela",15),fg="black")
    lname.place(x=10,y=140)
    ename=Entry(window,textvariable=dict_data['Name'],width=30,font=("canela",15),bg="white",fg="black")
    ename.place(x=200,y=140)   
     #label and entry for student phonenumber
    lusn=Label(window,text="USN",font=("canela",15),fg="black")
    lusn.place(x=10,y=180)
    eusn=Entry(window,textvariable=dict_data['USN'],width=30,font=("canela",15),bg="white",fg="black")
    eusn.place(x=200,y=180)
    #label and entry for student emailId
    lemail=Label(window,text="E-MAIL ID",font=("canela",15),fg="black")
    lemail.place(x=10,y=220)
    email=Entry(window,textvariable=dict_data['Email'],width=30,font=("canela",15),bg="white",fg="black")
    email.place(x=200,y=220)
    #label and entry for dob
    ldob=Label(window,text="DATE OF BIRTH",font=("canela",15),fg="black")
    ldob.place(x=10,y=260)
    #edd=Entry(window,width=5,font=("canela",15),bg="white",fg="black")
    #edd.place(x=200,y=260)
    listdays=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    droplistdays=OptionMenu(window,dict_data['DOB'][0],*listdays)
    droplistdays.config(width=5)
    droplistdays.place(x=200,y=260)
    #emm=Entry(window,width=5,font=("canela",15),bg="white",fg="black")
    #emm.place(x=300,y=260)
    listmonths=['January','February','March','April','May','June','July','August','September','October','November','December']
    droplistmonths=OptionMenu(window,dict_data['DOB'][1],*listmonths)
    droplistmonths.config(width=5)
    droplistmonths.place(x=300,y=260)
    #eyy=Entry(window,width=5,font=("canela",15),bg="white",fg="black")
    #eyy.place(x=400,y=260)
    listyears=['2000','2001','2002','2003','2004']
    droplistyears=OptionMenu(window,dict_data['DOB'][2],*listyears)
    droplistyears.config(width=5)
    droplistyears.place(x=400,y=260)
    #label for and entry for college
    lclg=Label(window,text="COLLEGE",font=("canela",15),fg="black")
    lclg.place(x=10,y=300)
    eclg=Entry(window,textvariable=dict_data['College'],width=30,font=("canela",15),bg="white",fg="black")
    eclg.place(x=200,y=300)
    #branch
    lbranch=Label(window,text="BRANCH",font=("canela",15),fg="black")
    lbranch.place(x=10,y=340)
    listbranch=['CSE','ISE','AI&ML','ECE','EEE','CIVIL','MECHANICAL','ETE','EIE']
    droplistba=OptionMenu(window,dict_data['Branch'],*listbranch)
    droplistba.config(width=30,fg="black",font=("canela",12))
    droplistba.place(x=200,y=340)
    #ebranch=Entry(window,textvariable=fbranch,width=30,font=("canela",15),fg="black")
    #ebranch.place(x=200,y=340)
    #section
    slsec=Label(window,text="SECTION",font=("canela",15),fg="black")
    slsec.place(x=10,y=380)
    esec=Entry(window,textvariable=dict_data['Section'],width=5,font=("canela",15),bg="white",fg="black")
    esec.place(x=200,y=380)
    #usn
    lph=Label(window,text="Phone Number",font=("canela",15),fg="black")
    lph.place(x=10,y=420)
    eph=Entry(window,textvariable=dict_data['Phno'],width=30,font=("canela",15),bg="white",fg="black")
    eph.place(x=200,y=420)
    lgender=Label(window,text="GENDER",font=("canela",15),fg="black")
    lgender.place(x=10,y=460)
    #gender
    rf=Radiobutton(window,text="FEMALE",variable=dict_data['Gender'],value=1,font=("canela",10),bg="white",fg="black")
    rf.place(x=200,y=460)
    rm=Radiobutton(window,text="MALE",variable=dict_data['Gender'],value=2,font=("canela",10),bg="white",fg="black") 
    rm.place(x=400,y=460)
    #enterbutton
    bst=Button(window,text="ENTER",font=("canela",15),fg="black",bg="white",command=store)
    bst.place(x=100,y=500)
    #clearbutton
    bclr=Button(window,text="CLEAR",font=("canela",15),fg="black",bg="white",command=clear)
    bclr.place(x=250,y=500)
    window.mainloop()

def update_student():
    print("Updating")
    #Update GUI Window goes here
def disp_student(usn_todisp):
    def displaywindow(details):
        display=Tk()
        display.title("USN - Information")
        display.minsize(width=500,height=500)
        display.maxsize(width=500,height=500)
        #display window
        ldis=Label(display,text="DISPLAY WINDOW",font=("Times New Roman",18),fg="black")
        ldis.pack(pady=10)
        #name
        lnm=Label(display,text="Name:",font=("Times New Roman",18),fg="black")
        lnm.place(x=10,y=70)
        enm=Label(display,text=details[0],font=("Times New Roman",18),fg="black")
        enm.place(x=210,y=70)
        #usn
        lus=Label(display,text="USN:",font=("Times New Roman",18),fg="black")
        lus.place(x=10,y=110)
        eus=Label(display,text=details[1],font=("Times New Roman",18),fg="black")
        eus.place(x=210,y=110)
        #phoneno
        lph=Label(display,text="Contact Number:",font=("Times New Roman",18),fg="black")
        lph.place(x=10,y=150)
        eph=Label(display,text=details[7],font=("Times New Roman",18),fg="black")
        eph.place(x=210,y=150)
        #email
        lemil=Label(display,text="Email ID:",font=("Times New Roman",18),fg="black")
        lemil.place(x=10,y=190)
        emil=Label(display,text=details[2],font=("Times New Roman",18),fg="black")
        emil.place(x=210,y=190)
        #dob
        ld=Label(display,text="Date of Birth:",font=("Times New Roman",18),fg="black")
        ld.place(x=10,y=230)
        edob = Label(display,text=details[3],font = ('Times New Roman',18))
        edob.place(x = 210, y = 230)
        #college
        lc=Label(display,text="College:",font=("Times New Roman",18),fg="black")
        lc.place(x=10,y=270)
        ec=Label(display,text=details[4],font=("Times New Roman",18),fg="black")
        ec.place(x=210,y=270)
        #branch
        lbr=Label(display,text="Branch: ",font=("Times New Roman",18),fg="black")
        lbr.place(x=10,y=310)
        ebr=Label(display,text=details[5],font=("Times New Roman",18),fg="black")
        ebr.place(x=210,y=310)
        #sec
        ls=Label(display,text="Section:",font=("Times New Roman",18),fg="black")
        ls.place(x=10,y=350)
        es=Label(display,text=details[6],font=("Times New Roman",18),fg="black")
        es.place(x=210,y=350)
        #gender
        lg=Label(display,text="Gender:",font=("Times New Roman",18),fg="black")
        lg.place(x=10,y=390)
        eg=Label(display,text=details[8],font=("Times New Roman",18),fg="black")
        eg.place(x=210,y=390)
        display.mainloop()
        #print('Its workingggg')
    with open('s_data.csv','r')as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if(not(row == [])):
                if(row[1] == usn_todisp):
                    displaywindow(row)
                    break
                else:
                    continue
            else:
                continue
    csvfile.close()
    print("Displaying")
    #Display GUI Window Goes here
def del_student(details):
    temp_list=[]
    with open('s_data.csv','r')as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == details:
                pass
            else:
                temp_list.append(row)
    print(temp_list)
    csvfile.close()
    with open('s_data.csv','w')as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(temp_list)):
            writer.writerows([temp_list[i]])
    csvfile.close()
    '''df = pd.read_csv('s_data.csv')
    df_s = df[:9]
    df_s.set_index('USN',inplace = True)
    df_s = df_s.drop(usn_todel)'''
    print("Deletiing")
    #Delete GUI Window goes here
def search_student(pathch):
    def check():
        print (feusn.get())
        with open('s_data.csv','r')as csvfile:
            reader=csv.reader(csvfile)
            flag = 0
            for row in reader:
                if(not(row == [])):
                    print(row[1])
                    if feusn.get() == row[1]:
                        if pathch == 0:
                            feusn.set('')
                            disp_student(row[1])
                            pass
                        else:
                            feusn.set('')
                            result=tkinter.messagebox.askquestion("Confirmation!",f"Are you sure you want to delete the following student from Database?\n USN: {row[1]}\n Name: {row[0]} ")
                            if result == 'yes':
                                del_student(row)
                            else:
                                return None
                            pass
                        #proceed
                        print("Student found")
                        flag = 1
                        break
                else:
                    continue
            if flag == 0:
                 tkinter.messagebox.showerror("ERROR101","INVALID USN ")
            feusn.set('')
        csvfile.close()
    perinfo=Tk()
    feusn=StringVar(perinfo)
    perinfo.title("Search Student")
    perinfo.minsize(width=300,height=300)
    perinfo.maxsize(width=300,height=300)
    leusn=Label(perinfo,text="ENTER USN",font=("canela",15),fg="black")
    leusn.place(x=90,y=50)
    eeusn=Entry(perinfo,font=("canela",15),textvariable=feusn,fg="black",bd=5,width=15)
    eeusn.place(x=70,y=100)
    #feusn=StringVar()
    beusn=Button(perinfo,text="ENTER",font=("canela",15),fg="black",command=check)
    beusn.place(x=110,y=150)

    perinfo.mainloop()
home_screen()

