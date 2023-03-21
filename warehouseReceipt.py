from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sqlite3 as sql

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.permission=False
        self.fullname=''
        self.style=ttk.Style()
        self.main()

    def main(self):
        self.headerVorodKalaImg = PhotoImage(file='image/headerReciept.png')
        self.searchBtnImg = PhotoImage(file='image/searchBtnImg.png')
        self.kalaImg = PhotoImage(file='image/imgSelectorBg.png')
        self.addKalaNumImg = PhotoImage(file='image/addKalaNum.png')
        
        self.geometry  ('1400x800+250+100')
        self.configure (bg='#F3F3F3')

        self.searchUserFrm = LabelFrame(bg='#DFDFDF',width=1410,height=170,bd=5,relief=SOLID)
        self.h_vorodKala = Label(self.searchUserFrm,image=self.headerVorodKalaImg)
        self.l_attention = Label(self.searchUserFrm,text='.توجه : لطفا ابتدا کد ملی متقاضی مورد نظر را وارد کنید',font=('Lalezar',17),bg='#DFDFDF')
        self.e_searchUser  = Entry(self.searchUserFrm,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUser = Button(self.searchUserFrm,bg='#DFDFDF',image=self.searchBtnImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.search_idUser)
        self.e_searchKala = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid',fg='#717171')
        self.e_searchKala.insert(0,'جستجوی کد کالا')
        self.b_searchKala = Button(self,bg='#DFDFDF',image=self.searchBtnImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.search_idKala)
        self.infoKalaFrm = LabelFrame(bg='#EAEAEA',width=1230,height=240,bd=5,relief=SOLID)
        self.l_nameUser = Label(self,text=' : نام',font=('Lalezar',17),bg='#EAEAEA')
        self.nameUserLbl = Label(self,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_nameKala = Label(self,text=' : نام کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.nameKalaLbl = Label(self,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_kalaType = Label(self,text=' : نوع کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.kalaTypeLbl =Label(self,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_lastUser = Label(self,text=' : نام خانوادگی',font=('Lalezar',17),bg='#EAEAEA')
        self.lastUserLbl = Label(self,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_kalaId = Label(self,text=' : کد کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.kalaIdLbl = Label(self,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_groupKala = Label(self,text=' : گروه کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.groupKalaLbl = Label(self,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_imgSelector = Label(self,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg = Label(self,bg='#F3F3F3',image=self.kalaImg,cursor='hand2',width=150,height=150)
        self.kalaNumFrm = LabelFrame(bg='#EAEAEA',width=540,height=70,bd=5,relief=SOLID) 
        self.kalaNum = Label(self.kalaNumFrm,text=' : تعداد کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.e_kalaNum = Entry(self.kalaNumFrm,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid',fg='#717171')
        self.b_addKalaNum = Button(self.kalaNumFrm,bg='#DFDFDF',image=self.addKalaNumImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.funcAddNum)
        #list
        self.listReceipt= ttk.Treeview(self,show='headings',height=5)

        self.listReceipt['columns']=('date','kalaNum','kalaId','groupKala','kalaType','kalaName','fullname','row')
        #columns
        # self.listKarmand.column('#0',width=0,stretch=NO)
        self.listReceipt.column('date',width=150,anchor=E)
        self.listReceipt.column('kalaNum',width=90,anchor=E)
        self.listReceipt.column('groupKala',width=200,anchor=E)
        self.listReceipt.column('kalaType',width=200,anchor=E)
        self.listReceipt.column('kalaId',width=90,anchor=E)
        self.listReceipt.column('kalaName',width=200,anchor=E)
        self.listReceipt.column('fullname',width=200,anchor=E)
        self.listReceipt.column('row',width=100,anchor=E)
        #heading
        # self.listKarmand.heading('#0',text='',anchor=E)
        self.listReceipt.heading('date',text=' : تاریخ',anchor=E)
        self.listReceipt.heading('kalaNum',text=' : تعداد',anchor=E)
        self.listReceipt.heading('groupKala',text=' : گروه کالا',anchor=E)
        self.listReceipt.heading('kalaType',text=' : نوع کالا',anchor=E)
        self.listReceipt.heading('kalaId',text=' : کد کالا',anchor=E)
        self.listReceipt.heading('kalaName',text=' : نام کالا',anchor=E)
        self.listReceipt.heading('fullname',text=' : نام و نام خانوادگی',anchor=E)
        self.listReceipt.heading('row',text=' : ردیف',anchor=E)
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading",font=('Lalezar', 18),
                            padding=[0, 5, 15, 5],background='#474A56',
                            foreground="white",bd=0,relief='raised'
                            )
        self.style.map("Treeview.Heading",
            background=[('active','#686A75')])
        self.style.configure("Treeview", highlightthickness=0, 
                            height=150,
                            bd=0, font=('AraFProgram', 16),
                            background="white",foreground="black",
                            rowheight = 35,fieldbackground="white"
                            )
        self.style.map("Treeview",
            background=[('selected', '#7A8BA7')],
            foreground=[('selected', 'white')])
        
        #____bind____
        self.e_searchUser.focus()
        self.e_searchUser.bind('<Return>',lambda event:self.b_searchUser.focus())
        self.b_searchUser.bind('<Return>',self.search_idUser)
        self.e_searchKala.bind('<Button-1>',lambda event:self.e_searchKala.delete(0,END))
        self.e_searchKala.bind('<Return>',lambda event:self.b_searchKala.focus())
        self.b_searchKala.bind('<Return>',self.search_idKala)
        self.e_kalaNum.bind('<Return>',lambda event:self.b_addKalaNum.focus())
        self.b_addKalaNum.bind('<Return>',self.funcAddNum)


        self.h_vorodKala.place(x=610,y=0)
        self.searchUserFrm.place(x=-5,y=-10)
        self.l_attention.place(x=690,y=90)
        self.e_searchUser.place(x=475,y=90)
        self.b_searchUser.place(x=315,y=85)
        self.e_searchKala.place(x=1115,y=175)
        self.b_searchKala.place(x=955,y=170)
        self.infoKalaFrm.place(x=85,y=225)
        self.l_nameUser.place(x=1240,y=280)
        self.nameUserLbl.place(x=1025,y=280)
        self.l_nameKala.place(x=1210,y=360)
        self.nameKalaLbl.place(x=1025,y=360)
        self.l_lastUser.place(x=860,y=280)
        self.lastUserLbl.place(x=675,y=280)
        self.l_kalaId.place(x=900,y=360)
        self.kalaIdLbl.place(x=675,y=360)
        self.l_kalaType.place(x=515,y=280)
        self.kalaTypeLbl.place(x=330,y=280)
        self.l_groupKala.place(x=520,y=360)
        self.groupKalaLbl.place(x=330,y=360)
        self.l_imgSelector.place(x=135,y=390)
        self.imgSelectorBg.place(x=110,y=240)
        self.kalaNumFrm.place(x=775,y=460)
        self.kalaNum.place(x=400,y=10)
        self.e_kalaNum.place(x=180,y=10)
        self.b_addKalaNum.place(x=15,y=5)
        self.listReceipt.place(x=85,y=545)


    def search_idUser(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.nationalId=self.e_searchUser.get()
        self.count=0
        if self.nationalId != '':
            self.row=self.cur.execute('SELECT * FROM user WHERE national_code="{}"'.format(self.nationalId))
            self.userInfo=list(self.row)
            if self.userInfo[0][6]=='فروشنده':
                self.permission=True
                self.nameUserLbl['text']=self.userInfo[0][1]
                self.lastUserLbl['text']=self.userInfo[0][2]
                self.fullname=self.userInfo[0][1]+' '+self.userInfo[0][2]

    def search_idKala(self,event=None):
        if self.permission==True:
            self.idKala=self.e_searchKala.get()
            if self.idKala !='':
                self.con=sql.connect('mydb.db')
                self.cur=self.con.cursor()
                self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala))
                self.kalaInfo=list(self.row)
                self.nameKalaLbl['text']=self.kalaInfo[0][1]
                self.kalaTypeLbl['text']=self.kalaInfo[0][2]
                self.kalaIdLbl['text']=self.kalaInfo[0][0]
                self.groupKalaLbl['text']=self.kalaInfo[0][3]

    def funcAddNum(self,event=None):
        self.count=1
        self.kalaNumber=self.e_kalaNum.get()
        self.cur.execute(''' UPDATE kala SET stock = "{}" WHERE id="{}" '''.format(self.kalaNumber,self.idKala))
        self.con.commit()
        self.listReceipt.insert(parent='',index='end',text='',
                                    values=('01/01',self.kalaNumber,self.kalaInfo[0][0],
                                            self.kalaInfo[0][3],self.kalaInfo[0][2],self.kalaInfo[0][1],self.fullname,self.count))
        self.count += 1
        self.e_kalaNum.delete(0,END)
        self.e_searchKala.delete(0,END)
        self.e_searchUser.delete(0,END)
        self.kalaInfo=[]
        self.fullname=''
        self.nameKalaLbl['text']=''
        self.kalaTypeLbl['text']=''
        self.kalaIdLbl['text']=''
        self.groupKalaLbl['text']=''
        self.nameUserLbl['text']=''
        self.lastUserLbl['text']=''
        self.permission=False

O=A()
O.mainloop()