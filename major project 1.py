import mysql.connector
from tkinter import *
from tkinter import messagebox
import random
db=mysql.connector.connect(host='localhost',
                           user='root',
                           password='0000',
                           database='air_online')
my_cur=db.cursor()


def entry():
    root=Tk()
    root.title('AIR_ONLINE .LTD')
    root.geometry('300x100')
    b=Button(root,text='WELCOME TO AIR_ONLINE',activeforeground = "blue",
             bd=5,font='jokerman')
    b.pack()
    def click():
        root.destroy()
        root1=Tk()
        root1.title('AIR_ONLINE .LTD')
        root1.geometry('180x235')

        
        
        def click1():
            root2=Tk()
            root2.title('AIR_ONLINE .LTD')
            root2.geometry('500x500')
            Label(root2,text="ENTRY FORM",font='jokerman',bg='red',bd=2,
                  relief=RAISED).place(bordermode=OUTSIDE, height=40,
                                       width=160,x=180,y=5)
    
            eno=str(random.randint(1,1000))+str(chr(random.randint(65,90)))+str(random.randint(1,1000))
            print(eno)
            
            Label(root2,text="NAME OF PASSENGER:",font='jokerman').place(x=50,y=60)
            Label(root2,text="AGE OF PASSENGER:",font='jokerman').place(x=50,y=90)
            Label(root2,text="GENDER:",font='jokerman').place(x=50,y=120)
            Label(root2,text="CATEGORY:",font='jokerman').place(x=50,y=150)
            Label(root2,text="FROM:",font='jokerman').place(x=50,y=180)
            Label(root2,text="TO:",font='jokerman').place(x=50,y=220)
            Label(root2,text="DATE OF JOURNEY:",font='jokerman').place(x=50,y=250)
            Label(root2,text="FLIGHTS:",font='jokerman').place(x=50,y=280)
            Label(root2,text="CLASS:",font='jokerman').place(x=50,y=310)
            Label(root2,text="MOBILE NO.:",font='jokerman').place(x=50,y=340)


            
            aa=StringVar(root2)
            bb=StringVar(root2)
            cc=StringVar(root2)
            dd=StringVar(root2)
            ee=StringVar(root2)
            ff=StringVar(root2)
            gg=StringVar(root2)
            hh=StringVar(root2)
            ii=StringVar(root2)
            jj=StringVar(root2)
            e1=Entry(root2,textvariable=aa).place(x=350,y=60)
            e2=Entry(root2,textvariable=bb).place(x=350,y=90)
            e3=Entry(root2,textvariable=cc).place(x=350,y=120)
            e4=Entry(root2,textvariable=dd).place(x=350,y=150)
            e5=Entry(root2,textvariable=ee).place(x=350,y=180)
            e6=Entry(root2,textvariable=ff).place(x=350,y=220)
            e7=Entry(root2,textvariable=gg).place(x=350,y=250)
            e8=Entry(root2,textvariable=hh).place(x=350,y=280)
            e9=Entry(root2,textvariable=ii).place(x=350,y=310)
            e10=Entry(root2,textvariable=jj).place(x=350,y=340)

            ename=aa.get()
            eage=bb.get()
            egender=cc.get()
            ecategory=dd.get()
            efrom=ee.get()
            eto=ff.get()
            edoj=gg.get()
            eflights=hh.get()
            eclass=ii.get()
            emob=jj.get()
            

            tup=(ename,eage,egender,ecategory,efrom,eto,edoj,eflights,eclass,emob)
            print(tup)

            def insert():
                ename=aa.get()
                eage=bb.get()
                egender=cc.get()
                ecategory=dd.get()
                efrom=ee.get()
                eto=ff.get()
                edoj=gg.get()
                eflights=hh.get()
                eclass=ii.get()
                emob=jj.get()
                
                print(ename,eage,egender,ecategory,efrom,eto,edoj,eflights,eclass,emob,eno)
                my_cur=db.cursor()
                my_cur.execute('insert into bookt values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                               (ename,eage,egender,ecategory,efrom,eto,edoj,eflights,eclass,emob,eno))
                db.commit()
                tup1=(ename,eage,egender,ecategory,efrom,eto,edoj,eflights,eclass,emob)
                print(tup1)
                messagebox.askquestion("Confirm","Are you sure?") 
                messagebox.showinfo('DONE!','TICKET BOOKED')
                
                root6=Tk()
                root6.title('UID')
                Label(root6,text=eno,font='jokerman').place(x=10,y=10)
                
                def onclick():
                    root6.destroy()
                    
                Button(root6,text='OK',command=onclick,font='jokerman').place(x=10,y=50)
                
                
                aa.set('')
                bb.set('')
                cc.set('')
                dd.set('')
                ee.set('')
                ff.set('')
                gg.set('')
                hh.set('')
                ii.set('')
                jj.set('')
                

            def clear():
                aa.set('')
                bb.set('')
                cc.set('')
                dd.set('')
                ee.set('')
                ff.set('')
                gg.set('')
                hh.set('')
                ii.set('')
                jj.set('')

            def exitall():
                root1.destroy()
                root2.destroy()
                
            def back():
                root2.destroy()
                
                


            
            Button(root2,text='SAVE',font='jokerman',command=insert).place(x=50,y=400)
            
            Button(root2,text='CLEAR',font='jokerman',command=clear).place(x=150,y=400)
            Button(root2,text='BACK',font='jokerman',command=back).place(x=250,y=400)
            Button(root2,text='EXITALL',font='jokerman',command=exitall).place(x=350,y=400)
            

         
        b2=Button(root1,text='BOOK_TICKETS',command=click1,bg='light salmon',bd=3,font='jokerman')
        b2.place(bordermode=OUTSIDE, height=50, width=160,x=10,y=10)
        

        def click2():

            root7=Tk()
            root7.title('AIR_ONLINE .LTD')
            v1=StringVar(root7)

            Label(root7,text='ENO:',font='jokerman').place(x=10,y=10)
            Entry(root7,textvariable=v1).place(x=55,y=10)

            
            def val():
                root3=Tk()
                root3.title('AIR_ONLINE .LTD')
                root3.geometry('500x500')
                Label(root3,text="UPDATE PANEL",font='jokerman',bg='red',bd=2,relief=RAISED).place(bordermode=OUTSIDE, height=40, width=160,x=180,y=5)
    
            
                Label(root3,text="NAME OF PASSENGER:",font='jokerman').place(x=50,y=60)
                Label(root3,text="AGE OF PASSENGER:",font='jokerman').place(x=50,y=90)
                Label(root3,text="GENDER:",font='jokerman').place(x=50,y=120)
                Label(root3,text="CATEGORY:",font='jokerman').place(x=50,y=150)
                Label(root3,text="FROM:",font='jokerman').place(x=50,y=180)
                Label(root3,text="TO:",font='jokerman').place(x=50,y=220)
                Label(root3,text="DATE OF JOURNEY:",font='jokerman').place(x=50,y=250)
                Label(root3,text="FLIGHTS:",font='jokerman').place(x=50,y=280)
                Label(root3,text="CLASS:",font='jokerman').place(x=50,y=310)
                Label(root3,text="MOBILE NO.:",font='jokerman').place(x=50,y=340)
            

            
                aa=StringVar(root3)
                bb=StringVar(root3)
                cc=StringVar(root3)
                dd=StringVar(root3)
                ee=StringVar(root3)
                ff=StringVar(root3)
                gg=StringVar(root3)
                hh=StringVar(root3)
                ii=StringVar(root3)
                jj=StringVar(root3)
                e1=Entry(root3,textvariable=aa).place(x=350,y=60)
                e2=Entry(root3,textvariable=bb).place(x=350,y=90)
                e3=Entry(root3,textvariable=cc).place(x=350,y=120)
                e4=Entry(root3,textvariable=dd).place(x=350,y=150)
                e5=Entry(root3,textvariable=ee).place(x=350,y=180)
                e6=Entry(root3,textvariable=ff).place(x=350,y=220)
                e7=Entry(root3,textvariable=gg).place(x=350,y=250)
                e8=Entry(root3,textvariable=hh).place(x=350,y=280)
                e9=Entry(root3,textvariable=ii).place(x=350,y=310)
                e10=Entry(root3,textvariable=jj).place(x=350,y=340)
            
                ename=aa.get()
                eage=bb.get()
                egender=cc.get()
                ecategory=dd.get()
                efrom=ee.get()
                eto=ff.get()
                edoj=gg.get()
                eflights=hh.get()
                eclass=ii.get()
                emob=jj.get()
                eno=v1.get()

                def update():
                    ename=aa.get()
                    eage=bb.get()
                    egender=cc.get()
                    ecategory=dd.get()
                    efrom=ee.get()
                    eto=ff.get()
                    edoj=gg.get()
                    eflights=hh.get()
                    eclass=ii.get()
                    emob=jj.get()            
                    eno=v1.get()
                    my_cur=db.cursor()
                    my_cur.execute('update bookt set ename=%s,eage=%s,egender=%s,ecategory=%s,efrom=%s,eto=%s,edoj=%s,eflights=%s,eclass=%s,emob=%s where eno=%s',(ename,eage,egender,ecategory,efrom,eto,edoj,eflights,eclass,emob,eno))
            
        
                    db.commit()
                    messagebox.askquestion("Confirm","Are you sure?")
                    messagebox.showinfo('DONE!','TICKET DETAILS UPDATED')
                    root3.destroy()
                    root7.destroy()
                
                def back():
                    root3.destroy()    
                Button(root3,text='UPDATE',font='jokerman',command=update).place(x=50,y=400)
                Button(root3,text='BACK',font='jokerman',command=back).place(x=250,y=400)

            Button(root7,text="PROCEED",font='jokerman',command=val).place(x=60,y=100)                
                


        
        
        b3=Button(root1,text='UPDATE_TICKETS',command=click2,bg='light salmon',bd=3,font='jokerman')
        b3.place(bordermode=OUTSIDE, height=50, width=160,x=10,y=65)


        def click3():
            root4=Tk()
            root4.title('AIR_ONLINE .LTD')
            root4.geometry('500x150')
            Label(root4,text="CANCEL PANEL",font='jokerman',bg='red',bd=2,relief=RAISED).place(bordermode=OUTSIDE, height=40, width=160,x=180,y=5)
    
            
            Label(root4,text="ENO:",font='jokerman').place(x=50,y=60)
            
            aa=StringVar(root4)
          
            e1=Entry(root4,textvariable=aa).place(x=350,y=60)
            eno=aa.get()


            
            def delete():
                eno=aa.get()
                eno=(eno,)
                my_cur=db.cursor()
                sql='delete from bookt where eno=%s'
                my_cur.execute(sql,eno)
        
                db.commit()
                messagebox.askquestion("Confirm","Are you sure?") 
                messagebox.showinfo('DONE!','Emp. Record Deleted')
                root4.destroy()

            def exitall():
                root1.destroy()
                root4.destroy()
                
            def back():
                root4.destroy()

                
            Button(root4,text='DELETE',font='jokerman',command=delete).place(x=50,y=100)
            Button(root4,text='EXITALL',font='jokerman',command=exitall).place(x=400,y=100)
            Button(root4,text='BACK',font='jokerman',command=back).place(x=220,y=100)
    

        b4=Button(root1,text='CANCEL_TICKETS',command=click3,bg='light salmon',bd=3,font='jokerman')
        b4.place(bordermode=OUTSIDE, height=50, width=160,x=10,y=120)


        def click4():

            root8=Tk()
            root8.title('AIR_ONLINE .LTD')
            v1=StringVar(root8)

            Label(root8,text='ENO:',font='jokerman').place(x=10,y=10)
            Entry(root8,textvariable=v1).place(x=55,y=10)
            print(v1)

            def val2():
                root8.destroy()
                if v1=='':
                    messagebox.showwarning("warning","PLEASE ENTER ENO")
                    click4()
                else:    
                    
                    messagebox.showinfo('DONE','DETAILS SEARCHED')
                    root5=Tk()
                    root5.title('AIR_ONLINE .LTD')
                    root5.geometry('500x500')
                    Label(root5,text="DETAILS",font='jokerman',bg='red',bd=2,relief=RAISED).place(bordermode=OUTSIDE, height=40, width=160,x=180,y=5)
    
            
                    Label(root5,text="NAME OF PASSENGER:",font='jokerman').place(x=50,y=60)
                    Label(root5,text="AGE OF PASSENGER:",font='jokerman').place(x=50,y=90)
                    Label(root5,text="GENDER:",font='jokerman').place(x=50,y=120)
                    Label(root5,text="CATEGORY:",font='jokerman').place(x=50,y=150)
                    Label(root5,text="FROM:",font='jokerman').place(x=50,y=180)
                    Label(root5,text="TO:",font='jokerman').place(x=50,y=220)
                    Label(root5,text="DATE OF JOURNEY:",font='jokerman').place(x=50,y=250)
                    Label(root5,text="FLIGHTS:",font='jokerman').place(x=50,y=280)
                    Label(root5,text="CLASS:",font='jokerman').place(x=50,y=310)
                    Label(root5,text="MOBILE NO.:",font='jokerman').place(x=50,y=340)

            
                    aa=StringVar(root5)
                    bb=StringVar(root5)
                    cc=StringVar(root5)
                    dd=StringVar(root5)
                    ee=StringVar(root5)
                    ff=StringVar(root5)
                    gg=StringVar(root5)
                    hh=StringVar(root5)
                    ii=StringVar(root5)
                    jj=StringVar(root5)
                    e1=Entry(root5,textvariable=aa).place(x=350,y=60)
                    e2=Entry(root5,textvariable=bb).place(x=350,y=90)
                    e3=Entry(root5,textvariable=cc).place(x=350,y=120)
                    e4=Entry(root5,textvariable=dd).place(x=350,y=150)
                    e5=Entry(root5,textvariable=ee).place(x=350,y=180)
                    e6=Entry(root5,textvariable=ff).place(x=350,y=220)
                    e7=Entry(root5,textvariable=gg).place(x=350,y=250)
                    e8=Entry(root5,textvariable=hh).place(x=350,y=280)
                    e9=Entry(root5,textvariable=ii).place(x=350,y=310)
                    e10=Entry(root5,textvariable=jj).place(x=350,y=340)
    
                    ename=aa.get()
                    eage=bb.get()
                    egender=cc.get()
                    ecategory=dd.get()
                    efrom=ee.get()
                    eto=ff.get()
                    edoj=gg.get()
                    eflights=hh.get()
                    eclass=ii.get()
                    emob=jj.get()
                    def search():
                        eno=v1.get()
                        eno=(eno,)
                        my_cur=db.cursor()
                        sql='select * from bookt where eno=%s'
                        my_cur.execute(sql,eno)
                        res=my_cur.fetchall()
                    
                        for x in res:
                            aa.set(x[0])
                            bb.set(x[1])
                            cc.set(x[2])
                            dd.set(x[3])
                            ee.set(x[4])
                            ff.set(x[5])
                            gg.set(x[6])
                            hh.set(x[7])
                            ii.set(x[8])
                            jj.set(x[9])

                    def exitall():
                        root1.destroy()
                        root5.destroy()
                        
                    def back():
                        root5.destroy()
    
                        
                    search()
                    Button(root5,text='EXITALL',font='jokerman',command=exitall).place(x=400,y=400)
                    Button(root5,text='BACK',font='jokerman',command=back).place(x=50,y=400)
    
          
            Button(root8,text="GET DETAILS",font='jokerman',command=val2).place(x=60,y=100)            
        

        b5=Button(root1,text='SEARCH_TICKETS',command=click4,bg='light salmon',bd=3,font='jokerman')
        b5.place(bordermode=OUTSIDE, height=50, width=160,x=10,y=175)

    
    b1=Button(root,text='click here',command=click,relief=RIDGE,bg='red',activeforeground = "blue",bd=3,font='jokerman')
    b1.pack(expand=0)
    
    
entry()

