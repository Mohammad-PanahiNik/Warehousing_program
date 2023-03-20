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
        self.y1=-50
        self.y2=-50

        self.main()
        self.data_to_list()

    def main(self):
        self.fildsBgImg    = PhotoImage(file='image/fildsBg.png')
        self.kalaImg      = PhotoImage(file='image/imgSelectorBg.png')
        self.listKalaBgImg = PhotoImage(file='image/listSkalaBg.png')
        self.searchBtnImg   = PhotoImage(file='image/searchBtnImg.png')
        self.h_sabtKalaImg = PhotoImage(file='image/headerSabtKala.png')
        self.addKalaBtnImg = PhotoImage(file='image/addKalaBtn.png')
        self.deleteBtnImg = PhotoImage(file='image/deleteBtnImg.png')
        self.editBtnImg = PhotoImage(file='image/editBtnImg.png')
        self.sabtTaghirBtn = PhotoImage(file='image/sabtEdit.png')

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
        self.l_groupType   = Label(self,text=' : گروه کالا',font=('Lalezar',17))
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
        self.b_delete=Button(self,image=self.deleteBtnImg,bd=0,activebackground='white',cursor='hand2')
        self.b_edit=Button(self,image=self.editBtnImg,bd=0,activebackground='white',cursor='hand2')
        self.b_sabtTaghirat=Button(self,image=self.sabtTaghirBtn,bd=0,activebackground='white')
        # self.b_delete=Button(self,image=self.deleteBtnImg,bd=0,activebackground='white')
        # self.b_edit=Button(self,image=self.editBtnImg,bd=0,activebackground='white')

        #list
        self.listKala= ttk.Treeview(self,show='headings',height=8)

        self.listKala['columns']=('Purchase','Category','Type','Name','id','row')
        #columns
        # self.listKala.column('#0',width=0,stretch=NO)
        self.listKala.column('Purchase',width=220,anchor=E)
        self.listKala.column('Category',width=220,anchor=E)
        self.listKala.column('Type',width=220,anchor=E)
        self.listKala.column('Name',width=220,anchor=E)
        self.listKala.column('id',width=200,anchor=E)
        self.listKala.column('row',width=150,anchor=E)
        #heading
        # self.listKala.heading('#0',text='',anchor=E)
        self.listKala.heading('Purchase',text=' : نقطه خرید',anchor=E)
        self.listKala.heading('Category',text=' : گروه کالا',anchor=E)
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
        self.l_groupType.place   (x=1235 , y=250)
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
        self.b_sabtTaghirat.place(x=-100,y=-100)

        # self.b_delete.place      (x=0 , y=0)
        # self.b_edit.place        (x=0 , y=0)
        
        # self.b_delete.place_forget()
        # self.b_edit.place_forget()
        #____
        # self.productIdBg.place   (x=1000 , y=80)
        # self.productNameBg.place (x=380 , y=80)
        # self.productTypeBg.place (x=1000 , y=175)
        # self.groupTypeBg.place   (x=380 , y=175)
        # self.descriptionBg.place (x=890 , y=275)
        # self.purchaseBg.place    (x=380 , y=275)
        # self.searchBg.place      (x=130 , y=360)

        #_____ bind _____
        self.e_productId.focus()
        self.e_productId.bind('<Return>',lambda event : self.e_productName.focus())
        self.e_productName.bind('<Return>',lambda event : self.e_purchase.focus())
        self.e_purchase.bind('<Return>',lambda event : self.e_description.focus())
        self.e_description.bind('<Return>',lambda event : self.b_addKala.focus())
        self.e_search.bind('<Return>',lambda event : self.b_search.focus())
        self.b_search.bind('<Return>', self.search_id)
        self.b_addKala.bind('<Return>', self.funcAddKala)
        self.imgSelectorBg.bind('<Button-1>', self.funcAddImg)
        self.listKala.bind('<ButtonRelease-1>', self.select_record)
        self.b_delete.bind('<Button-1>', self.delete_record)
        self.b_edit.bind('<ButtonRelease-1>', self.edit_record_values)
        self.b_sabtTaghirat.bind('<Button-1>', self.edit)

        #_______ hover button ________
        self.e_search.insert(0,'جستجو کد کالا  ')
        self.e_search.bind('<Button-1>',lambda event :self.e_search.delete(0,END))
        self.b_search.bind('<Enter>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImgH.png'))
        self.b_search.bind('<Leave>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImg.png'))
        self.b_delete.bind('<Enter>',lambda event : self.funcBtnHover(self.deleteBtnImg,'image/deleteBtnImgH.png'))
        self.b_delete.bind('<Leave>',lambda event : self.funcBtnHover(self.deleteBtnImg,'image/deleteBtnImg.png'))
        self.b_edit.bind('<Enter>',lambda event : self.funcBtnHover(self.editBtnImg,'image/editBtnImgH.png'))
        self.b_edit.bind('<Leave>',lambda event : self.funcBtnHover(self.editBtnImg,'image/editBtnImg.png'))

    def data_to_list(self):
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kala'")
        
        self.result = self.cur.fetchone()
        if self.result != None:
            
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
        self.c_productType.set("یک گزینه را انتخاب کنید")
        self.c_groupType.set("یک گزینه را انتخاب کنید")
        self.e_purchase.delete(0,END)
        self.e_description.delete(0,END)
        self.kalaImg['file']='image/imgSelectorBg.png'
        self.e_productId.focus()

        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.data=(self.productId,self.productName,self.productType,self.groupType,self.purchase,self.description,self.photo,'0')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS kala (id TEXT PRIMARY KEY NOT NULL ,name TEXT NOT NULL ,type TEXT NOT NULL,category TEXT NOT NULL
        ,purchase INTEGER NOT NULL,description TEXT NOT NULL,photo BLOB NOT NULL,stock)''')
        self.cur.execute('INSERT INTO kala(id,name,type,category,purchase,description,photo,stock) VALUES(?,?,?,?,?,?,?,?)',self.data)
        self.con.commit()
        self.numlist=len(self.listKala.get_children())
        self.listKala.insert(parent='',index='end',text='',values=(self.purchase,self.groupType,self.productType,
                                                                                  self.productName,self.productId,self.numlist+1))

    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
    
    def search_id(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idKala=self.e_search.get()
        self.count=0
        if self.idKala !='':
            for i in self.listKala.get_children():
                self.listKala.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala))
            self.search_list=list(self.row)
            self.listKala.insert(parent='',index='end',iid=self.count,text='',
                                    values=(self.search_list[0][4],self.search_list[0][3],self.search_list[0][2],
                                            self.search_list[0][1],self.search_list[0][0],str(self.count+1)))
            
        else:
            self.lst=[]
            self.listKala.delete('0')
            self.data_to_list()

    def select_record(self,event=None):
        self.selected = self.listKala.focus()
        self.values = self.listKala.item(self.selected , "values")
        self.row_id =self.listKala.identify_row(event.y)
        start = self.listKala.bbox(self.row_id, column=None)
        self.y1=start[1]+400
        self.y2=start[1]+440
        self.b_delete.place(x=40,y=self.y1)
        self.b_edit.place(x=40,y=self.y2)

    def delete_record(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.code=self.values[4]
        self.cur.execute("DELETE FROM kala WHERE id='{}'" .format(self.code))
        self.con.commit()
        for item in self.listKala.get_children():
            self.listKala.delete(item)
        self.lst=[]
        self.data_to_list()
        self.b_delete.place(x=-50,y=-50)
        self.b_edit.place(x=-50,y=-50)

    def sql_search(self,id1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        self.cur.execute("SELECT COUNT(*) FROM kala")
        self.rowNum = self.cur.fetchone()[0]
        row = cur.execute('SELECT * FROM kala WHERE id="{}"'.format(id1))
        return list(row)
    
    def edit_record_values(self ,event=None):
        self.e_productId.delete(0,END)
        self.e_productName.delete(0,END)
        self.c_groupType.set("یک گزینه را انتخاب کنید")
        self.c_productType.set("یک گزینه را انتخاب کنید")
        self.e_purchase.delete(0,END)
        self.e_description.delete(0,END)

        self.values = self.listKala.item(self.selected , "values")
        self.row_num=self.values[5]
        self.valuelst = self.sql_search(self.values[4])
        # self.cur('SELECT * FROM Blob WHERE id={}'.format(self.valuelst[0][6]))
        print('salmmmm')
        print(self.values[0])
        self.e_productId.insert(0,self.valuelst[0][0])
        self.e_productName.insert(0,self.valuelst[0][1])
        self.c_productType.set(self.valuelst[0][2])
        self.c_groupType.set(self.valuelst[0][3])
        self.e_purchase.insert(0,self.valuelst[0][4])
        self.e_description.insert(0,self.valuelst[0][5])
        self.b_sabtTaghirat.place(x=910,y=340)


    def edit(self,event = None):
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.code = self.e_productId.get()
        self.name = self.e_productName.get()
        self.point = self.e_purchase.get()
        self.desc = self.e_description.get()
        self.type = self.c_productType.get()
        self.group = self.c_groupType.get()
        self.listKala.item(self.selected ,values = (self.point,self.group,self.type,self.name,self.code,self.row_num))
        print(self.values)
        self.cur.execute(''' UPDATE kala SET id = "{}" , name = "{}", type = "{}",category = "{}",
        purchase = "{}",description = "{}" WHERE id="{}" '''.format(self.code,self.name,self.type,self.group,self.point,self.desc,self.values[4]))
        self.con.commit()
        self.b_sabtTaghirat.place(x=-100,y=-100)
        self.b_delete.place(x=-50,y=-50)
        self.b_edit.place(x=-50,y=-50)
        # self.kalaImg['file']=self.valuelst[0][6]
    # def sql_update(self):
    #     self.con = sql.connect('mydb.db')
    #     self.cur = self.con.cursor()
    #     self.dastor =' UPDATE kala SET id = "{}" , name = "{}", type = "{}",category = "{}", purchase = "{}",description = "{}" WHERE id="{}" '.format(self.code,self.name,self.type,self.group,self.point,self.des,self.values[3])
    #     self.cur.execute(self.dastor)
    #     self.con.commit()
    #     self.b_sabtTaghirat.place(x=-100,y=-100)
    #     self.b_delete.place(x=-50,y=-50)
    #     self.b_edit.place(x=-50,y=-50)

    def funcBtnHover(self,img,url):
        img['file'] = url

O=A()
O.mainloop()