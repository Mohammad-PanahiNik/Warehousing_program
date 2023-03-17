from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sqlite3 as sql


class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.style=ttk.Style()
        self.lst=[]
        self.search_list=[]

        self.main()
        self.data_to_list()

    def main(self):
        self.fildsBgImg    = PhotoImage(file='image/fildsBg.png')
        self.kalaImg      = PhotoImage(file='image/imgSelectorBg.png')
        self.listKalaBgImg = PhotoImage(file='image/listSkalaBg.png')
        self.searchBtnImg   = PhotoImage(file='image/searchBtnImg.png')
        self.h_sabtKalaImg = PhotoImage(file='image/headerSabtKala.png')
        self.addKalaBtnImg = PhotoImage(file='image/addKalaBtn.png')

        self.geometry  ('1400x800+250+100')
        self.configure (bg='#F3F3F3')

        self.h_sabtKala    = Label(self,image=self.h_sabtKalaImg)
        self.l_productId   = Label(self,text=' : کد کالا',font=('Lalezar',17))
        self.e_productId   = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_productName = Label(self,text=' : نام کالا',font=('Lalezar',17))
        self.e_productName = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_productType = Label(self,text=' : نوع کالا',font=('Lalezar',17))
        self.c_productType = ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                            justify = 'right',values=["مواد خام", "کالای خریداری شده",
                                            "کالای توید شده اولیه", "کالای تولید شده برای فروش"])
        self.l_groupType   = Label(self,text=' : نام گروه کالا',font=('Lalezar',17))
        self.c_groupType   = ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["فلزات", "مواد غذایی"])
        self.c_productType.set("یک گزینه را انتخاب کنید")
        self.c_groupType.set("یک گزینه را انتخاب کنید")
        self.l_description = Label(self,text=' : توضیحات',font=('Lalezar',17))
        self.e_description = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=28,relief='solid')
        self.l_purchase    = Label(self,text=' : نقطه خرید',font=('Lalezar',17))
        self.e_purchase    = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_imgSelector = Label(self,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg = Label(self,bg='#F3F3F3',image=self.kalaImg,cursor='hand2',width=150,height=150)
        self.e_search      = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_search      = Button(self,bg='#F3F3F3',image=self.searchBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.search_id)
        self.b_addKala     = Button(self,bg='#F3F3F3',image=self.addKalaBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.funcAddKala)
        self.listKalaBg    = Label(self,bg='white',image=self.listKalaBgImg)

        #list
        self.listKala= ttk.Treeview(self,show='headings',height=8)

        self.listKala['columns']=('Purchase','Category','Type','Name','id','row')
        #columns
        self.listKala.column('#0',width=0,stretch=NO)
        self.listKala.column('Purchase',width=220,anchor=E)
        self.listKala.column('Category',width=220,anchor=E)
        self.listKala.column('Type',width=220,anchor=E)
        self.listKala.column('Name',width=220,anchor=E)
        self.listKala.column('id',width=200,anchor=E)
        self.listKala.column('row',width=150,anchor=E)
        #heading
        self.listKala.heading('#0',text='',anchor=E)
        self.listKala.heading('Purchase',text=' : گروه کالا',anchor=E)
        self.listKala.heading('Category',text=' : نوع بسته بندی',anchor=E)
        self.listKala.heading('Type',text=' : نوع کالا',anchor=E)
        self.listKala.heading('Name',text=' : نام کالا',anchor=E)
        self.listKala.heading('id',text=' : کد کالا',anchor=E)
        self.listKala.heading('row',text=' : ردیف',anchor=E)
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
        #___________
        # self.productIdBg   = Label(self,bg='#F3F3F3',image=self.fildImg1)
        # self.productNameBg = Label(self,bg='#F3F3F3',image=self.fildImg1)
        # self.productTypeBg = Label(self,bg='#F3F3F3',image=self.fildImg1)
        # self.groupTypeBg   = Label(self,bg='#F3F3F3',image=self.fildImg1)
        # self.descriptionBg = Label(self,bg='#F3F3F3',image=self.fildImg3)
        # self.purchaseBg    = Label(self,bg='#F3F3F3',image=self.fildImg1)
        # self.searchBg      = Label(self,bg='#F3F3F3',image=self.fildImg1)

        self.h_sabtKala.place    (x=580 , y=0)
        self.l_productId.place   (x=1245 , y=100)
        self.e_productId.place   (x=985 , y=105)
        self.l_productName.place (x=840 , y=100)
        self.e_productName.place (x=585 , y=100)
        self.l_productType.place (x=1240 , y=178)
        self.c_productType.place (x=985 , y=178)
        self.l_groupType.place   (x=1200 , y=250)
        self.c_groupType.place   (x=985 , y=250)
        self.l_description.place (x=820 , y=250)
        self.e_description.place (x=475 , y=250)
        self.l_purchase.place    (x=820 , y=180)
        self.e_purchase.place    (x=585 , y=180)
        self.l_imgSelector.place (x=210 , y=260)
        self.imgSelectorBg.place (x=190 , y=100)
        self.e_search.place      (x=245 , y=375)
        self.b_search.place      (x=85 , y=370)
        self.b_addKala.place     (x=1120 , y=340)
        self.listKala.place      (x=85 , y=420)

        #____
        # self.productIdBg.place   (x=1000 , y=80)
        # self.productNameBg.place (x=380 , y=80)
        # self.productTypeBg.place (x=1000 , y=175)
        # self.groupTypeBg.place   (x=380 , y=175)
        # self.descriptionBg.place (x=890 , y=275)
        # self.purchaseBg.place    (x=380 , y=275)
        # self.searchBg.place      (x=130 , y=360)

        #_____bind_____
        self.e_productId.focus()
        self.e_productId.bind     ('<Return>',lambda event : self.e_productName.focus())
        self.e_productName.bind     ('<Return>',lambda event : self.e_purchase.focus())
        self.e_purchase.bind     ('<Return>',lambda event : self.e_description.focus())
        self.e_description.bind     ('<Return>',lambda event : self.b_addKala.focus())
        self.b_addKala.bind     ('<Return>', self.funcAddKala)
        self.imgSelectorBg.bind     ('<Button-1>', self.funcAddImg)

        self.e_search.insert(0,'جستجو کد کالا  ')
        self.e_search.bind('<Button-1>',lambda event :self.e_search.delete(0,END))
        self.b_addKala.bind('<Enter>',lambda event : self.funcBtnHover(self.addKalaBtnImg,'image/addKalaBtnH.png'))
        self.b_addKala.bind('<Leave>',lambda event : self.funcBtnHover(self.addKalaBtnImg,'image/addKalaBtn.png'))
        self.b_search.bind('<Enter>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImgH.png'))
        self.b_search.bind('<Leave>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImg.png'))

    def data_to_list(self):
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        row=self.cur.execute('SELECT * FROM kala')
        for i in row :
            self.lst.append(i)
        
        for i in self.lst:
            self.listKala.insert(parent='',index='end',iid=self.count,text='',
                                 values=(i[4],i[3],i[2],i[1],i[0],str(self.count+1)))
            self.count += 1

    def funcAddImg(self,event=None):
        self.img_name = filedialog.askopenfilename()
        self.kalaImg['file']= self.img_name
    
    def funcAddKala(self , event=None):
        self.productId=self.e_productId.get()
        self.productName=self.e_productName.get()
        self.productType=self.c_productType.get()
        self.groupType=self.c_groupType.get()
        self.purchase=self.e_purchase.get()
        self.description=self.e_description.get()
        self.photo = self.covert_to_binary_data(self.img_name)

        self.e_productId.delete(0,END)
        self.e_productName.delete(0,END)
        self.c_productType.set('')
        self.c_groupType.set('')
        self.e_purchase.delete(0,END)
        self.e_description.delete(0,END)
        self.kalaImg['file']='image/imgSelectorBg.png'
        self.e_productId.focus()

        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data=(self.productId,self.productName,self.productType,self.groupType,self.purchase,self.description,self.photo)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS kala (id PRIMARY KEY NOT NULL ,name TEXT NOT NULL ,type TEXT NOT NULL,category TEXT NOT NULL
        ,purchase INTEGER NOT NULL,description TEXT NOT NULL,photo BLOB NOT NULL)''')
        self.cur.execute('INSERT INTO kala(id,name,type,category,purchase,description,photo) VALUES(?,?,?,?,?,?,?)',self.data)
        self.con.commit()

    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
    
    def search_id(self):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idKala=self.e_search.get()
        self.count=0
        if self.idKala !='':
            for i in self.listKala.get_children():
                self.listKala.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala))
            self.search_list=list(self.row)
            print(len(self.search_list))
            self.listKala.insert(parent='',index='end',iid=self.count,text='',
                                    values=(self.search_list[0][4],self.search_list[0][3],self.search_list[0][2],
                                            self.search_list[0][1],self.search_list[0][0],str(self.count+1)))
        else:
            self.lst=[]
            self.listKala.delete('0')
            self.data_to_list()

    def funcBtnHover(self,img,url):
        img['file'] = url

O=A()
O.mainloop()