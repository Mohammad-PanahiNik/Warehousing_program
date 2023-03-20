from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sqlite3 as sql

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.lst=[]
        self.search_list=[]

        self.style=ttk.Style()
        self.main()
        self.data_to_list()


    def main(self):
        self.hSabtUserImg = PhotoImage(file='image/headerSabtKarmandImg.png')
        self.UserImg = PhotoImage(file='image/imgSelectorBg.png')
        self.searchBtnImg   = PhotoImage(file='image/searchBtnImg.png')
        self.addPesonnelImg = PhotoImage(file='image/addPesonnelBtnImg.png')
        self.geometry ('1400x800+250+100')
        self.configure (bg='#F3F3F3')
    
        self.l_headerUser=Label(self,image=self.hSabtUserImg)
        self.l_nameUser=Label(self,text=' : نام',font=('Lalezar',17))
        self.e_nameUser=Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_lastUser=Label(self,text=' : نام خانوادگی',font=('Lalezar',17))
        self.e_lastUser=Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_nationalCode=Label(self,text=' : کد ملی',font=('Lalezar',17))
        self.e_nationalCode=Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_gender=Label(self,text=' : جنسیت',font=('Lalezar',17))
        self.c_gender=ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["زن", "مرد"])
        self.c_gender.set("یک گزینه را انتخاب کنید")
        self.l_phoneNum=Label(self,text=' : شماره تماس',font=('Lalezar',17))
        self.e_phoneNum=Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_accountType=Label(self,text=' : نوع کاربری',font=('Lalezar',17))
        self.c_accountType=ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["کارمند","ادمین", "مدیر"])
        self.c_accountType.set("یک گزینه را انتخاب کنید")
        self.l_personnelId=Label(self,text=' : کد کارمند',font=('Lalezar',17))
        self.e_personnelId=Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_UserPass=Label(self,text=' : رمزعبور',font=('Lalezar',17))
        self.e_UserPass=Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_imgSelector = Label(self,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg = Label(self,bg='#F3F3F3',image=self.UserImg,cursor='hand2',width=150,height=150)
        self.b_addPesonnel= Button(self,bg='#F3F3F3',image=self.addPesonnelImg,activebackground='#F3F3F3',bd=0,cursor='hand2')
        self.e_searchUser   = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUser= Button(self,bg='#F3F3F3',image=self.searchBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.search_id)
        
        #list
        self.listUser= ttk.Treeview(self,show='headings',height=8)

        self.listUser['columns']=('type','phoneNum','nationalCode','last','name','personnelId','row')
        #columns
        # self.listKarmand.column('#0',width=0,stretch=NO)
        self.listUser.column('type',width=200,anchor=E)
        self.listUser.column('phoneNum',width=200,anchor=E)
        self.listUser.column('nationalCode',width=200,anchor=E)
        self.listUser.column('last',width=200,anchor=E)
        self.listUser.column('name',width=200,anchor=E)
        self.listUser.column('personnelId',width=150,anchor=E)
        self.listUser.column('row',width=100,anchor=E)
        #heading
        # self.listKarmand.heading('#0',text='',anchor=E)
        self.listUser.heading('type',text=' : نوع کاربر',anchor=E)
        self.listUser.heading('phoneNum',text=' : شماره تماس',anchor=E)
        self.listUser.heading('nationalCode',text=' : کد ملی',anchor=E)
        self.listUser.heading('last',text=' : نام خانوادگی',anchor=E)
        self.listUser.heading('name',text=' : نام',anchor=E)
        self.listUser.heading('personnelId',text=' : کد کارمندی',anchor=E)
        self.listUser.heading('row',text=' : ردیف',anchor=E)
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



        self.l_headerUser.place(x=595,y=0)
        self.l_nameUser.place(x=1315,y=100)
        self.e_nameUser.place(x=1015,y=100)
        self.l_lastUser.place(x=1245,y=175)
        self.e_lastUser.place(x=1015,y=175)
        self.l_nationalCode.place(x=1285,y=255)
        self.e_nationalCode.place(x=1015,y=255)
        self.l_gender.place(x=885,y=100)
        self.c_gender.place(x=630,y=100)
        self.l_phoneNum.place(x=855,y=175)
        self.e_phoneNum.place(x=630,y=175)
        self.l_accountType.place(x=865,y=250)
        self.c_accountType.place(x=630,y=250)
        self.l_personnelId.place(x=470,y=100)
        self.e_personnelId.place(x=245,y=100)
        self.l_UserPass.place(x=480,y=175)
        self.e_UserPass.place(x=245,y=175)
        self.l_imgSelector.place(x=55,y=260)
        self.imgSelectorBg.place(x=45,y=100)
        self.b_addPesonnel.place(x=1160,y=330)
        self.listUser.place(x=75,y=420)
        self.b_searchUser.place(x=75,y=370)
        self.e_searchUser.place(x=240,y=375)

        #_____ bind _____
        self.e_nameUser.focus()
        self.e_nameUser.bind('<Return>',lambda event : self.e_lastUser.focus())
        self.e_lastUser.bind('<Return>',lambda event : self.e_nationalCode.focus())
        self.e_nationalCode.bind('<Return>',lambda event : self.e_phoneNum.focus())
        self.e_phoneNum.bind('<Return>',lambda event : self.e_personnelId.focus())
        self.e_personnelId.bind('<Return>',lambda event : self.e_UserPass.focus())
        self.e_UserPass.bind('<Return>',lambda event : self.e_UserPass.focus())
        self.e_UserPass.bind('<Return>',lambda event : self.funcAddUser)
        self.b_addPesonnel.bind('<Button-1>',self.funcAddUser)
        self.imgSelectorBg.bind('<Button-1>', self.funcAddImg)


    def funcAddImg(self,event=None):
        self.img_name = filedialog.askopenfilename()
        self.UserImg['file']= self.img_name

    def funcBtnHover(self,img,url):
        img['file'] = url

    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
    
    def data_to_list(self):
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
        
        self.result = self.cur.fetchone()
        if self.result != None:
            row=self.cur.execute('SELECT * FROM user')
            for i in row :
                self.lst.append(i)
            
            for i in self.lst:
                self.listUser.insert(parent='',index='end',iid=self.count,text='',
                                    values=(i[4],i[3],i[2],i[1],i[0],str(self.count+1)))
                self.count += 1

    def data_to_list(self):
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kala'")
        
        self.result = self.cur.fetchone()
        if self.result != None:
            
            row=self.cur.execute('SELECT * FROM user')
            for i in row :
                self.lst.append(i)
            
            for i in self.lst:
                self.listUser.insert(parent='',index='end',iid=self.count,text='',
                                    values=(i[4],i[3],i[2],i[1],i[0],str(self.count+1)))
                self.count += 1

    def funcAddUser(self , event=None):
        self.pesonnelName=self.e_nameUser.get()
        self.pesonnelLast=self.e_lastUser.get()
        self.nationalCode=self.e_nationalCode.get()
        self.gender=self.c_gender.get()
        self.phoneNum=self.e_phoneNum.get()
        self.accountType=self.c_accountType.get()
        self.personnelId=self.e_personnelId.get()
        self.personnelPass=self.e_UserPass.get()
        self.photo = self.covert_to_binary_data(self.img_name)

        self.e_nameUser.delete(0,END)
        self.e_lastUser.delete(0,END)
        self.e_nationalCode.delete(0,END)
        self.c_gender.set("یک گزینه را انتخاب کنید")
        self.e_phoneNum.delete(0,END)
        self.c_accountType.set("یک گزینه را انتخاب کنید")
        self.e_personnelId.delete(0,END)
        self.e_UserPass.delete(0,END)
        self.UserImg['file']='image/imgSelectorBg.png'
        self.e_nameUser.focus()

        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data=(self.personnelId,self.pesonnelName,self.pesonnelLast,self.nationalCode,self.gender,self.phoneNum,self.accountType,self.personnelPass,self.photo)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user (id TEXT PRIMARY KEY NOT NULL ,name TEXT NOT NULL ,last_name TEXT NOT NULL,national_code TEXT NOT NULL
        ,gender INTEGER NOT NULL,phone_number TEXT NOT NULL,account_type TEXT NOT NULL,personnel_pass TEXT NOT NULL,photo BLOB NOT NULL)''')
        self.cur.execute('INSERT INTO user(id,name,last_name,national_code,gender,phone_number,account_type,personnel_pass,photo) VALUES(?,?,?,?,?,?,?,?,?)',self.data)
        self.con.commit()
        self.numlist=len(self.listUser.get_children())
        self.listUser.insert(parent='',index='end',text='',values=(self.accountType,self.phoneNum,self.accountType,
                                                                    self.pesonnelLast,self.pesonnelName,self.personnelId,self.numlist+1))
    
    def search_id(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idUser=self.e_searchUser.get()
        self.count=0
        if self.idUser !='':
            for i in self.listUser.get_children():
                self.listUser.delete(i)
            self.row=self.cur.execute('SELECT * FROM user WHERE id="{}"'.format(self.idUser))
            self.search_list=list(self.row)
            self.listUser.insert(parent='',index='end',iid=self.count,text='',
                                    values=(self.search_list[0][4],self.search_list[0][3],self.search_list[0][2],
                                            self.search_list[0][1],self.search_list[0][0],str(self.count+1)))
        else:
            self.lst=[]
            self.listUser.delete('0')
            self.data_to_list()

O=A()
O.mainloop()