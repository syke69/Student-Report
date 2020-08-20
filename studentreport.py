import pickle 
import sys
import datetime
from _datetime import date
import matplotlib.pyplot as plt

def write():
    f=open('studentreport.dat','wb')
    record=[]
    loop = True
    while loop:
                                                 #roll number and name
        try:
            rno=int(input('enter roll no: '))
        except ValueError:
            print('type properly!!')
            rno=int(input('enter roll no: '))
        
        name=(input('enter student name: '))
                                                #dob
        try:
            dd,mm,yyyy= [int(x) for x in input('enter student\'s DOB(dd-mm-yyyy): ').split('-')]
            dob=date(yyyy,mm,dd)
        except ValueError:
            print('either day is out of range or you dont know how to type!')
            dd,mm,yyyy= [int(x) for x in input('enter student\'s DOB(dd-mm-yyyy): ').split('-')]
            dob=date(yyyy,mm,dd)
                                                #marks
                                                #cs
        try:
            csmarks=float(input('enter marks in cs: '))
        except ValueError:
            print('You have to enter a number!')
            csmarks=float(input('enter marks in cs: '))
        else:
            if csmarks>100:
                print('enter in 0-100 range!')
                csmarks=float(input('enter marks in cs: '))
                                                #maths
        try:
            mtmarks=int(input('enter marks in maths: '))
        except ValueError:
            print('You have to enter a number!')
            mtmarks=float(input('enter marks in maths: '))
        else:
            if mtmarks>100:
                print('enter in 0-100 range!')
                mtmarks=float(input('enter marks in maths: '))
                                        #english
        try:
            enmarks=int(input('enter marks in english: '))
        except ValueError:
            print('You have to enter a number!')
            enmarks=float(input('enter marks in english: '))
        else:
            if enmarks>100:
                print('enter in 0-100 range!')
                enmarks=float(input('enter marks in english: '))
                                        #physics
        try:
            phmarks=int(input('enter marks in physics: '))
        except ValueError:
            print('You have to enter a number!')
            phmarks=float(input('enter marks in physics: '))
        else:
            if phmarks>100:
                print('enter in 0-100 range!')
                phmarks=float(input('enter marks in physics: '))
                                            #chemistry
        try:
            chmarks=int(input('enter marks in chem: '))
        except ValueError:
            print('You have to enter a number!')
            chmarks=float(input('enter marks in chemistry: '))
        else:
            if chmarks>100:
                print('enter in 0-100 range!')
                chmarks=float(input('enter marks in chemistry: '))
        
        perc=(csmarks+mtmarks+enmarks+phmarks+chmarks)/5
        
        data=[rno, name, dob, csmarks, mtmarks, enmarks, phmarks, chmarks, perc]
        record.append(data)
        breaker=input('do you want to enter more(y/n): ')
        if breaker=='n':
            break
    pickle.dump(record, f)
def view(li):
    print('##########################################STUDENTS RECORD TABLE#######################################################')
    print('| roll no. |     name    |       dob      |    CS    |   maths   |  english  |  physics  |  chemistry  |  perc  |')
    print('========================================================================================================')
    for i in li:
        print('|   ',i[0],'   |   ',i[1],'   |  ',i[2],' |    ',i[3],'   |    ',i[4],'    |    ',i[5],'    |    ',i[6],'   |     ',i[7],'   |     ',i[8])
        print('|----------------------------------------------------------------------------------------------------------------------------------')
def SortName(name_li): 
    name_li.sort(key = lambda x: x[1]) 
    return view(name_li) 
def SortMarks(mark_li):
    mark_li.sort(reverse=True,key = lambda x: x[8]) 
    return view(mark_li)
def read():
    f=open('studentreport.dat','rb')
    a=pickle.load(f)
    while True:
        print('READ MENU \n 1-Normal Read View \n 2-Name wise \n 3- Marks wise \n 4-Back to main menu') 
        ch=int(input('enter your choice: '))
        if ch==1:
            view(a)
        if ch==2:
            SortName(a)
        if ch==3:
            SortMarks(a)
        if ch==4:
            break  
    f.close()
