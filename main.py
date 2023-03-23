from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sqlite3 as sql
from tkinter import messagebox
import uuid
import time
import math

main_page = Tk()
register_page = Toplevel()
loginn_page = Toplevel()
product_page = Toplevel()
user_page = Toplevel()
stock_page = Toplevel()
receipt_page = Toplevel()
request_page = Toplevel()
order_page = Toplevel()
exit_page = Toplevel()

class App:
    def __init__(self,event=None):
        self.btnState = False
        self.permission=False
        self.style=ttk.Style()
        self.lst=[]
        self.search_list=[]

        self.main()
        self.add_product_page()
        self.data_to_list_kala()
        self.warehouse_stock_page()
        self.data_to_list_stock()
        self.add_user_page()
        self.data_to_list_user()
        self.warehouse_receipt_page()
        self.warehouse_login_page()
        self.warehouse_register_page()
        self.request_product_page()
        self.data_to_list_request()
        self.order_kala_page()
        self.data_to_list_order()
        self.exit_kala_page()
        self.data_to_list_exit()

    def main(self):
        main_page.geometry('1400x800+250+100')
        main_page.configure(bg='white')
        main_page.title('menu')
        main_page.state('withdraw')
        
        #image
        self.addUserImg=PhotoImage(file='image/adduserImg.png')
        self.addWareImg=PhotoImage(file='image/addWareImg.png')
        self.WrStockImg=PhotoImage(file='image/WrStockImg.png')
        self.ReceiptImg=PhotoImage(file='image/ReceiptImg.png')
        self.requestImg=PhotoImage(file='image/requestImg.png')
        self.issuanceImg=PhotoImage(file='image/issuanceImg.png')
        self.exitImg=PhotoImage(file='image/exitImg.png')
        self.closeBtnImg=PhotoImage(file='image/closeImg.png')
        self.openBtnImg=PhotoImage(file='image/openNavImg.png')

        self.b_openNav=Button(main_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch,cursor='hand2')
        self.navFrm=Frame(main_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm=LabelFrame(self.navFrm,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav=Button(self.closeFrm,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch)
        self.b_addUser=Button(self.navFrm,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.open_addUser_page)
        self.b_addWare=Button(self.navFrm,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.open_addKala_page)
        self.b_WrStock=Button(self.navFrm,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.open_stock_page)
        self.b_Receipt=Button(self.navFrm,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.open_receipt_page)
        self.b_request=Button(self.navFrm,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.open_request_page)
        self.b_issuance=Button(self.navFrm,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit=Button(self.navFrm,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.b_openNav.place(x=1340,y=20)
        self.navFrm.place(x=1400,y=0)
        self.closeFrm.place(x=0,y=0)
        self.b_closeNav.place(x=15,y=15)
        self.b_addWare.place(x=0,y=50)
        self.b_addUser.place(x=0,y=115)
        self.b_WrStock.place(x=0,y=180)
        self.b_Receipt.place(x=0,y=245)
        self.b_request.place(x=0,y=310)
        self.b_issuance.place(x=0,y=375)
        self.b_exit.place(x=0,y=440)

    def switch(self):
        if self.btnState is True:
            for x in range(1180,1400):
                self.navFrm.place(x=+x, y=0)
                self.navFrm.update()
            self.btnState = False
        else:
            Px=1400
            for x in range(55):
                x=4
                Px=Px-x
                self.navFrm.place(x=Px, y=0)
                self.navFrm.update()
            self.btnState = True

    def open_addKala_page(self):
        product_page .state('normal')
        main_page.state('withdraw')
        register_page.state('withdraw')
        loginn_page.state('withdraw')
        user_page.state('withdraw')
        stock_page.state('withdraw')
        request_page.state('withdraw')
        receipt_page.state('withdraw')
        self.btnState = False

    def open_addUser_page(self):
        user_page.state('normal')
        product_page .state('withdraw')
        main_page.state('withdraw')
        register_page.state('withdraw')
        loginn_page.state('withdraw')
        stock_page.state('withdraw')
        request_page.state('withdraw')
        receipt_page.state('withdraw')
        self.btnState = False
    
    def open_stock_page(self):
        stock_page.state('normal')
        user_page.state('withdraw')
        product_page .state('withdraw')
        main_page.state('withdraw')
        register_page.state('withdraw')
        loginn_page.state('withdraw')
        request_page.state('withdraw')
        receipt_page.state('withdraw')
        self.btnState = False
    
    def open_receipt_page(self):
        receipt_page.state('normal')
        stock_page.state('withdraw')
        user_page.state('withdraw')
        product_page .state('withdraw')
        main_page.state('withdraw')
        register_page.state('withdraw')
        request_page.state('withdraw')
        loginn_page.state('withdraw')
        self.btnState = False

    def open_request_page(self):
        request_page.state('normal')
        receipt_page.state('withdraw')
        stock_page.state('withdraw')
        user_page.state('withdraw')
        product_page .state('withdraw')
        main_page.state('withdraw')
        register_page.state('withdraw')
        loginn_page.state('withdraw')
        self.btnState = False

#_____________________________________________________________________________________________________________________
#_________________________________________________login page__________________________________________________________
    def warehouse_login_page(self):
        loginn_page.geometry('400x510+750+300')
        loginn_page.config(bg='white')
        loginn_page.state('withdraw')

        #image
        self.logFrmImg = PhotoImage(file='image/loginFrm.png')
        self.logoImg = PhotoImage(file='image/logoImg.png')
        self.logBtnImg = PhotoImage(file='image/loginBtn.png')
        self.eyeImg = PhotoImage(file='image/openEye.png')

        self.logoImgLog = Label(loginn_page,image=self.logoImg,bg='white')
        self.l_userNameLog = Label(loginn_page,text=' : نام کاربری',font=('Lalezar',17),bg='white')
        self.e_userNameLog = Entry(loginn_page,font=('arial',18),justify=RIGHT,bd=2,relief='solid')
        self.l_passwordLog = Label(loginn_page,text=' : رمز عبور',font=('Lalezar',17),bg='white')
        self.e_passwordLog = Entry(loginn_page,font=('arial',18),justify=RIGHT,bd=2,relief='solid',show='*')
        self.showBtn = Button(loginn_page,image=self.eyeImg,bd=0,activebackground='white')
        self.b_enterBtn =Button(loginn_page,image=self.logBtnImg ,activebackground='white',bd=0)

        self.logoImgLog.place(x=135,y=10)
        self.l_userNameLog.place(x=250,y=175)
        self.e_userNameLog.place(x=80,y=215)
        self.l_passwordLog.place(x=270,y=275)
        self.e_passwordLog.place(x=80,y=316)
        self.showBtn.place(x=20,y=310)
        self.b_enterBtn.place(x=120,y=400)

        self.e_userNameLog.focus()
        self.e_userNameLog.bind('<Return>',lambda event : self.e_passwordLog.focus())
        self.e_passwordLog.bind('<Return>',lambda event : self.b_enterBtn.focus())
        self.showBtn.bind('<Button-1>',self.funcShow)
        

    def funcShow(self,event=None):
        if self.e_passwordLog['show']=='*':
            self.e_passwordLog['show']=''
            self.eyeImg['file']='image/closeEye.png'
        else:
            self.e_passwordLog['show']='*'
            self.eyeImg['file']='image/openEye.png'
#_____________________________________________________________________________________________________________________
#_________________________________________________ register page _____________________________________________________

    def warehouse_register_page(self):
        register_page.state('withdraw')
        register_page.geometry('1000x600+450+200')

        # Images
        self.signin_mainImg = PhotoImage(file='image/signInMainImg.png')
        self.logoImg_signIn = PhotoImage(file='image/logoImg.png')
        self.signInImg_filds = PhotoImage(file='image/signIn_filds.png')
        self.signInBtn = PhotoImage(file='image/registerBtn.png')

        self.signinImgFrm  = LabelFrame(register_page,bd=0)
        self.img_signin = Label(self.signinImgFrm,image=self.signin_mainImg)
        self.signinFrm  = Label(register_page,bd=0 ,image=self.signInImg_filds)
        self.signIn_logo  = Label(self.signinFrm,bd=0 ,image=self.logoImg_signIn,bg='white')
        self.e_Name     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.e_Last     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.e_user_name     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.e_password     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.b_signin_btn     = Button (self.signinFrm,image=self.signInBtn,bd=0)
        self.l_description = Label(self.signinFrm,text=' ! لطفا برای ورود به برنامه ابتدا ثبت نام کنید *   ', bg='white',font=('Lalezar',14),fg='#5D5555')

        self.signinImgFrm.grid  (row=1,column=1)
        self.img_signin.grid (row=1,column=1)
        self.signinFrm.grid  (row=1,column=2)
        self.signIn_logo.place(x=175,y=10)
        self.e_Name.place(x=100,y=175)
        self.e_Last.place(x=100,y=264)
        self.e_user_name.place(x=100,y=353)
        self.e_password.place(x=100,y=442)
        self.b_signin_btn.place(x=150,y=495)
        self.l_description.place(x=80,y=560)

        #bind
        self.e_Name.focus()
        self.e_Name.bind     ('<Return>',lambda event : self.e_Last.focus())
        self.e_Last.bind     ('<Return>',lambda event : self.e_user_name.focus())
        self.e_user_name.bind ('<Return>',lambda event : self.e_password.focus())
        self.e_password.bind    ('<Return>',lambda event : self.b_signin_btn.focus())
        self.b_signin_btn.bind    ('<Enter>',lambda event : self.funcBtnHover(self.signInBtn,'image/registerBtnH.png'))
        self.b_signin_btn.bind    ('<Leave>',lambda event : self.funcBtnHover(self.signInBtn,'image/registerBtn.png'))

    def funcBtnHover(self,img,url):
        img['file'] = url

    def f_register(self):
        pass

#______________________________________________________________________________________________________________________
#_________________________________________________ add product page ____________________________________________________

    def add_product_page(self):
        self.fildsBgImg = PhotoImage(file='image/fildsBg.png')
        self.kalaImg_kala = PhotoImage(file='image/imgSelectorBg.png')
        self.listKalaBgImg = PhotoImage(file='image/listSkalaBg.png')
        self.searchBtnImg_kala   = PhotoImage(file='image/searchBtnImg.png')
        self.h_sabtKalaImg = PhotoImage(file='image/headerSabtKala.png')
        self.addKalaBtnImg = PhotoImage(file='image/addKalaBtn.png')
        self.deleteBtnImg_kala = PhotoImage(file='image/deleteBtnImg.png')
        self.editBtnImg_kala = PhotoImage(file='image/editBtnImg.png')
        self.sabtTaghirKalaBtn = PhotoImage(file='image/sabtEdit.png')

        product_page.geometry  ('1400x800+250+100')
        product_page.state ('withdraw')
        product_page.configure (bg='#F3F3F3')

        #-------menu------

        self.h_sabtKala_kala = Label(product_page,image=self.h_sabtKalaImg)
        self.l_productId_kala = Label(product_page,text=' : کد کالا',font=('Lalezar',17))
        self.e_productId_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_productName_kala = Label(product_page,text=' : نام کالا',font=('Lalezar',17))
        self.e_productName_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_productType_kala = Label(product_page,text=' : نوع کالا',font=('Lalezar',17))
        self.c_productType_kala = ttk.Combobox(product_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                            justify = 'right',values=["مواد خام", "کالای خریداری شده",
                                            "کالای توید شده اولیه", "کالای تولید شده برای فروش"])
        self.l_groupType_kala = Label(product_page,text=' : گروه کالا',font=('Lalezar',17))
        self.c_groupType_kala = ttk.Combobox(product_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["فلزات", "مواد غذایی"])
        self.c_productType_kala.set("یک گزینه را انتخاب کنید")
        self.c_groupType_kala.set("یک گزینه را انتخاب کنید")
        self.l_description_kala = Label(product_page,text=' : توضیحات',font=('Lalezar',17))
        self.e_description_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=28,relief='solid')
        self.l_purchase_kala = Label(product_page,text=' : نقطه خرید',font=('Lalezar',17))
        self.e_purchase_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_imgSelector_kala = Label(product_page,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg_kala = Label(product_page,bg='#F3F3F3',image=self.kalaImg_kala,cursor='hand2',width=150,height=150)
        self.e_search_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_search_kala = Button(product_page,bg='#F3F3F3',image=self.searchBtnImg_kala,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.search_id_kalaPage)
        self.b_addKala_kala = Button(product_page,bg='#F3F3F3',image=self.addKalaBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.funcAddKala)
        self.listKalaBg_kala = Label(product_page,bg='white',image=self.listKalaBgImg)
        self.b_delete_kala = Button(product_page,image=self.deleteBtnImg_kala,bd=0,activebackground='white',cursor='hand2')
        self.b_edit_kala = Button(product_page,image=self.editBtnImg_kala,bd=0,activebackground='white',cursor='hand2')
        self.b_sabtTaghirat_kala = Button(product_page,image=self.sabtTaghirKalaBtn,bd=0,activebackground='white')

        #list
        self.listKala= ttk.Treeview(product_page,show='headings',height=8)

        self.listKala['columns']=('Purchase','Category','Type','Name','id','row')
        #columns
        self.listKala.column('Purchase',width=220,anchor=E)
        self.listKala.column('Category',width=220,anchor=E)
        self.listKala.column('Type',width=220,anchor=E)
        self.listKala.column('Name',width=220,anchor=E)
        self.listKala.column('id',width=200,anchor=E)
        self.listKala.column('row',width=150,anchor=E)
        #heading
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
        
        self.b_openNav_product=Button(product_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_product_nav,cursor='hand2')
        self.navFrm_product=Frame(product_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_product=LabelFrame(self.navFrm_product,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_product=Button(self.closeFrm_product,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_product_nav)
        self.b_addUser_product=Label(self.navFrm_product,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2')
        self.b_addWare_product=Label(self.navFrm_product,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2')
        self.b_WrStock_product=Label(self.navFrm_product,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2')
        self.b_Receipt_product=Label(self.navFrm_product,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2')
        self.b_request_product=Label(self.navFrm_product,image=self.requestImg,bg='#777777',bd=0,cursor='hand2')
        self.b_issuance_product=Label(self.navFrm_product,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_product=Label(self.navFrm_product,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.b_openNav_product.place (x=1340,y=20)
        self.navFrm_product.place (x=1400,y=0)
        self.closeFrm_product.place (x=0,y=0)
        self.b_closeNav_product.place (x=15,y=15)
        self.b_addUser_product.place (x=0,y=50)
        self.b_WrStock_product.place (x=0,y=115)
        self.b_Receipt_product.place (x=0,y=180)
        self.b_request_product.place (x=0,y=245)
        self.b_issuance_product.place (x=0,y=310)
        self.b_exit_product.place (x=0,y=375)
        self.h_sabtKala_kala.place (x=580 , y=0)
        self.l_productId_kala.place (x=1245 , y=100)
        self.e_productId_kala.place (x=985 , y=105)
        self.l_productName_kala.place (x=840 , y=100)
        self.e_productName_kala.place (x=585 , y=100)
        self.l_productType_kala.place (x=1240 , y=178)
        self.c_productType_kala.place (x=985 , y=178)
        self.l_groupType_kala.place (x=1235 , y=250)
        self.c_groupType_kala.place (x=985 , y=250)
        self.l_description_kala.place (x=820 , y=250)
        self.e_description_kala.place (x=475 , y=250)
        self.l_purchase_kala.place (x=820 , y=180)
        self.e_purchase_kala.place (x=585 , y=180)
        self.l_imgSelector_kala.place (x=210 , y=260)
        self.imgSelectorBg_kala.place (x=190 , y=100)
        self.e_search_kala.place (x=245 , y=375)
        self.b_search_kala.place  (x=85 , y=370)
        self.b_addKala_kala.place (x=1120 , y=340)
        self.listKala.place (x=85 , y=420)
        self.b_sabtTaghirat_kala.place (x=-100,y=-100)

        #_____ bind _____
        self.e_productId_kala.focus()
        self.e_productId_kala.bind('<Return>',lambda event : self.e_productName_kala.focus())
        self.e_productName_kala.bind('<Return>',lambda event : self.e_purchase_kala.focus())
        self.e_purchase_kala.bind('<Return>',lambda event : self.e_description_kala.focus())
        self.e_description_kala.bind('<Return>',lambda event : self.b_addKala_kala.focus())
        self.e_search_kala.bind('<Return>',lambda event : self.b_search_kala.focus())
        self.b_search_kala.bind('<Return>', self.search_id_kalaPage)
        self.b_addKala_kala.bind('<Return>', self.funcAddKala)
        self.imgSelectorBg_kala.bind('<Button-1>', self.funcAddImg_kala)
        self.listKala.bind('<ButtonRelease-1>', self.select_record_list_kala)
        self.b_delete_kala.bind('<Button-1>', self.delete_record_kala)
        self.b_edit_kala.bind('<ButtonRelease-1>', self.edit_record_kala_values)
        self.b_sabtTaghirat_kala.bind('<Button-1>', self.edit_kala)

        #_______ hover button ________
        self.e_search_kala.insert(0,'جستجو کد کالا  ')
        self.e_search_kala.bind('<Button-1>',lambda event :self.e_search_kala.delete(0,END))
        self.b_search_kala.bind('<Enter>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImgH.png'))
        self.b_search_kala.bind('<Leave>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImg.png'))
        self.b_delete_kala.bind('<Enter>',lambda event : self.funcBtnHover(self.deleteBtnImg,'image/deleteBtnImgH.png'))
        self.b_delete_kala.bind('<Leave>',lambda event : self.funcBtnHover(self.deleteBtnImg,'image/deleteBtnImg.png'))
        self.b_edit_kala.bind('<Enter>',lambda event : self.funcBtnHover(self.editBtnImg,'image/editBtnImgH.png'))
        self.b_edit_kala.bind('<Leave>',lambda event : self.funcBtnHover(self.editBtnImg,'image/editBtnImg.png'))

    def switch_product_nav(self):
        if self.btnState is True:
            self.navFrm_product.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_product.place(x=1180, y=0)
            self.btnState = True

    def data_to_list_kala(self):
        self.count=0        
        self.lst=[]
        for item in self.listKala.get_children():
            self.listUser.delete(item)
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kala'")
        
        self.result = self.cur.fetchone()
        if self.result != None:
            
            row=self.cur.execute('SELECT * FROM kala')
            for i in row :
                self.lst.append(i)
            
            for i in self.lst:
                self.listKala.insert(parent='',index='end',text='',
                                    values=(i[4],i[3],i[2],i[1],i[0],str(self.count+1)))
                self.count += 1

    def funcAddImg_kala(self,event=None):
        self.img_name = filedialog.askopenfilename()
        self.kalaImg_kala['file']= self.img_name
    
    def funcAddKala(self , event=None):
        self.productId=self.e_productId_kala.get()
        self.productName=self.e_productName_kala.get()
        self.productType=self.c_productType_kala.get()
        self.groupType=self.c_groupType_kala.get()
        self.purchase=self.e_purchase_kala.get()
        self.description=self.e_description_kala.get()
        self.photo = self.covert_to_binary_data(self.img_name)

        self.e_productId_kala.delete(0,END)
        self.e_productName_kala.delete(0,END)
        self.c_productType_kala.set("یک گزینه را انتخاب کنید")
        self.c_groupType_kala.set("یک گزینه را انتخاب کنید")
        self.e_purchase_kala.delete(0,END)
        self.e_description_kala.delete(0,END)
        self.kalaImg_kala['file']='image/imgSelectorBg.png'
        self.e_productId_kala.focus()

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
    
    def search_id_kalaPage(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idKala=self.e_search_kala.get()
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
            self.data_to_list_kala()

    def select_record_list_kala(self,event=None):
        self.selected = self.listKala.focus()
        self.values = self.listKala.item(self.selected , "values")
        self.row_id =self.listKala.identify_row(event.y)
        start = self.listKala.bbox(self.row_id, column=None)
        self.y1=start[1]+400
        self.y2=start[1]+440
        self.b_delete_kala.place(x=40,y=self.y1)
        self.b_edit_kala.place(x=40,y=self.y2)

    def delete_record_kala(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.code=self.values[4]
        self.cur.execute("DELETE FROM kala WHERE id='{}'" .format(self.code))
        self.con.commit()
        for item in self.listKala.get_children():
            self.listKala.delete(item)
        self.lst=[]
        self.data_to_list_kala()
        self.b_delete_kala.place(x=-50,y=-50)
        self.b_edit_kala.place(x=-50,y=-50)

    def sql_search_kala(self,id1):
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT COUNT(*) FROM kala")
        self.rowNum = self.cur.fetchone()[0]
        row = self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(id1))
        print(row)
        return list(row)
    
    def edit_record_kala_values(self ,event=None):
        self.e_productId_kala.delete(0,END)
        self.e_productName_kala.delete(0,END)
        self.c_groupType_kala.set("یک گزینه را انتخاب کنید")
        self.c_productType_kala.set("یک گزینه را انتخاب کنید")
        self.e_purchase_kala.delete(0,END)
        self.e_description_kala.delete(0,END)
        self.values = self.listKala.item(self.selected , "values")
        self.row_num=self.values[5]
        self.valuelst = self.sql_search_kala(self.values[4])
        self.e_productId_kala.insert(0,self.valuelst[0][0])
        self.e_productName_kala.insert(0,self.valuelst[0][1])
        self.c_productType_kala.set(self.valuelst[0][2])
        self.c_groupType_kala.set(self.valuelst[0][3])
        self.e_purchase_kala.insert(0,self.valuelst[0][4])
        self.e_description_kala.insert(0,self.valuelst[0][5])
        self.b_sabtTaghirat_kala.place(x=910,y=340)

    def edit_kala(self,event = None):
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.code = self.e_productId_kala.get()
        self.name = self.e_productName_kala.get()
        self.point = self.e_purchase_kala.get()
        self.desc = self.e_description_kala.get()
        self.type = self.c_productType_kala.get()
        self.group = self.c_groupType_kala.get()
        self.listKala.item(self.selected ,values = (self.point,self.group,self.type,self.name,self.code,self.row_num))
        print(self.values)
        self.cur.execute(''' UPDATE kala SET id = "{}" , name = "{}", type = "{}",category = "{}",
        purchase = "{}",description = "{}" WHERE id="{}" '''.format(self.code,self.name,self.type,self.group,self.point,self.desc,self.values[4]))
        self.con.commit()
        self.b_sabtTaghirat_kala.place(x=-100,y=-100)
        self.b_delete_kala.place(x=-50,y=-50)
        self.b_edit_kala.place(x=-50,y=-50)
        self.valuelst=[]
#_________________________________________________________________________________________________________________________
#____________________________________________________ add user page ______________________________________________________
    def add_user_page(self):
        self.hSabtUserImg = PhotoImage(file='image/headerSabtKarmandImg.png')
        self.UserImg = PhotoImage(file='image/imgSelectorBg.png')
        self.searchBtnImg_user = PhotoImage(file='image/searchBtnImg.png')
        self.addPesonnelImg = PhotoImage(file='image/addPesonnelBtnImg.png')
        self.deleteBtnImg_user = PhotoImage(file='image/deleteBtnImg.png')
        self.editBtnImg_user = PhotoImage(file='image/editBtnImg.png')
        self.sabtTaghirBtn_user = PhotoImage(file='image/sabtEdit.png')

        user_page.geometry ('1400x800+250+100')
        user_page.configure (bg='#F3F3F3')
        user_page.state ('withdraw')
    
        self.l_headerUser=Label(user_page,image=self.hSabtUserImg)
        self.l_nameUser=Label(user_page,text=' : نام',font=('Lalezar',17))
        self.e_nameUser=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_lastUser=Label(user_page,text=' : نام خانوادگی',font=('Lalezar',17))
        self.e_lastUser=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_nationalCode=Label(user_page,text=' : کد ملی',font=('Lalezar',17))
        self.e_nationalCode=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_gender=Label(user_page,text=' : جنسیت',font=('Lalezar',17))
        self.c_gender=ttk.Combobox(user_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["زن", "مرد"])
        self.c_gender.set("یک گزینه را انتخاب کنید")
        self.l_phoneNum=Label(user_page,text=' : شماره تماس',font=('Lalezar',17))
        self.e_phoneNum=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_accountType=Label(user_page,text=' : نوع کاربری',font=('Lalezar',17))
        self.c_accountType=ttk.Combobox(user_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["فروشنده","کارمند","ادمین", "مدیر"])
        self.c_accountType.set("یک گزینه را انتخاب کنید")
        self.l_personnelId=Label(user_page,text=' : کد کارمند',font=('Lalezar',17))
        self.e_personnelId=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_UserPass=Label(user_page,text=' : رمزعبور',font=('Lalezar',17))
        self.e_UserPass=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_imgSelector = Label(user_page,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg = Label(user_page,bg='#F3F3F3',image=self.UserImg,cursor='hand2',width=150,height=150)
        self.b_addPesonnel= Button(user_page,bg='#F3F3F3',image=self.addPesonnelImg,activebackground='#F3F3F3',bd=0,cursor='hand2')
        self.e_searchUser   = Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUser= Button(user_page,bg='#F3F3F3',image=self.searchBtnImg_user,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.search_id_user)
        self.b_delete_user=Button(user_page,image=self.deleteBtnImg_user,bd=0,activebackground='white',cursor='hand2')
        self.b_edit_user=Button(user_page,image=self.editBtnImg_user,bd=0,activebackground='white',cursor='hand2')
        self.b_sabtTaghirat_user=Button(user_page,image=self.sabtTaghirBtn_user,bd=0,activebackground='white')
        
        #list
        self.listUser= ttk.Treeview(user_page,show='headings',height=8)

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

        self.b_openNav_user=Button(user_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_user_nav,cursor='hand2')
        self.navFrm_user=Frame(user_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_user=LabelFrame(self.navFrm_user,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_user=Button(self.closeFrm_user,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_user_nav)
        self.b_addUser_user=Label(self.navFrm_user,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2')
        self.b_addWare_user=Label(self.navFrm_user,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2')
        self.b_WrStock_user=Label(self.navFrm_user,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2')
        self.b_Receipt_user=Label(self.navFrm_user,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2')
        self.b_request_user=Label(self.navFrm_user,image=self.requestImg,bg='#777777',bd=0,cursor='hand2')
        self.b_issuance_user=Label(self.navFrm_user,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_user=Label(self.navFrm_user,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.b_openNav_user.place(x=1340,y=20)
        self.navFrm_user.place(x=1400,y=0)
        self.closeFrm_user.place(x=0,y=0)
        self.b_closeNav_user.place(x=15,y=15)
        self.b_addUser_user.place(x=0,y=50)
        self.b_WrStock_user.place(x=0,y=115)
        self.b_Receipt_user.place(x=0,y=180)
        self.b_request_user.place(x=0,y=245)
        self.b_issuance_user.place(x=0,y=310)
        self.b_exit_user.place(x=0,y=375)

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
        self.listUser.bind('<ButtonRelease-1>', self.select_record_user)
        self.b_delete_user.bind('<Button-1>', self.delete_record_user)
        self.b_edit_user.bind('<ButtonRelease-1>', self.edit_record_values_user)
        self.b_sabtTaghirat_user.bind('<Button-1>', self.edit_user)

    def switch_user_nav(self):
        if self.btnState is True:
            self.navFrm_user.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_user.place(x=1180, y=0)
            self.btnState = True

    def funcAddImg(self,event=None):
        self.img_name = filedialog.askopenfilename()
        self.UserImg['file']= self.img_name

    def funcBtnHover(self,img,url):
        img['file'] = url

    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
    
    def data_to_list_user(self):
        self.count=0
        self.lst=[]
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
                                    values=(i[6],i[5],i[3],i[2],i[1],i[0],str(self.count+1)))
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
        self.listUser.insert(parent='',index='end',text='',values=(self.accountType,self.phoneNum,self.gender,
                                                                    self.pesonnelLast,self.pesonnelName,self.personnelId,self.numlist+1))
    
    def search_id_user(self,event=None):
        print('okk')
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idUser=self.e_searchUser.get()
        if self.idUser !='':
            for i in self.listUser.get_children():
                self.listUser.delete(i)
            self.numlist=len(self.listUser.get_children())
            self.row=self.cur.execute('SELECT * FROM user WHERE id="{}"'.format(self.idUser))
            self.search_list=list(self.row)
            self.listUser.insert(parent='',index='end',iid=self.count,text='',
                                    values=(self.search_list[0][6],self.search_list[0][5],self.search_list[0][3],
                                            self.search_list[0][2],self.search_list[0][1],self.search_list[0][0],str(self.numlist+1)))
        else:
            self.lst=[]
            self.listUser.delete('0')
            self.data_to_list_user()
    
    def select_record_user(self,event=None):
        self.selected = self.listUser.focus()
        self.values = self.listUser.item(self.selected , "values")
        self.row_id =self.listUser.identify_row(event.y)
        start = self.listUser.bbox(self.row_id, column=None)
        self.y1=start[1]+400
        self.y2=start[1]+440
        self.b_delete_user.place(x=40,y=self.y1)
        self.b_edit_user.place(x=40,y=self.y2)

    def delete_record_user(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.code=self.values[5]
        self.cur.execute("DELETE FROM user WHERE id='{}'" .format(self.code))
        self.con.commit()
        for item in self.listUser.get_children():
            self.listUser.delete(item)
        self.lst=[]
        self.data_to_list_user()
        self.b_delete_user.place(x=-50,y=-50)
        self.b_edit_user.place(x=-50,y=-50)

    def sql_search_user(self,id1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        self.cur.execute("SELECT COUNT(*) FROM user")
        self.rowNum = self.cur.fetchone()[0]
        row = cur.execute('SELECT * FROM user WHERE id="{}"'.format(id1))
        return list(row)
    
    def edit_record_values_user(self ,event=None):
        self.e_nameUser.delete(0,END)
        self.e_lastUser.delete(0,END)
        self.e_nationalCode.delete(0,END)
        self.c_gender.set("یک گزینه را انتخاب کنید")
        self.e_phoneNum.delete(0,END)
        self.c_accountType.set("یک گزینه را انتخاب کنید")
        self.e_personnelId.delete(0,END)
        self.e_UserPass.delete(0,END)
        self.values = self.listUser.item(self.selected , "values")
        self.row_num=self.values[6]
        self.valuelst = self.sql_search_user(self.values[5])
        self.e_personnelId.insert(0,self.valuelst[0][0])
        self.e_nameUser.insert(0,self.valuelst[0][1])
        self.e_lastUser.insert(0,self.valuelst[0][2])
        self.e_nationalCode.insert(0,self.valuelst[0][3])
        self.c_gender.insert(0,self.valuelst[0][4])
        self.e_phoneNum.insert(0,self.valuelst[0][5])
        self.c_accountType.insert(0,self.valuelst[0][6])
        self.e_UserPass.insert(0,self.valuelst[0][7])
        self.b_sabtTaghirat_user.place(x=910,y=340)

    def edit_user(self,event = None):
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.pesonnelName=self.e_nameUser.get()
        self.pesonnelLast=self.e_lastUser.get()
        self.nationalCode=self.e_nationalCode.get()
        self.gender=self.c_gender.get()
        self.phoneNum=self.e_phoneNum.get()
        self.accountType=self.c_accountType.get()
        self.personnelId=self.e_personnelId.get()
        self.personnelPass=self.e_UserPass.get()
        self.listUser.item(self.selected ,values = (self.accountType,self.phoneNum,self.nationalCode,self.pesonnelLast,self.pesonnelName,self.personnelId,self.row_num))
        self.cur.execute(''' UPDATE user SET id = "{}" , name = "{}", last_name = "{}",national_code = "{}",
        gender = "{}",phone_number = "{}",account_type ="{}",personnel_pass ="{}" WHERE id="{}" '''.format(self.personnelId,
                                                    self.pesonnelName,self.pesonnelLast,self.nationalCode,self.gender,
                                                    self.phoneNum,self.accountType,self.personnelPass,self.values[5]))
        self.con.commit()
        self.b_sabtTaghirat_user.place(x=-100,y=-100)
        self.b_delete_user.place(x=-50,y=-50)
        self.b_edit_user.place(x=-50,y=-50)


    #____________________________________________________________________________________________________________________
    #________________________________________________ warehouse Stock page ______________________________________________
    def warehouse_stock_page(self):

        self.h_stockImg = PhotoImage(file='image/headerStock.png')
        self.searchBtnImg_stock   = PhotoImage(file='image/searchBtnImg.png')
        self.filterBtnImg = PhotoImage(file='image/filterBtnImg.png')
        self.deleteBtnImg_stock = PhotoImage(file='image/deleteBtnImg.png')

        stock_page.geometry ('1400x800+250+100')
        stock_page.configure (bg='#F3F3F3')
        stock_page.state ('withdraw')

        self.l_headerStock=Label(stock_page,image=self.h_stockImg)
        self.b_filterStock=Button(stock_page,image=self.filterBtnImg,bd=0,activebackground='white',command=self.filter_stock)
        self.c_filterStock = ttk.Combobox(stock_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["همه ی کالا ها","فلزات", "مواد غذایی"])
        self.c_filterStock.set("یک گزینه را انتخاب کنید")
        self.l_filterStock=Label(stock_page,text=' : گروه کالا',font=('Lalezar',17))
        self.e_searchStock = Entry(stock_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchStock= Button(stock_page,image=self.searchBtnImg_stock,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.search_id_stock)
        self.b_delete_stock=Button(stock_page,image=self.deleteBtnImg_stock,bd=0,activebackground='#F3F3F3',cursor='hand2')

        #list
        self.listStock= ttk.Treeview(stock_page,show='headings',height=15)

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
        self.listStock.bind('<ButtonRelease-1>', self.select_record_stock)
        self.b_delete_stock.bind('<Button-1>', self.delete_record_stock)


        self.l_headerStock.place(x=580,y=0)
        self.b_filterStock.place(x=860,y=130)
        self.c_filterStock.place(x=1020,y=135)
        self.l_filterStock.place(x=1230,y=135)
        self.e_searchStock.place(x=245,y=135)
        self.b_searchStock.place(x=85,y=130)
        self.listStock.place(x=85,y=185)

    def data_to_list_stock(self):
        self.count=0
        self.lst=[]
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
    
    def select_record_stock(self,event=None):
        self.selected = self.listStock.focus()
        self.values = self.listStock.item(self.selected , "values")
        self.row_id =self.listStock.identify_row(event.y)
        start = self.listStock.bbox(self.row_id, column=None)
        self.y1=start[1]+185
        self.b_delete_stock.place(x=40,y=self.y1)

    def delete_record_stock(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.code=self.values[5]
        self.cur.execute("DELETE FROM kala WHERE id='{}'" .format(self.code))
        self.con.commit()
        for item in self.listStock.get_children():
            self.listStock.delete(item)
        self.lst=[]
        self.data_to_list_stock()
        self.b_delete_stock.place(x=-50,y=-50)
    
    def filter_stock(self):
        self.filterLst=self.c_filterStock.get()
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.count=0
        if self.filterLst =="همه ی کالا ها":
            for item in self.listStock.get_children():
                self.listStock.delete(item)
            self.lst=[]
            self.data_to_list_stock()
        elif self.filterLst !='یک گزینه را انتخاب کنید':
            for i in self.listStock.get_children():
                self.listStock.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE category="{}"'.format(self.filterLst))
            self.filter_list=list(self.row)
            for i in self.filter_list:
                self.listStock.insert(parent='',index='end',text='',
                                    values=(i[4],i[7],i[3],i[2],i[1],i[0],str(self.count+1)))
                self.count += 1
    
    def search_id_stock(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idKala=self.e_searchStock.get()
        self.count=0
        if self.idKala !='':
            for i in self.listStock.get_children():
                self.listStock.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala))
            self.search_list=list(self.row)
            self.listStock.insert(parent='',index='end',iid=self.count,text='',
                                    values=(self.search_list[0][4],self.search_list[0][7],self.search_list[0][3],
                                            self.search_list[0][2],self.search_list[0][1],self.search_list[0][0],str(self.count+1)))
        else:
            self.lst=[]
            self.listStock.delete('0')
            self.data_to_list_stock()

#________________________________________________________________________________________________________________________
#________________________________________________ warehouse receipt page_________________________________________________

    def warehouse_receipt_page(self):
        self.headerVorodKalaImg = PhotoImage(file='image/headerReciept.png')
        self.searchBtnImg = PhotoImage(file='image/searchBtnImg.png')
        self.kalaImg = PhotoImage(file='image/imgSelectorBg.png')
        self.addKalaNumImg = PhotoImage(file='image/addKalaNum.png')
        
        receipt_page.geometry ('1400x800+250+100')
        receipt_page.configure (bg='#F3F3F3')
        receipt_page.state ('withdraw')

        self.searchUserFrm = LabelFrame(receipt_page,bg='#DFDFDF',width=1410,height=170,bd=5,relief=SOLID)
        self.h_vorodKala_receipt = Label(self.searchUserFrm,image=self.headerVorodKalaImg)
        self.l_attention_receipt = Label(self.searchUserFrm,text='.توجه : لطفا ابتدا کد ملی متقاضی مورد نظر را وارد کنید',font=('Lalezar',17),bg='#DFDFDF')
        self.e_searchUser_receipt  = Entry(self.searchUserFrm,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUser_receipt = Button(self.searchUserFrm,bg='#DFDFDF',image=self.searchBtnImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.search_idUser_receipt)
        self.e_searchKala_receipt = Entry(receipt_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid',fg='#717171')
        self.e_searchKala_receipt.insert(0,'جستجوی کد کالا')
        self.b_searchKala_receipt = Button(receipt_page,bg='#DFDFDF',image=self.searchBtnImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.search_idKala)
        self.infoKalaFrm_receipt = LabelFrame(receipt_page,bg='#EAEAEA',width=1230,height=240,bd=5,relief=SOLID)
        self.l_nameUser_receipt = Label(receipt_page,text=' : نام',font=('Lalezar',17),bg='#EAEAEA')
        self.nameUserLbl_receipt = Label(receipt_page,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_nameKala_receipt = Label(receipt_page,text=' : نام کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.nameKalaLbl_receipt = Label(receipt_page,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_kalaType_receipt = Label(receipt_page,text=' : نوع کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.kalaTypeLbl_receipt =Label(receipt_page,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_lastUser_receipt = Label(receipt_page,text=' : نام خانوادگی',font=('Lalezar',17),bg='#EAEAEA')
        self.lastUserLbl_receipt = Label(receipt_page,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_kalaId_receipt = Label(receipt_page,text=' : کد کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.kalaIdLbl_receipt = Label(receipt_page,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_groupKala_receipt = Label(receipt_page,text=' : گروه کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.groupKalaLbl_receipt = Label(receipt_page,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_imgSelector_receipt = Label(receipt_page,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg_receipt = Label(receipt_page,bg='#F3F3F3',image=self.kalaImg,cursor='hand2',width=150,height=150)
        self.kalaNumFrm_receipt = LabelFrame(receipt_page,bg='#EAEAEA',width=540,height=70,bd=5,relief=SOLID) 
        self.kalaNum_receipt = Label(self.kalaNumFrm_receipt,text=' : تعداد کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.e_kalaNum_receipt = Entry(self.kalaNumFrm_receipt,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid',fg='#717171')
        self.b_addKalaNum_receipt = Button(self.kalaNumFrm_receipt,bg='#DFDFDF',image=self.addKalaNumImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.funcAddNum)
        #list
        self.listReceipt= ttk.Treeview(receipt_page,show='headings',height=5)
        self.listReceipt['columns']=('date','kalaNum','kalaId','groupKala','kalaType','kalaName','fullname','row')
        #columns
        self.listReceipt.column('date',width=150,anchor=E)
        self.listReceipt.column('kalaNum',width=90,anchor=E)
        self.listReceipt.column('groupKala',width=200,anchor=E)
        self.listReceipt.column('kalaType',width=200,anchor=E)
        self.listReceipt.column('kalaId',width=90,anchor=E)
        self.listReceipt.column('kalaName',width=200,anchor=E)
        self.listReceipt.column('fullname',width=200,anchor=E)
        self.listReceipt.column('row',width=100,anchor=E)
        #heading
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
        self.e_searchUser_receipt.focus()
        self.e_searchUser_receipt.bind('<Return>',lambda event:self.b_searchUser_receipt.focus())
        self.b_searchUser_receipt.bind('<Return>',self.search_idUser_receipt)
        self.e_searchKala_receipt.bind('<Button-1>',lambda event:self.e_searchKala_receipt.delete(0,END))
        self.e_searchKala_receipt.bind('<Return>',lambda event:self.b_searchKala_receipt.focus())
        self.b_searchKala_receipt.bind('<Return>',self.search_idKala)
        self.e_kalaNum_receipt.bind('<Return>',lambda event:self.b_addKalaNum_receipt.focus())
        self.b_addKalaNum_receipt.bind('<Return>',self.funcAddNum)


        self.h_vorodKala_receipt.place(x=610,y=0)
        self.searchUserFrm.place(x=-5,y=-10)
        self.l_attention_receipt.place(x=690,y=90)
        self.e_searchUser_receipt.place(x=475,y=90)
        self.b_searchUser_receipt.place(x=315,y=85)
        self.e_searchKala_receipt.place(x=1115,y=175)
        self.b_searchKala_receipt.place(x=955,y=170)
        self.infoKalaFrm_receipt.place(x=85,y=225)
        self.l_nameUser_receipt.place(x=1240,y=280)
        self.nameUserLbl_receipt.place(x=1025,y=280)
        self.l_nameKala_receipt.place(x=1210,y=360)
        self.nameKalaLbl_receipt.place(x=1025,y=360)
        self.l_lastUser_receipt.place(x=860,y=280)
        self.lastUserLbl_receipt.place(x=675,y=280)
        self.l_kalaId_receipt.place(x=900,y=360)
        self.kalaIdLbl_receipt.place(x=675,y=360)
        self.l_kalaType_receipt.place(x=515,y=280)
        self.kalaTypeLbl_receipt.place(x=330,y=280)
        self.l_groupKala_receipt.place(x=520,y=360)
        self.groupKalaLbl_receipt.place(x=330,y=360)
        self.l_imgSelector_receipt.place(x=135,y=390)
        self.imgSelectorBg_receipt.place(x=110,y=240)
        self.kalaNumFrm_receipt.place(x=775,y=460)
        self.kalaNum_receipt.place(x=400,y=10)
        self.e_kalaNum_receipt.place(x=180,y=10)
        self.b_addKalaNum_receipt.place(x=15,y=5)
        self.listReceipt.place(x=85,y=545)


    def search_idUser_receipt(self,event=None):
        try:
            self.con=sql.connect('mydb.db')
            self.cur=self.con.cursor()
            self.nationalId=self.e_searchUser_receipt.get()
            self.count=0
            if self.nationalId != '':
                self.row=self.cur.execute('SELECT * FROM user WHERE national_code="{}"'.format(self.nationalId))
                self.userInfo=list(self.row)
                if self.userInfo[0][6]=='فروشنده':
                    self.permission=True
                    self.nameUserLbl_receipt['text']=self.userInfo[0][1]
                    self.lastUserLbl_receipt['text']=self.userInfo[0][2]
                    self.fullname=self.userInfo[0][1]+' '+self.userInfo[0][2]
                else:
                    messagebox.showinfo("information","کاربر با این کد ملی قادر به ثبت ورود کالا نیست")
        except :
            messagebox.showinfo("information","کاربری با این کد ملی وجود ندارد")


    def search_idKala(self,event=None):
        if self.permission==True:
            self.idKala=self.e_searchKala_receipt.get()
            if self.idKala !='':
                self.con=sql.connect('mydb.db')
                self.cur=self.con.cursor()
                self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala))
                self.kalaInfo=list(self.row)
                self.nameKalaLbl_receipt['text']=self.kalaInfo[0][1]
                self.kalaTypeLbl_receipt['text']=self.kalaInfo[0][2]
                self.kalaIdLbl_receipt['text']=self.kalaInfo[0][0]
                self.groupKalaLbl_receipt['text']=self.kalaInfo[0][3]

    def funcAddNum(self,event=None):
        self.entryNum=self.e_kalaNum_receipt.get()
        self.kalaNumber=int(self.entryNum)+int(self.kalaInfo[0][7])

        self.cur.execute(''' UPDATE kala SET stock = "{}" WHERE id="{}" '''.format(self.kalaNumber,self.idKala))
        self.con.commit()
        self.num_of_rows = len(self.listReceipt.get_children())
        self.listReceipt.insert(parent='',index='end',text='',
                                    values=('01/01',self.kalaNumber,self.kalaInfo[0][0],
                                            self.kalaInfo[0][3],self.kalaInfo[0][2],self.kalaInfo[0][1],self.fullname,self.num_of_rows+1))
        self.e_kalaNum_receipt.delete(0,END)
        self.e_searchKala_receipt.delete(0,END)
        self.e_searchUser_receipt.delete(0,END)
        self.kalaInfo=[]
        self.fullname=''
        self.nameKalaLbl_receipt['text']=''
        self.kalaTypeLbl_receipt['text']=''
        self.kalaIdLbl_receipt['text']=''
        self.groupKalaLbl_receipt['text']=''
        self.nameUserLbl_receipt['text']=''
        self.lastUserLbl_receipt['text']=''
        self.permission=False

    #____________________________________________________________________________________________________________________
    #__________________________________________________ request product _________________________________________________

    def request_product_page(self):
        request_page.geometry('1400x800+250+100')
        request_page.configure(bg='white')
        request_page.title('menu')
        request_page.state('withdraw')

        self.headerReguestImg = PhotoImage(file='image/headerRequestImg.png')
        self.requestBtnImg = PhotoImage(file='image/requestBtnImg.png')

        self.h_requestPage = Label(request_page,image=self.headerReguestImg)
        self.b_requestPage = Button(request_page,image=self.requestBtnImg,bd=0,activebackground='white',command=self.order_kala)
        #list
        self.listRequest= ttk.Treeview(request_page,show='headings',height=15)

        self.listRequest['columns']=('Purchase','number','Category','Type','Name','id','row')
        #columns
        self.listRequest.column('Purchase',width=150,anchor=E)
        self.listRequest.column('number',width=150,anchor=E)
        self.listRequest.column('Category',width=220,anchor=E)
        self.listRequest.column('Type',width=220,anchor=E)
        self.listRequest.column('Name',width=220,anchor=E)
        self.listRequest.column('id',width=150,anchor=E)
        self.listRequest.column('row',width=120,anchor=E)
        #heading
        self.listRequest.heading('Purchase',text=' : نقطه خرید',anchor=E)
        self.listRequest.heading('number',text=' : تعداد',anchor=E)
        self.listRequest.heading('Category',text=' : گروه کالا',anchor=E)
        self.listRequest.heading('Type',text=' : نوع کالا',anchor=E)
        self.listRequest.heading('Name',text=' : نام کالا',anchor=E)
        self.listRequest.heading('id',text=' : کد کالا',anchor=E)
        self.listRequest.heading('row',text=' : ردیف',anchor=E)
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
        
        #_________________bind_________________
        self.listRequest.bind('<ButtonRelease>',self.select_record_list_request)

        self.h_requestPage.place(x=580,y=0)
        self.listRequest.place(x=85,y=90)
        self.b_requestPage.place(x=600,y=720)

    def data_to_list_request(self):
        self.lst=[]
        self.fullname='محمد پناهی'
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kala'")
        self.result_request = self.cur.fetchone()
        if self.result_request != None:
            row=self.cur.execute('SELECT * FROM kala')
            for i in row:
                self.lst.append(i)
            for i in self.lst:
                if int(i[4]) > int(i[7]):
                    self.numlistRequest=len(self.listKala.get_children())
                    self.listRequest.insert(parent='',index='end',text='',
                                    values=(i[4],i[7],i[3],i[2],i[1],i[0],self.numlistRequest))
                    self.purchase_req=i[4]
                    self.kalaNum_req=i[7]
    def order_kala(self):
        self.permission=True
        receipt_page.state('normal')
        request_page.state('withdraw')
        self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.valuesReq[5]))
        self.e_searchKala_receipt.delete(0,END)
        self.e_searchKala_receipt.insert('0',(self.valuesReq[5]))
        self.search_idKala()
        self.e_kalaNum_receipt.insert('0',int(self.purchase_req)-int(self.kalaNum_req))
        self.con.commit()

    def select_record_list_request(self,event=None):
        self.selected = self.listRequest.focus()
        self.valuesReq = self.listRequest.item(self.selected , "values")
        
#__________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________ order page ______________________________________________________________________________
    def order_kala_page(self):
        order_page.geometry('1400x800+250+100')
        order_page.configure(bg='white')
        order_page.title('menu')
        order_page.state('normal')

        self.headerReguestImg = PhotoImage(file='image/headerRequestImg.png')
        self.sabtOrderBtnImg = PhotoImage(file='image/sabtOrder.png')
        self.searchBtnImg_order = PhotoImage(file='image/searchBtnImg.png')
        self.order_imgSelectorPic = PhotoImage(file='image/imgSelectorBg.png')
        self.order_baresiImg = PhotoImage(file='image/baresiBtnImg.png')
        self.tickImgBtn = PhotoImage(file='image/tickImgBtn.png')

        self.l_headerOrderPage = Label(order_page,image=self.headerReguestImg)
        self.attention_idUser = Label(order_page,text=' . لطفا کد کاربر موردنطر خود را وارد کنید',font=('Lalezar',17),bg='white')
        self.e_idUser_order = Entry(order_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUserBtnOrder = Button(order_page,image=self.order_baresiImg,bd=0,activebackground='white',command=self.search_idUser_order)
        self.e_idKala_order = Entry(order_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchBtnOrder = Button(order_page,image=self.searchBtnImg_order,bd=0,activebackground='white',command=self.search_idKala_order)
        self.userInfo_order_frm = LabelFrame(order_page,width=510,height=165,bg='#F2F2F2',bd=5,relief=SOLID)
        self.l_nameUser_order = Label(self.userInfo_order_frm,text=' : نام',font=('Lalezar',17),bg='#F2F2F2')
        self.nameUserLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_lastUser_order = Label(self.userInfo_order_frm,text=' : نام خانوادگی',font=('Lalezar',17),bg='#F2F2F2')
        self.lastUserLbl_order =Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_nationalCode_order = Label(self.userInfo_order_frm,text=' : کد ملی',font=('Lalezar',17),bg='#F2F2F2')
        self.nationalCodeLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_userId_order = Label(self.userInfo_order_frm,text=' : کد کاربری',font=('Lalezar',17),bg='#F2F2F2')
        self.userIdLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=8,fg='#4F4E4E')
        self.order_frm_num = LabelFrame(order_page,width=510,height=85,bg='#F2F2F2',bd=5,relief=SOLID)
        self.l_orderNum = Label(self.order_frm_num,text=' : تعداد',font=('Lalezar',17))
        self.e_orderNum = Entry(self.order_frm_num,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_sabtOrder = Button(self.order_frm_num,image=self.sabtOrderBtnImg,bd=0,activebackground='white',command=self.addOrder)
        self.kalaInfo_order_frm = LabelFrame(order_page,width=800,height=240,bg='#D0D0D0',bd=5,relief=SOLID)
        self.l_nameKala_order = Label(self.kalaInfo_order_frm,text=' : نام کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.nameKalaLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_kalaType_order = Label(self.kalaInfo_order_frm,text=' : نوع کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.kalaTypeLbl_order =Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_kalaId_order = Label(self.kalaInfo_order_frm,text=' : کد کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.kalaIdLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_groupKala_order = Label(self.kalaInfo_order_frm,text=' : گروه کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.groupKalaLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_kalaNum_order = Label(self.kalaInfo_order_frm,text=' : موجودی',font=('Lalezar',17),bg='#D0D0D0')
        self.kalaNumLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_purcase_order = Label(self.kalaInfo_order_frm,text=' : نقطه خرید',font=('Lalezar',17),bg='#D0D0D0')
        self.purcaseLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_imgSelector_order = Label(self.kalaInfo_order_frm,text='انتخاب تصویر',font=('Lalezar',17),bg='#D0D0D0')
        self.imgSelectorBg_order = Label(self.kalaInfo_order_frm,bg='#D0D0D0',image=self.order_imgSelectorPic,cursor='hand2',width=150,height=150)
        self.tickBtnOrder = Button(order_page,bg='#D0D0D0',image=self.tickImgBtn,bd=0,background='white',cursor='hand2')
        #list
        self.listOrder= ttk.Treeview(order_page,show='headings',height=8)

        self.listOrder['columns']=('date','stock','orderNum','orderId','userName','NameKala','id','row')
        #columns
        self.listOrder.column('date',width=140,anchor=CENTER)
        self.listOrder.column('stock',width=140,anchor=CENTER)
        self.listOrder.column('orderId',width=210,anchor=E)
        self.listOrder.column('orderNum',width=130,anchor=CENTER)
        self.listOrder.column('userName',width=230,anchor=E)
        self.listOrder.column('NameKala',width=185,anchor=E)
        self.listOrder.column('id',width=130,anchor=CENTER)
        self.listOrder.column('row',width=130,anchor=CENTER)
        #heading
        self.listOrder.heading('date',text=' : تاریخ',anchor=E)
        self.listOrder.heading('stock',text=' : موجودی',anchor=E)
        self.listOrder.heading('orderId',text=' : کد سفارش',anchor=E)
        self.listOrder.heading('orderNum',text=' : تعداد سفارش',anchor=E)
        self.listOrder.heading('userName',text=' : نام سفارش دهنده',anchor=E)
        self.listOrder.heading('NameKala',text=' : نام کالا',anchor=E)
        self.listOrder.heading('id',text=' : کد کالا',anchor=E)
        self.listOrder.heading('row',text=' : ردیف',anchor=E)
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading",font=('Lalezar', 16),
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
    
        self.l_headerOrderPage.place(x=580,y=0)
        self.attention_idUser.place(x=1040,y=90)
        self.e_idUser_order.place(x=835,y=90)
        self.b_searchUserBtnOrder.place(x=670,y=85)
        self.b_searchBtnOrder.place(x=50,y=85)
        self.e_idKala_order.place(x=215,y=90)
        self.order_frm_num.place(x=845,y=305)
        self.l_orderNum.place(x=420,y=15)
        self.e_orderNum.place(x=210,y=15)
        self.b_sabtOrder.place(x=20,y=10)
        self.userInfo_order_frm.place(x=845,y=150)
        self.l_nameUser_order.place(x=450,y=20)
        self.nameUserLbl_order.place(x=260,y=20)
        self.l_lastUser_order.place(x=200,y=20)
        self.lastUserLbl_order.place(x=10,y=20)
        self.l_userId_order.place(x=405,y=80)
        self.userIdLbl_order.place(x=260,y=80)
        self.l_nationalCode_order.place(x=190,y=80)
        self.nationalCodeLbl_order.place(x=5,y=80)
        self.kalaInfo_order_frm.place(x=50,y=150)
        self.l_kalaId_order.place(x=690,y=10)
        self.kalaIdLbl_order.place(x=510,y=10)
        self.l_nameKala_order.place(x=400,y=10)
        self.nameKalaLbl_order.place(x=220,y=10)
        self.l_kalaType_order.place(x=690,y=90)
        self.kalaTypeLbl_order.place(x=510,y=90)
        self.l_groupKala_order.place(x=400,y=90)
        self.groupKalaLbl_order.place(x=220,y=90)
        self.l_kalaNum_order.place(x=690,y=170)
        self.kalaNumLbl_order.place(x=510,y=170)
        self.l_purcase_order.place(x=400,y=170)
        self.purcaseLbl_order.place(x=220,y=170)
        self.l_imgSelector_order.place(x=65,y=175)
        self.imgSelectorBg_order.place(x=50,y=25)
        self.listOrder.place(x=60,y=420)


        #________bind___________
        self.listOrder.bind('<ButtonRelease-1>',self.select_record_order)
        self.tickBtnOrder.bind('<Button-1>',self.ready_to_delivery)

    def search_idKala_order(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idKala_order=self.e_idKala_order.get()
        if self.permission==True:
            if self.idKala_order !='':
                self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala_order))
                self.iInfo_order_list = list(self.row)
                self.kalaIdLbl_order['text']=self.iInfo_order_list[0][0]
                self.nameKalaLbl_order['text']=self.iInfo_order_list[0][1]
                self.kalaTypeLbl_order['text']=self.iInfo_order_list[0][2]
                self.groupKalaLbl_order['text']=self.iInfo_order_list[0][3]
                self.kalaNumLbl_order['text']=self.iInfo_order_list[0][7]
                self.purcaseLbl_order['text']=self.iInfo_order_list[0][4]
    
    def search_idUser_order(self,event=None):
        try:
            self.con=sql.connect('mydb.db')
            self.cur=self.con.cursor()
            self.nationalId=self.e_idUser_order.get()
            self.count=0
            if self.nationalId != '':
                self.row=self.cur.execute('SELECT * FROM user WHERE national_code="{}"'.format(self.nationalId))
                self.userInfo_order=list(self.row)
                if self.userInfo_order[0][6]=='فروشنده':
                    self.permission=True
                    self.nameUserLbl_order['text']=self.userInfo_order[0][1]
                    self.lastUserLbl_order['text']=self.userInfo_order[0][2]
                    self.userIdLbl_order['text']=self.userInfo_order[0][0]
                    self.nationalCodeLbl_order['text']=self.userInfo_order[0][3]
                    self.fullname_order=self.userInfo_order[0][1]+' '+self.userInfo_order[0][2]
                    self.con.close()

                else:
                    messagebox.showinfo("information","کاربر با این کد ملی قادر به ثبت ورود کالا نیست")
        except :
            messagebox.showinfo("information","کاربری با این کد ملی وجود ندارد")

    def addOrder(self):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.numKalaOrder = self.e_orderNum.get()
        self.randomId=str(uuid.uuid4())
        self.randomId=self.randomId[:8]
        if self.numKalaOrder != '':
            self.fullNameUser = self.userInfo_order[0][1]+' '+self.userInfo_order[0][2]
            self.data=(self.iInfo_order_list[0][0],self.iInfo_order_list[0][1],self.fullNameUser,self.numKalaOrder,self.iInfo_order_list[0][7],
                       self.iInfo_order_list[0][4],'سفارش داده شد','01/01',self.randomId)
            self.cur.execute('''CREATE TABLE IF NOT EXISTS orders (idKala TEXT  NOT NULL ,nameKala TEXT NOT NULL ,nameUser TEXT NOT NULL
            ,numOrder TEXT NOT NULL,stock TEXT NOT NULL,purchase TEXT NOT NULL,condition TEXT,date INTEGER NOT NULL,orderId)''')
            self.cur.execute('INSERT INTO orders(idKala,nameKala,nameUser,numOrder,stock,purchase,condition,date,orderId) VALUES(?,?,?,?,?,?,?,?,?)',self.data)
            self.con.commit()
            self.numlist=len(self.listOrder.get_children())
            self.listOrder.insert(parent='',index='end',text='',values=('01/01',self.iInfo_order_list[0][7],self.numKalaOrder,
                                    self.randomId,self.fullNameUser,self.iInfo_order_list[0][1],self.iInfo_order_list[0][0],self.numlist+1))
            self.e_orderNum.delete(0,END)
            self.e_idUser_order.delete(0,END)
            self.e_idKala_order.delete(0,END)
            self.nameUserLbl_order['text']=''
            self.lastUserLbl_order['text']=''
            self.userIdLbl_order['text']=''
            self.nationalCodeLbl_order['text']=''
            self.fullname_order=''
            self.kalaIdLbl_order['text']=''
            self.nameKalaLbl_order['text']=''
            self.kalaTypeLbl_order['text']=''
            self.groupKalaLbl_order['text']=''
            self.kalaNumLbl_order['text']=''
            self.purcaseLbl_order['text']=''
            self.permission=False
            self.e_idUser_order.focus()
        
    def data_to_list_order(self):
        self.lst=[]
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        self.result = self.cur.fetchone()
        if self.result != None:
            row=self.cur.execute('SELECT * FROM orders')
            self.list_order=list(row)
            for i in self.list_order :
                if i[6] == 'سفارش داده شد':
                    self.lst.append(i)
            for i in self.lst:
                self.numlist_order=len(self.listOrder.get_children())
                self.listOrder.insert(parent='',index='end',text='',
                    values=('01/01',i[4],i[3],i[8],i[2],i[1],i[0],self.numlist_order+1))
    def select_record_order(self ,event=None):
        self.selected = self.listOrder.focus()
        self.values_order_list = self.listOrder.item(self.selected , "values")
        self.row_id_order =self.listOrder.identify_row(event.y)
        start = self.listOrder.bbox(self.row_id_order, column=None)
        self.y1=start[1]+420
        self.tickBtnOrder.place(x=20,y=self.y1)

    def ready_to_delivery(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        orderIdCheck=self.values_order_list[3]
        self.cur.execute(''' UPDATE orders SET condition = ?  WHERE orderId= ? ''',("آماده تحویل",orderIdCheck))
        self.listOrder.delete(orderIdCheck)
        self.con.commit()

#_____________________________________________________________________________________________________________________________________________
#______________________________________________________________ exit kala page _______________________________________________________________
    def exit_kala_page(self):
        exit_page.geometry('1400x800+250+100')
        exit_page.configure(bg='white')
        exit_page.title('menu')
        exit_page.state('normal')

        self.h_sabtExitKalaImg = PhotoImage(file='image/sabtExitKala.png')
        self.exitKalaImg = PhotoImage(file='image/sabtExitBtn.png')

        self.h_exitPage = Label(exit_page,image=self.h_sabtExitKalaImg)
        #list
        self.listExit= ttk.Treeview(exit_page,show='headings',height=15)
        self.listExit['columns']=('date','stock','orderNum','orderId','userName','NameKala','id','row')
        self.b_exit_kala = Button(exit_page,bg='#F3F3F3',image=self.exitKalaImg,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.sabt_exit_kala)
        #columns
        self.listExit.column('date',width=140,anchor=CENTER)
        self.listExit.column('stock',width=140,anchor=CENTER)
        self.listExit.column('orderId',width=210,anchor=E)
        self.listExit.column('orderNum',width=130,anchor=CENTER)
        self.listExit.column('userName',width=230,anchor=E)
        self.listExit.column('NameKala',width=185,anchor=E)
        self.listExit.column('id',width=130,anchor=CENTER)
        self.listExit.column('row',width=130,anchor=CENTER)
        #heading
        self.listExit.heading('date',text=' : تاریخ',anchor=E)
        self.listExit.heading('stock',text=' : موجودی',anchor=E)
        self.listExit.heading('orderId',text=' : کد سفارش',anchor=E)
        self.listExit.heading('orderNum',text=' : تعداد سفارش',anchor=E)
        self.listExit.heading('userName',text=' : نام سفارش دهنده',anchor=E)
        self.listExit.heading('NameKala',text=' : نام کالا',anchor=E)
        self.listExit.heading('id',text=' : کد کالا',anchor=E)
        self.listExit.heading('row',text=' : ردیف',anchor=E)
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading",font=('Lalezar', 16),
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
    

        self.h_exitPage.place(x=590,y=0)
        self.listExit.place(x=60,y=100)
        self.b_exit_kala.place(x=630,y=720)

        self.listExit.bind('<ButtonRelease-1>',self.select_record_exit)
    
    def data_to_list_exit(self):
        self.lst=[]
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        self.result = self.cur.fetchone()
        if self.result != None:
            row=self.cur.execute('SELECT * FROM orders')
            self.list_exit=list(row)
            for i in self.list_exit :
                if i[6] == 'آماده تحویل':
                    self.lst.append(i)
            for i in self.lst:
                self.numlist_exit=len(self.listExit.get_children())
                self.listExit.insert(parent='',index='end',text='',
                    values=('01/01',i[4],i[3],i[8],i[2],i[1],i[0],self.numlist_exit+1))

    def select_record_exit(self ,event=None):
        self.selected_exit = self.listExit.focus()
        self.values_exit_list = self.listExit.item(self.selected_exit , "values")

    def sabt_exit_kala(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        exitIdCheck=self.values_exit_list[3]
        self.cur.execute(''' UPDATE orders SET condition = ?  WHERE orderId= ? ''',("تحویل داده شد",exitIdCheck))
        self.con.commit()

    
O = App(main_page)
main_page.mainloop()