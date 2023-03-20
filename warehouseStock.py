from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sqlite3 as sql

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.style=ttk.Style()
        self.lst=[]

        self.main()
        self.data_to_list()

    def main(self):

        self.h_stockImg = PhotoImage(file='image/headerStock.png')
        self.filterBtnImg = PhotoImage(file='image/filterBtnImg.png')
        self.searchBtnImg = PhotoImage(file='image/searchBtnImg.png')
        self.deleteBtnImg = PhotoImage(file='image/deleteBtnImg.png')

        self.geometry ('1400x800+250+100')
        self.configure (bg='#F3F3F3')

        self.l_headerStock=Label(self,image=self.h_stockImg)
        self.b_filterStock=Button(self,image=self.filterBtnImg,bd=0,activebackground='white',command=self.filter_stock)
        self.c_filterStock = ttk.Combobox(self,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["همه ی کالا ها","فلزات", "مواد غذایی"])
        self.c_filterStock.set("یک گزینه را انتخاب کنید")
        self.l_filterStock=Label(self,text=' : گروه کالا',font=('Lalezar',17))
        self.e_searchUser   = Entry(self,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUser= Button(self,bg='#F3F3F3',image=self.searchBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2')
        self.b_delete=Button(self,image=self.deleteBtnImg,bd=0,activebackground='white',cursor='hand2')

        #list
        self.listStock= ttk.Treeview(self,show='headings',height=15)

        self.listStock['columns']=('purchase','number','category','type','name','id','row')
        #columns
        # self.listKarmand.column('#0',width=0,stretch=NO)
        self.listStock.column('purchase',width=140,anchor=E)
        self.listStock.column('number',width=140,anchor=E)
        self.listStock.column('category',width=180,anchor=E)
        self.listStock.column('type',width=270,anchor=E)
        self.listStock.column('name',width=230,anchor=E)
        self.listStock.column('id',width=130,anchor=E)
        self.listStock.column('row',width=130,anchor=E)
        #heading
        # self.listKarmand.heading('#0',text='',anchor=E)
        self.listStock.heading('purchase',text=' : نقطه خرید',anchor=E)
        self.listStock.heading('number',text=' : تعداد',anchor=E)
        self.listStock.heading('category',text=' : گروه کالا',anchor=E)
        self.listStock.heading('type',text=' : نوع کالا',anchor=E)
        self.listStock.heading('name',text=' : نام کالا',anchor=E)
        self.listStock.heading('id',text=' : کد کالا',anchor=E)
        self.listStock.heading('row',text=' : ردیف',anchor=E)
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
        
        #___bind___
        self.listStock.bind('<ButtonRelease-1>', self.select_record)
        self.b_delete.bind('<Button-1>', self.delete_record)


        self.l_headerStock.place(x=580,y=0)
        self.b_filterStock.place(x=860,y=130)
        self.c_filterStock.place(x=1020,y=135)
        self.l_filterStock.place(x=1230,y=135)
        self.e_searchUser.place(x=245,y=135)
        self.b_searchUser.place(x=85,y=130)
        self.listStock.place(x=85,y=185)

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
                self.listStock.insert(parent='',index='end',text='',
                                    values=(i[4],i[7],i[3],i[2],i[1],i[0],str(self.count+1)))
                self.count += 1
    
    def select_record(self,event=None):
        self.selected = self.listStock.focus()
        self.values = self.listStock.item(self.selected , "values")
        self.row_id =self.listStock.identify_row(event.y)
        start = self.listStock.bbox(self.row_id, column=None)
        self.y1=start[1]+185
        self.b_delete.place(x=40,y=self.y1)

    def delete_record(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.code=self.values[5]
        self.cur.execute("DELETE FROM kala WHERE id='{}'" .format(self.code))
        self.con.commit()
        for item in self.listStock.get_children():
            self.listStock.delete(item)
        self.lst=[]
        self.data_to_list()
        self.b_delete.place(x=-50,y=-50)
    
    def filter_stock(self):
        self.filterLst=self.c_filterStock.get()
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.count=0
        if self.filterLst =="همه ی کالا ها":
            for item in self.listStock.get_children():
                self.listStock.delete(item)
            self.lst=[]
            self.data_to_list()
        elif self.filterLst !='یک گزینه را انتخاب کنید':
            for i in self.listStock.get_children():
                self.listStock.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE category="{}"'.format(self.filterLst))
            self.filter_list=list(self.row)
            for i in self.filter_list:
                self.listStock.insert(parent='',index='end',text='',
                                    values=(i[4],i[7],i[3],i[2],i[1],i[0],str(self.count+1)))
                self.count += 1
        

        

O=A()
O.mainloop()