def close():
    print('Thank You!')
    sys.exit()
    
def search():
    f=open('studentreport.dat','rb')
    r=pickle.load(f)
    while True:
        found=0
        print('Search Filter \n 1-search by roll number \n 2-search by name \n 3-Back to main menu')
        try:
            choice = int(input('enter choice: '))
        except ValueError:
            print('wrong key pressed')
            choice = int(input('enter your choice: '))
        if choice==1:
            rn=int(input('enter roll number to search: '))
            for s in r:
                li = []
                if s[0]==rn:
                    li.append(s)
                    view(li)
                    found=1
            if found==0:
                print('record not found...')
                break
        if choice==2:
            search=str(input('enter name to search: '))
            for s in r:
                if s[1]==search:
                    print(s)
                    found=1   
            if found==0:
                print('record not found...')
        if choice==3:
            break
    
def graph():
    f=open('studentreport.dat','rb')
    a=pickle.load(f)

    rno = [x[0] for x in a]
    name=[x[1] for x in a]
    total=len(name)
    
    cslist=[x[3] for x in a]
    csavg=sum(cslist)/total
    
    mtlist=[x[4] for x in a]
    mtavg=sum(mtlist)/total
    
    enlist=[x[5] for x in a]
    enavg=sum(enlist)/total


    phlist=[x[6] for x in a]
    phavg=sum(phlist)/total

    
    chlist=[x[7] for x in a]
    chavg=sum(chlist)/total

    classtotal=[x[8] for x in a]
    classavg=sum(classtotal)/total 

    subavg=[csavg, mtavg, enavg, phavg, chavg, classavg]

    while True:
        print('GRAPH MENU \n 1-Subject-Marks graph\n 2-Subject-Average graph\n 3-Individual-Report \n 3-Back to main menu')
        try:
            choice = int(input('enter choice: '))
        except ValueError:
            print('wrong key pressed')
            choice = int(input('enter your choice: '))


        if choice==1:
            print('SUBJECTS \ncs\nmaths\neng\nphy\nchem ')
            ch=input('choose your subject: ')
            if ch=='cs':
                y=cslist
            elif ch=='maths':
                y=mtlist
            elif ch=='eng':
                y=enlist
            elif ch=='phy':
                y=phlist
            elif ch=='chem':
                y=chlist
            plt.bar(name, y, label='marks')
            plt.xlabel(ch)
            plt.ylabel('Marks')
            plt.subplots_adjust(bottom=0.19)
            plt.xticks(rotation=45)
            plt.title('Subject-Marks distribution')
            plt.legend()
            plt.grid()
            plt.show()
        elif choice==2:
            x=['C.S.','Maths','English','Physics','Chemistry','Class Average']
            y=subavg
            plt.bar(x, y, label='average marks')
            plt.xlabel('Subjects')
            plt.ylabel('Marks')
            plt.subplots_adjust(bottom=0.19)
            plt.xticks(rotation=45)
            plt.title('Subject-Average Graph')
            plt.legend()
            plt.grid()
            plt.show()
        elif choice==3:
            x=['C.S.','Maths','English','Physics','Chemistry','Percentage']
            rn=int(input('enter roll number to search: '))
            liy=[x for x in a if x[0]==rn]
            y=liy[0]
            yaxis=y[3:]
            plt.bar(x, yaxis, label='marks')
            plt.xlabel('Subjects')
            plt.ylabel('Marks Scored')
            plt.subplots_adjust(bottom=0.19)
            plt.xticks(rotation=45)
            plt.title(y[1]+'\nReport card')
            plt.legend()
            plt.grid()
            plt.show()

        elif choice==4:
            break

   
while True:
    print('MENU \n 1-Write student record \n 2-Display student record \n 3-Search \n 4-Graph \n 5-Exit')
    try:
        n=int(input('enter your choice: '))
    except ValueError:
        print('wrong key pressed')
        n=int(input('enter your choice: '))
    if n==1:
        write()
    if n==2:
        read()
    if n==3:
        search()
    if n==4:
        graph()
    if n==5:
        close()

