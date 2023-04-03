from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sqlite3 as sql
import numpy as np
from tkinter import messagebox
import uuid
from datetime import datetime
from tkcalendar import DateEntry
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import io
from PIL import ImageTk, Image

main_page = Tk()
register_page = Toplevel()
login_page = Toplevel()
product_page = Toplevel()
user_page = Toplevel()
chart_page = Toplevel()
stock_page = Toplevel()
receipt_page = Toplevel()
request_page = Toplevel()
order_page = Toplevel()
exit_page = Toplevel()
history_page = Toplevel()
sodorbill_page = Toplevel()
bill_page = Toplevel()


class Phone_number:
    def __set_name__ (self,instance,key):
        self.key=key

    def __get__ (self,instance,owner):
        return instance.__dict__[self.key]
    
    def __set__ (self,instance,value):
        if len(value) == 11 and value.isdigit() and value[0] == '0':
            instance.__dict__[self.key]=value
        else:
            instance.__dict__[self.key]='Error!'

    def __delete__ (self,instance):
        del instance.dict[self.key]

class App:
    '''
    production time : 2023/04
    App builder : Mohammad Panahi Nik

    '''
    phoneNum=Phone_number()

    def __init__(self,event=None):
        main_page.state('withdraw')
        register_page.state('withdraw')
        login_page.state('withdraw')
        product_page.state ('withdraw')
        user_page.state ('withdraw')
        stock_page.state ('withdraw')
        receipt_page.state ('withdraw')
        request_page.state('withdraw')
        order_page.state('withdraw')
        exit_page.state('withdraw')
        history_page.state('withdraw')
        sodorbill_page.state('withdraw')
        bill_page.state('withdraw')
        chart_page.state('withdraw')
        self.btnState = False
        self.permission=False
        self.style=ttk.Style()
        self.lst=[]
        self.search_list=[]

        self.main()
        self.add_product_page()
        self.warehouse_stock_page()
        self.add_user_page()
        self.warehouse_receipt_page()
        self.warehouse_login_page()
        self.warehouse_register_page()
        self.check_exist_user()
        self.request_product_page()
        self.order_kala_page()
        self.exit_kala_page()
        self.order_history_page()
        self.sodor_bill_kala_page()
        self.bill_kala_page()
        self.chartkala_page()

        self.update_time()
        self.update_time_product()
        self.update_time_user()
        self.update_time_stock()
        self.update_time_receipt()
        self.update_time_request()
        self.update_time_order()
        self.update_time_exit()
        self.update_time_history()
        self.update_time_bill()

    def main(self):
        main_page.geometry('1400x800+250+100')
        main_page.configure(bg='white')
        main_page.title('نرم افزار انبارداری')
        main_page.resizable(False,False)
        main_page.iconbitmap('image/warehouseIco.ico')
        
        #image
        self.addUserImg=PhotoImage(file='image/adduserImg.png')
        self.addWareImg=PhotoImage(file='image/addWareImg.png')
        self.WrStockImg=PhotoImage(file='image/WrStockImg.png')
        self.ReceiptImg=PhotoImage(file='image/ReceiptImg.png')
        self.requestImg=PhotoImage(file='image/requestImg.png')
        self.issuanceImg=PhotoImage(file='image/fishBtnMenuImg.png')
        self.homePageBtnImg=PhotoImage(file='image/homePageBtnImg.png')
        self.exitImg=PhotoImage(file='image/exitImg.png')
        self.sabtSefareshBtnImg=PhotoImage(file='image/sabtSefareshBtnImg.png')
        self.exitKalaBtnMenuImg=PhotoImage(file='image/exitKalaBtnMenuImg.png')
        self.closeBtnImg=PhotoImage(file='image/closeImg.png')
        self.openBtnImg=PhotoImage(file='image/openNavImg.png')
        self.historyBtnImg=PhotoImage(file='image/historyOrderBtnImg.png')
        self.bgDateImg=PhotoImage(file='image/bgDateImg.png')
        self.mainBgImg=PhotoImage(file='image/mainPageBg.png')
        
        self.l_mainPageBg=Label(main_page,image=self.mainBgImg, height=800,width=1400,bd=0)
        self.dateFrm=Label(main_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label=Label(self.dateFrm)
        self.date_label=Label(self.dateFrm)
        self.navFrm=Frame(main_page,height=800,width=220,bg='#777777',bd=0)
        self.b_home_page=Button(self.navFrm,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_addUser=Button(self.navFrm,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.open_addUser_page)
        self.b_addWare=Button(self.navFrm,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.open_addKala_page)
        self.b_WrStock=Button(self.navFrm,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.open_stock_page)
        self.b_Receipt=Button(self.navFrm,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.open_receipt_page)
        self.b_request=Button(self.navFrm,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.open_request_page)
        self.b_sabtSefareshPage=Button(self.navFrm,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.open_sabtSefaresh_page)
        self.b_sabtExitKalaPage=Button(self.navFrm,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.open_sabtExit_page)
        self.b_historyOrder=Button(self.navFrm,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.open_history_page)
        self.b_bill_main=Button(self.navFrm,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.open_sodorbill_page)
        self.b_exit=Button(self.navFrm,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.l_mainPageBg.place(x=0,y=0)
        self.dateFrm.place(x=0,y=0)
        self.date_label.place(x=15,y=4)
        self.time_label.place(x=190,y=4)
        self.navFrm.place(x=1180,y=0)
        self.b_home_page.place(x=0,y=0)
        self.b_addWare.place(x=0,y=65)
        self.b_addUser.place(x=0,y=130)
        self.b_WrStock.place(x=0,y=195)
        self.b_Receipt.place(x=0,y=260)
        self.b_request.place(x=0,y=325)
        self.b_sabtSefareshPage.place(x=0,y=390)
        self.b_sabtExitKalaPage.place(x=0,y=455)
        self.b_historyOrder.place(x=0,y=520)
        self.b_bill_main.place(x=0,y=585)
        self.b_exit.place(x=0,y=650)

    def update_time(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm.after(1000, self.update_time)

    def open_addKala_page(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page .state('normal')
        main_page.state('withdraw')
        self.btnState = True

    def open_history_page(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True

    def open_sodorbill_page(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        main_page.state('withdraw')
        self.btnState = True

    def open_addUser_page(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True
    
    def open_stock_page(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True
    
    def open_receipt_page(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True

    def open_request_page(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True

    def open_sabtSefaresh_page(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True

    def open_sabtExit_page(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True

#_____________________________________________________________________________________________________________________
#_________________________________________________login page__________________________________________________________
    def warehouse_login_page(self):
        login_page.geometry('400x510+1000+300')
        login_page.configure(bg='white')
        login_page.title('نرم افزار انبارداری')
        login_page.resizable(False,False)
        login_page.iconbitmap('image/warehouseIco.ico')

        self.logFrmImg = PhotoImage(file='image/loginFrm.png')
        self.logoImg = PhotoImage(file='image/logoImg.png')
        self.logBtnImg = PhotoImage(file='image/loginBtn.png')
        self.eyeImg = PhotoImage(file='image/openEye.png')

        self.logoImgLog = Label(login_page,image=self.logoImg,bg='white')
        self.l_userIdLog = Label(login_page,text=' : کد کاربری',font=('Lalezar',17),bg='white')
        self.e_userIdLog = Entry(login_page,font=('arial',18),justify=RIGHT,bd=2,relief='solid')
        self.l_passwordLog = Label(login_page,text=' : رمز عبور',font=('Lalezar',17),bg='white')
        self.e_passwordLog = Entry(login_page,font=('arial',18),justify=RIGHT,bd=2,relief='solid',show='*')
        self.showBtn = Button(login_page,image=self.eyeImg,bd=0,activebackground='white')
        self.b_enterBtn =Button(login_page,image=self.logBtnImg ,activebackground='white',bd=0,command=self.logIn)
        self.l_register_log = Label(login_page,text='ثبت حساب جدید',font=('Lalezar',17),bg='white',fg='#00348E',cursor='hand2')
        self.b_enterBtn =Button(login_page,image=self.logBtnImg ,activebackground='white',bd=0,command=self.logIn)

        self.logoImgLog.place(x=135,y=10)
        self.l_userIdLog.place(x=250,y=175)
        self.e_userIdLog.place(x=80,y=215)
        self.l_passwordLog.place(x=270,y=275)
        self.e_passwordLog.place(x=80,y=316)
        self.showBtn.place(x=20,y=310)
        self.l_register_log.place(x=125,y=450)
        self.b_enterBtn.place(x=120,y=380)

        self.e_userIdLog.focus()
        self.l_register_log.bind('<Button-1>',self.login_to_register )
        self.e_userIdLog.bind('<Return>',lambda event : self.e_passwordLog.focus())
        self.e_passwordLog.bind('<Return>',lambda event : self.b_enterBtn.focus())
        self.showBtn.bind('<Button-1>',self.funcShow)

    def login_to_register(self,event=None):
        register_page.state('normal')
        login_page.state('withdraw')
        self.e_userIdLog.delete(0,END)
        self.e_passwordLog.delete(0,END)
        self.e_userIdLog.focus()

    def funcShow(self,event=None):
        if self.e_passwordLog['show']=='*':
            self.e_passwordLog['show']=''
            self.eyeImg['file']='image/closeEye.png'
        else:
            self.e_passwordLog['show']='*'
            self.eyeImg['file']='image/openEye.png'
    
    def logIn(self):
        lst=[]
        self.log_peremision=False
        userId =self.e_userIdLog.get()
        userPass =self.e_passwordLog.get()
        self.con=sql.connect('mydb.db')

        if userId == '' or userPass == '': 
            messagebox.showerror('ERROR', '!کد کاربری یا رمز عبور را وارد نکرده اید  ')
            self.e_userIdLog.delete(0,END)
            self.e_passwordLog.delete(0,END)
            self.e_userIdLog.focus()
        else:
            self.cur=self.con.cursor()
            row=self.cur.execute('SELECT * FROM admins')
            row=list(row)
            for i in row:
                lst.append(i)
            for i in lst: 
                if i[0]==userId and i[3]==userPass:
                    self.log_peremision = True
            self.check_peremision_log()

    def check_peremision_log(self):
        if self.log_peremision:
            main_page.state('normal')
            login_page.state('withdraw')
        else:
            messagebox.showerror('ERROR', '!کد کاربری یا رمز عبور را اشتباه وارد کرده اید  ')
            self.e_userIdLog.delete(0,END)
            self.e_passwordLog.delete(0,END)
            self.e_userIdLog.focus()

#_____________________________________________________________________________________________________________________
#_________________________________________________ register page _____________________________________________________

    def warehouse_register_page(self):
        
        register_page.geometry('1000x600+450+200')
        register_page.configure(bg='white')
        register_page.title('نرم افزار انبارداری')
        register_page.resizable(False,False)
        register_page.iconbitmap('image/warehouseIco.ico')

        # Images
        self.signin_mainImg = PhotoImage(file='image/signInMainImg.png')
        self.logoImg_signIn = PhotoImage(file='image/logoImgRegister.png')
        self.addpersonalBtnImg = PhotoImage(file='image/registerBtn.png')

        self.img_signin = Label(register_page,image=self.signin_mainImg)
        self.registerFrm = LabelFrame(register_page,width=460,height=600,bg='#F6F5F5',bd=0)
        self.l_headerUser_register=Label(register_page,image=self.logoImg_signIn,bg='#F6F5F5')
        self.l_nameUser_register=Label(register_page,text=' : نام',font=('Lalezar',17))
        self.e_nameUser_register=Entry(register_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=25,relief='solid')
        self.l_lastUser_register=Label(register_page,text=' : نام خانوادگی',font=('Lalezar',17))
        self.e_lastUser_register=Entry(register_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=25,relief='solid')
        self.l_personnelId_register=Label(register_page,text=' : کد کارمند',font=('Lalezar',17))
        self.e_personnelId_register=Entry(register_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=25,relief='solid')
        self.l_UserPass_register=Label(register_page,text=' : رمزعبور',font=('Lalezar',17))
        self.e_UserPass_register=Entry(register_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=25,relief='solid')
        self.b_addPesonnel_register= Button(register_page,bg='#F6F5F5',image=self.addpersonalBtnImg,activebackground='#F6F5F5',bd=0,cursor='hand2',command=self.addPersonalRegister)
        self.l_description = Label(register_page,text='! ابتدا ثبت نام کنید', bg='white',font=('Lalezar',16),fg='black')

        self.img_signin.place (x=0,y=0)
        self.l_headerUser_register.place (x=700,y=0)
        self.registerFrm.place (x=540,y=0)
        self.l_nameUser_register.place(x=875,y=120)
        self.e_nameUser_register.place(x=640,y=160)
        self.l_lastUser_register.place(x=805,y=210)
        self.e_lastUser_register.place(x=640,y=250)
        self.l_personnelId_register.place(x=825,y=300)
        self.e_personnelId_register.place(x=640,y=335)
        self.l_UserPass_register.place(x=840,y=385)
        self.e_UserPass_register.place(x=640,y=425)
        self.b_addPesonnel_register.place(x=700,y=485)
        self.l_description.place(x=705,y=545)

        # bind
        self.e_nameUser_register.focus()
        self.e_nameUser_register.bind ('<Return>',lambda event : self.e_lastUser_register.focus())
        self.e_lastUser_register.bind ('<Return>',lambda event : self.e_personnelId_register.focus())
        self.e_personnelId_register.bind ('<Return>',lambda event : self.e_UserPass_register.focus())

    def funcBtnHover(self,img,url):
        img['file'] = url

    def addPersonalRegister(self):
        self.pesonnelName_register=self.e_nameUser_register.get()
        self.pesonnelLast_register=self.e_lastUser_register.get()
        self.personnelId_register=self.e_personnelId_register.get()
        self.personnelPass_register=self.e_UserPass_register.get()

        self.e_nameUser_register.delete(0,END)
        self.e_lastUser_register.delete(0,END)
        self.e_personnelId_register.delete(0,END)
        self.e_UserPass_register.delete(0,END)
        self.e_nameUser_register.focus()

        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        data=(self.personnelId_register,self.pesonnelName_register,self.pesonnelLast_register,self.personnelPass_register)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS admins (id TEXT PRIMARY KEY NOT NULL ,name TEXT NOT NULL ,
        last_name TEXT NOT NULL,personnel_pass TEXT NOT NULL)''')
        self.cur.execute('INSERT INTO admins (id,name,last_name,personnel_pass) VALUES(?,?,?,?)',data)
        self.con.commit()
        self.con.close()
        register_page.state('withdraw')
        main_page.state('normal')

    def check_exist_user(self):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admins'")
        result = self.cur.fetchone()
        if result != None :
            login_page.state('normal')
            self.l_description['text']='آیا حساب کاربری دارید؟'
            self.l_register_to_login=Label(register_page,text='ورود',fg='#00348E',cursor='hand2',font=('Lalezar',17))
            self.l_register_to_login.place(x=660,y=545)
            self.l_register_to_login.bind('<Button-1>',self.register_to_login)
        else:
            register_page.state('normal')

    def register_to_login(self,event=None):
        login_page.state('normal')
        register_page.state('withdraw')
        self.e_nameUser_register.delete(0,END)
        self.e_lastUser_register.delete(0,END)
        self.e_personnelId_register.delete(0,END)
        self.e_UserPass_register.delete(0,END)
        self.e_nameUser_register.focus()

#______________________________________________________________________________________________________________________
#_________________________________________________ add product page ____________________________________________________

    def add_product_page(self):
        self.fildsBgImg = PhotoImage(file='image/fildsBg.png')
        self.kalaImg_kala = PhotoImage(file='image/imgSelectorBg.png')
        self.listKalaBgImg = PhotoImage(file='image/listSkalaBg.png')
        self.searchBtnImg_kala1 = PhotoImage(file='image/searchBtnImg.png')
        self.h_sabtKalaImg = PhotoImage(file='image/headerSabtKala.png')
        self.addKalaBtnImg = PhotoImage(file='image/addKalaBtn.png')
        self.deleteBtnImg_kala = PhotoImage(file='image/deleteBtnImg.png')
        self.editBtnImg_kala = PhotoImage(file='image/editBtnImg.png')
        self.sabtTaghirKalaBtn = PhotoImage(file='image/sabtEdit.png')

        product_page.geometry ('1400x800+250+100')
        product_page.title('نرم افزار انبارداری')
        product_page.resizable(False,False)
        product_page.configure(bg='#F6F5F5')
        product_page.iconbitmap('image/warehouseIco.ico')

        self.h_sabtKala_kala = Label(product_page,image=self.h_sabtKalaImg,bg='#F6F5F5')
        self.l_productId_kala = Label(product_page,text=' : کد کالا',font=('Lalezar',17),bg='#F6F5F5')
        self.e_productId_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_productName_kala = Label(product_page,text=' : نام کالا',font=('Lalezar',17),bg='#F6F5F5')
        self.e_productName_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_productType_kala = Label(product_page,text=' : نوع کالا',font=('Lalezar',17),bg='#F6F5F5')
        self.c_productType_kala = ttk.Combobox(product_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                            justify = 'right',values=[ "کالای خریداری شده","کالای مصرفی", "کالای تولید شده برای فروش"])
        self.l_groupType_kala = Label(product_page,text=' : گروه کالا',font=('Lalezar',17),bg='#F6F5F5')
        self.c_groupType_kala = ttk.Combobox(product_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["مواد غذایی","لوازم آشپزخانه","لوازم الکترونیکی"])
        self.c_productType_kala.set("یک گزینه را انتخاب کنید")
        self.c_groupType_kala.set("یک گزینه را انتخاب کنید")
        self.l_description_kala = Label(product_page,text=' : توضیحات',font=('Lalezar',17),bg='#F6F5F5')
        self.e_description_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=28,relief='solid')
        self.l_purchase_kala = Label(product_page,text=' : نقطه خرید',font=('Lalezar',17),bg='#F6F5F5')
        self.e_purchase_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_imgSelector_kala = Label(product_page,text='انتخاب تصویر',font=('Lalezar',17),bg='#F6F5F5')
        self.imgSelectorBg_kala = Label(product_page,bg='#F6F5F5',image=self.kalaImg_kala,cursor='hand2',width=150,height=150)
        self.e_search_kala = Entry(product_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid',bg='#F6F5F5')
        self.b_search_kala = Button(product_page,bg='#F6F5F5',image=self.searchBtnImg_kala1,activebackground='#F6F5F5',bd=0,cursor='hand2',command=self.search_id_kalaPage)
        self.b_addKala_kala = Button(product_page,bg='#F6F5F5',image=self.addKalaBtnImg,activebackground='#F6F5F5',bd=0,cursor='hand2',command=self.funcAddKala)
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
        
        self.dateFrm_product = Label(product_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label_product = Label(self.dateFrm_product)
        self.date_label_product = Label(self.dateFrm_product)
        self.b_openNav_product=Button(product_page,image=self.openBtnImg,bg='#F6F5F5',activebackground='white',bd=0,command=self.switch_product_nav,cursor='hand2')
        self.navFrm_product=Frame(product_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_product=LabelFrame(self.navFrm_product,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_product=Button(self.closeFrm_product,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_product_nav)
        self.b_mainpage_product=Button(self.navFrm_product,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_main)
        self.b_addKala_product=Button(self.navFrm_product,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_addUser_product=Button(self.navFrm_product,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_user)
        self.b_WrStock_product=Button(self.navFrm_product,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_WrStock)
        self.b_Receipt_product=Button(self.navFrm_product,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_Receipt)
        self.b_request_product=Button(self.navFrm_product,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_request)
        self.b_order_product=Button(self.navFrm_product,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_order)
        self.b_exitKala_product=Button(self.navFrm_product,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_exit)
        self.b_history_product=Button(self.navFrm_product,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_history)
        self.b_issuance_product=Button(self.navFrm_product,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.product_to_bill)
        self.b_exit_product=Button(self.navFrm_product,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.dateFrm_product.place(x=0,y=0)
        self.date_label_product.place(x=15,y=4)
        self.time_label_product.place(x=190,y=4)
        self.b_openNav_product.place (x=1340,y=20)
        self.navFrm_product.place (x=1400,y=0)
        self.closeFrm_product.place (x=0,y=0)
        self.b_closeNav_product.place (x=15,y=15)
        self.b_mainpage_product.place (x=0,y=50)
        self.b_addKala_product.place (x=0,y=115)
        self.b_addUser_product.place (x=0,y=180)
        self.b_WrStock_product.place (x=0,y=245)
        self.b_Receipt_product.place (x=0,y=310)
        self.b_request_product.place (x=0,y=375)
        self.b_order_product.place (x=0,y=440)
        self.b_exitKala_product.place (x=0,y=505)
        self.b_history_product.place (x=0,y=570)
        self.b_issuance_product.place (x=0,y=635)
        self.b_exit_product.place (x=0,y=700)
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
        self.e_search_kala.insert(0,'جستجوی کد کالا')
        self.e_search_kala.bind('<Button-1>',lambda event :self.e_search_kala.delete(0,END))

    def update_time_product(self):
        now_product = datetime.now()
        self.current_time_product = now_product.strftime("%H:%M:%S")
        self.current_date_product = now_product.strftime("%Y/%m/%d")
        self.time_label_product.config(text=f"{self.current_time_product}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_product.config(text=f"{self.current_date_product}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_product.after(1000, self.update_time_product)

    def product_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True
        
    def product_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def product_to_bill(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def product_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True
    
    def product_to_WrStock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True
    
    def product_to_Receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def product_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def product_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def product_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

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
            self.listKala.delete(item)
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
        self.procuct_img = Image.open(self.img_name)
        self.procuct_image = self.procuct_img.resize((150, 150))
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.imgSelectorBg_kala['image']=self.product_photo
    
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
        self.imgSelectorBg_kala['image']=self.kalaImg_kala
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
        self.peremision_delete_record = messagebox.askquestion("Confirm","آیا از پاک کردن کالا مطمئن هستید؟")
        if self.peremision_delete_record == 'yes':
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
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT photo FROM kala WHERE id = '{}'".format(self.valuelst[0][0]))
        image_data = self.cur.fetchone()[0]
        procuct_img = Image.open(io.BytesIO(image_data))
        procuct_image = procuct_img.resize((150, 150))
        self.product_photo = ImageTk.PhotoImage(procuct_image)
        self.imgSelectorBg_kala['image']=self.product_photo

    def edit_kala(self,event = None):
        self.peremision_edit_record = messagebox.askquestion("Confirm","آیا از تغییر اطلاعات کالا مطمئن هستید؟")
        if self.peremision_edit_record == 'yes':
            self.con = sql.connect('mydb.db')
            self.cur = self.con.cursor()
            self.code = self.e_productId_kala.get()
            self.name = self.e_productName_kala.get()
            self.point = self.e_purchase_kala.get()
            self.desc = self.e_description_kala.get()
            self.type = self.c_productType_kala.get()
            self.group = self.c_groupType_kala.get()
            self.listKala.item(self.selected ,values = (self.point,self.group,self.type,self.name,self.code,self.row_num))
            self.cur.execute(''' UPDATE kala SET id = "{}" , name = "{}", type = "{}",category = "{}",
            purchase = "{}",description = "{}" WHERE id="{}" '''.format(self.code,self.name,self.type,self.group,self.point,self.desc,self.values[4]))
            self.con.commit()
            self.b_sabtTaghirat_kala.place(x=-100,y=-100)
            self.b_delete_kala.place(x=-50,y=-50)
            self.b_edit_kala.place(x=-50,y=-50)
            self.valuelst=[]
            self.e_productId_kala.delete(0,END)
            self.e_productName_kala.delete(0,END)
            self.c_productType_kala.set("یک گزینه را انتخاب کنید")
            self.c_groupType_kala.set("یک گزینه را انتخاب کنید")
            self.e_purchase_kala.delete(0,END)
            self.e_description_kala.delete(0,END)
            self.e_productId_kala.focus()
            self.imgSelectorBg_kala['image']=self.kalaImg_kala

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
        
        user_page.title('نرم افزار انبارداری')
        user_page.resizable(False,False)
        user_page.iconbitmap('image/warehouseIco.ico')
        user_page.geometry ('1400x800+250+100')
        user_page.configure (bg='#F6F5F5')
    
        self.dateFrm_user=Label(user_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label_user = Label(self.dateFrm_user)
        self.date_label_user = Label(self.dateFrm_user)
        self.l_headerUser=Label(user_page,image=self.hSabtUserImg,bg='#F6F5F5')
        self.l_nameUser=Label(user_page,text=' : نام',font=('Lalezar',17),bg='#F6F5F5')
        self.e_nameUser=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_lastUser=Label(user_page,text=' : نام خانوادگی',font=('Lalezar',17),bg='#F6F5F5')
        self.e_lastUser=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_nationalCode=Label(user_page,text=' : کد ملی',font=('Lalezar',17),bg='#F6F5F5')
        self.e_nationalCode=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_gender=Label(user_page,text=' : جنسیت',font=('Lalezar',17),bg='#F6F5F5')
        self.c_gender=ttk.Combobox(user_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["زن", "مرد"])
        self.c_gender.set("یک گزینه را انتخاب کنید")
        self.l_phoneNum=Label(user_page,text=' : شماره تماس',font=('Lalezar',17),bg='#F6F5F5')
        self.e_phoneNum=Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_accountType=Label(user_page,text=' : نوع کاربری',font=('Lalezar',17),bg='#F6F5F5')
        self.c_accountType=ttk.Combobox(user_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["فروشنده","کارمند"])
        self.c_accountType.set("یک گزینه را انتخاب کنید")
        self.l_personnelId = Label(user_page,text=' : کد کارمند',font=('Lalezar',17),bg='#F6F5F5')
        self.e_personnelId = Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_imgSelector = Label(user_page,text='انتخاب تصویر',font=('Lalezar',17),bg='#F6F5F5')
        self.imgSelectorBg = Label(user_page,bg='#F6F5F5',image=self.UserImg,cursor='hand2',width=150,height=150)
        self.b_addPesonnel= Button(user_page,bg='#F6F5F5',image=self.addPesonnelImg,activebackground='#F6F5F5',bd=0,cursor='hand2')
        self.e_searchUser = Entry(user_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUser = Button(user_page,bg='#F6F5F5',image=self.searchBtnImg_user,activebackground='#F6F5F5',bd=0,cursor='hand2',command=self.search_id_user)
        self.b_delete_user = Button(user_page,image=self.deleteBtnImg_user,bd=0,activebackground='white',cursor='hand2')
        self.b_edit_user = Button(user_page,image=self.editBtnImg_user,bd=0,activebackground='white',cursor='hand2')
        self.b_sabtTaghirat_user = Button(user_page,image=self.sabtTaghirBtn_user,bd=0,activebackground='white')
        
        #list
        self.listUser= ttk.Treeview(user_page,show='headings',height=8)
        self.listUser['columns']=('type','phoneNum','nationalCode','gender','nameUser','personnelId','row')
        #columns
        self.listUser.column('type',width=200,anchor=E)
        self.listUser.column('phoneNum',width=200,anchor=E)
        self.listUser.column('nationalCode',width=200,anchor=E)
        self.listUser.column('gender',width=150,anchor=E)
        self.listUser.column('nameUser',width=250,anchor=E)
        self.listUser.column('personnelId',width=150,anchor=E)
        self.listUser.column('row',width=100,anchor=E)
        #heading
        self.listUser.heading('type',text=' : نوع کاربر',anchor=E)
        self.listUser.heading('phoneNum',text=' : شماره تماس',anchor=E)
        self.listUser.heading('nationalCode',text=' : کد ملی',anchor=E)
        self.listUser.heading('gender',text=' : جنسیت',anchor=E)
        self.listUser.heading('nameUser',text=' : نام و نام خانوادگی',anchor=E)
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

        self.b_openNav_user=Button(user_page,image=self.openBtnImg,bg='#F6F5F5',activebackground='#F6F5F5',bd=0,command=self.switch_user_nav,cursor='hand2')
        self.navFrm_user=Frame(user_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_user=LabelFrame(self.navFrm_user,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_user=Button(self.closeFrm_user,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_user_nav)
        self.b_mainPage_user=Button(self.navFrm_user,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_main)
        self.b_addKala_user=Button(self.navFrm_user,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_kala)
        self.b_addUser_user=Button(self.navFrm_user,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_WrStock_user=Button(self.navFrm_user,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_stock)
        self.b_Receipt_user=Button(self.navFrm_user,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_receipt)
        self.b_request_user=Button(self.navFrm_user,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_request)
        self.b_order_user=Button(self.navFrm_user,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_order)
        self.b_exitKala_user=Button(self.navFrm_user,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_exit)
        self.b_history_user=Button(self.navFrm_user,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_history)
        self.b_issuance_user=Button(self.navFrm_user,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_bill)
        self.b_exit_user=Button(self.navFrm_user,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.dateFrm_user.place(x=0,y=0)
        self.date_label_user.place(x=15,y=4)
        self.time_label_user.place(x=190,y=4)
        self.b_openNav_user.place(x=1340,y=20)
        self.navFrm_user.place(x=1400,y=0)
        self.closeFrm_user.place(x=0,y=0)
        self.b_closeNav_user.place(x=15,y=15)
        self.b_mainPage_user.place(x=0,y=50)
        self.b_addKala_user.place(x=0,y=115)
        self.b_addUser_user.place(x=0,y=180)
        self.b_WrStock_user.place(x=0,y=245)
        self.b_Receipt_user.place(x=0,y=310)
        self.b_request_user.place(x=0,y=375)
        self.b_order_user.place(x=0,y=440)
        self.b_exitKala_user.place(x=0,y=505)
        self.b_history_user.place(x=0,y=570)
        self.b_issuance_user.place(x=0,y=635)
        self.b_exit_user.place(x=0,y=700)
        self.l_headerUser.place(x=595,y=0)
        self.l_nameUser.place(x=1315,y=100)
        self.e_nameUser.place(x=1015,y=100)
        self.l_lastUser.place(x=1245,y=175)
        self.e_lastUser.place(x=1015,y=175)
        self.l_nationalCode.place(x=480,y=175)
        self.e_nationalCode.place(x=245,y=175)
        self.l_gender.place(x=885,y=100)
        self.c_gender.place(x=630,y=100)
        self.l_phoneNum.place(x=855,y=175)
        self.e_phoneNum.place(x=630,y=175)
        self.l_accountType.place(x=1255,y=255)
        self.c_accountType.place(x=1015,y=255)
        self.l_personnelId.place(x=470,y=100)
        self.e_personnelId.place(x=245,y=100)
        self.l_imgSelector.place(x=55,y=260)
        self.imgSelectorBg.place(x=45,y=100)
        self.b_addPesonnel.place(x=1160,y=330)
        self.listUser.place(x=75,y=420)
        self.b_searchUser.place(x=75,y=370)
        self.e_searchUser.place(x=240,y=375)

        #_____ bind _____
        self.e_searchUser.insert(0,'جستجوی کد کاربر')
        self.e_searchUser.bind('<Button-1>', lambda event : self.e_searchUser.delete(0,END))
        self.e_nameUser.focus()
        self.e_nameUser.bind('<Return>',lambda event : self.e_lastUser.focus())
        self.e_lastUser.bind('<Return>',lambda event : self.e_phoneNum.focus())
        self.e_phoneNum.bind('<Return>',lambda event : self.e_personnelId.focus())
        self.e_personnelId.bind('<Return>',lambda event : self.e_nationalCode.focus())
        self.b_addPesonnel.bind('<Button-1>',self.funcAddUser)
        self.imgSelectorBg.bind('<Button-1>', self.funcAddImg)
        self.listUser.bind('<ButtonRelease-1>', self.select_record_user)
        self.b_delete_user.bind('<Button-1>', self.delete_record_user)
        self.b_edit_user.bind('<ButtonRelease-1>', self.edit_record_values_user)
        self.b_sabtTaghirat_user.bind('<Button-1>', self.edit_user)
    
    def update_time_user(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_user.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_user.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_user.after(1000, self.update_time_user)

    def switch_user_nav(self):
        if self.btnState is True:
            self.navFrm_user.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_user.place(x=1180, y=0)
            self.btnState = True
    
    def user_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page .state('normal')
        user_page.state('withdraw')
        self.btnState = True

    def user_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        user_page.state('withdraw')
        self.btnState = True    
    
    def user_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        user_page.state('withdraw')
        self.btnState = True

    def user_to_bill(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        user_page.state('withdraw')
        self.btnState = True

    def user_to_stock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        user_page.state('withdraw')
        self.btnState = True
    
    def user_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        user_page.state('withdraw')
        self.btnState = False

    def user_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        user_page.state('withdraw')
        self.btnState = True

    def user_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        user_page.state('withdraw')
        self.btnState = True

    def user_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        user_page.state('withdraw')
        self.btnState = True

    def funcAddImg(self,event=None):
        self.img_name = filedialog.askopenfilename()
        self.procuct_img = Image.open(self.img_name)
        self.procuct_image = self.procuct_img.resize((150, 150))
        self.product_photo = ImageTk.PhotoImage(self.procuct_image)
        self.imgSelectorBg['image']=self.product_photo

    def covert_to_binary_data(self,filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata
    
    def data_to_list_user(self):
        self.count=0
        self.lst=[]
        for item in self.listUser.get_children():
            self.listUser.delete(item)
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
        self.result = self.cur.fetchone()
        if self.result != None:
            row=self.cur.execute('SELECT * FROM user')
            for i in row :
                self.lst.append(i)
            for i in self.lst:
                fullname_user=i[1]+' '+i[2]
                self.listUser.insert(parent='',index='end',iid=self.count,text='',
                                    values=(i[6],i[5],i[3],i[4],fullname_user,i[0],str(self.count+1)))
                self.count += 1

    def funcAddUser(self , event=None):
        self.phoneNum=self.e_phoneNum.get()
        self.pesonnelName=self.e_nameUser.get()
        self.pesonnelLast=self.e_lastUser.get()
        self.nationalCode=self.e_nationalCode.get()
        self.gender=self.c_gender.get()
        self.accountType=self.c_accountType.get()
        self.personnelId=self.e_personnelId.get()
        self.photo = self.covert_to_binary_data(self.img_name)
        if self.phoneNum != 'Error!':
            self.e_nameUser.delete(0,END)
            self.e_lastUser.delete(0,END)
            self.e_nationalCode.delete(0,END)
            self.c_gender.set("یک گزینه را انتخاب کنید")
            self.e_phoneNum.delete(0,END)
            self.c_accountType.set("یک گزینه را انتخاب کنید")
            self.e_personnelId.delete(0,END)
            self.imgSelectorBg['image']=self.UserImg
            self.e_nameUser.focus()

            self.con=sql.connect('mydb.db')
            self.cur=self.con.cursor()
            self.data=(self.personnelId,self.pesonnelName,self.pesonnelLast,self.nationalCode,self.gender,self.phoneNum,self.accountType,self.photo)
            self.cur.execute('''CREATE TABLE IF NOT EXISTS user (id TEXT PRIMARY KEY NOT NULL ,name TEXT NOT NULL ,last_name TEXT NOT NULL,national_code TEXT NOT NULL
            ,gender INTEGER NOT NULL,phone_number TEXT NOT NULL,account_type TEXT NOT NULL,photo BLOB NOT NULL)''')
            self.cur.execute('INSERT INTO user(id,name,last_name,national_code,gender,phone_number,account_type,photo) VALUES(?,?,?,?,?,?,?,?)',self.data)
            self.con.commit()
            fullname_user=self.pesonnelName+' '+self.pesonnelLast
            self.numlist=len(self.listUser.get_children())
            self.listUser.insert(parent='',index='end',text='',values=(self.accountType,self.phoneNum,self.nationalCode,
                                                                        self.gender,fullname_user,self.personnelId,self.numlist+1))
        elif self.phoneNum == 'Error!':
            messagebox.showerror('ERROR', '! شماره تلفن را درست وارد کنید ')

    def search_id_user(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.idUser=self.e_searchUser.get()
        self.count=0
        if self.idUser !='':
            for i in self.listUser.get_children():
                self.listUser.delete(i)
            self.row=self.cur.execute('SELECT * FROM user WHERE id="{}"'.format(self.idUser))
            self.search_list=list(self.row)
            fullname_user=self.search_list[0][1]+' '+self.search_list[0][2]
            self.listUser.insert(parent='',index='end',iid=self.count,text='',
                                    values=(self.search_list[0][6],self.search_list[0][5],self.search_list[0][3],
                                            self.search_list[0][4],fullname_user,self.search_list[0][0],str(self.count+1)))
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
        self.b_delete_user.place(x=30,y=self.y1)
        self.b_edit_user.place(x=30,y=self.y2)

    def delete_record_user(self,event=None):
        self.peremision_delete_recordUser = messagebox.askquestion("Confirm","آیا از حذف کاربر مطمِن هستید؟")
        if self.peremision_delete_recordUser == 'yes':
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
        self.e_phoneNum.delete(0,END)
        self.e_personnelId.delete(0,END)
        self.values = self.listUser.item(self.selected , "values")
        self.row_num=self.values[6]
        self.valuelst = self.sql_search_user(self.values[5])
        self.e_personnelId.insert(0,self.valuelst[0][0])
        self.e_nameUser.insert(0,self.valuelst[0][1])
        self.e_lastUser.insert(0,self.valuelst[0][2])
        self.e_nationalCode.insert(0,self.valuelst[0][3])
        self.c_gender.set(self.valuelst[0][4])
        self.e_phoneNum.insert(0,self.valuelst[0][5])
        self.c_accountType.set(self.valuelst[0][6])
        self.b_sabtTaghirat_user.place(x=950,y=330)
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT photo FROM user WHERE id = '{}'".format(self.valuelst[0][0]))
        image_data = self.cur.fetchone()[0]
        user_img = Image.open(io.BytesIO(image_data))
        user_image = user_img.resize((150, 150))
        self.user_photo = ImageTk.PhotoImage(user_image)
        self.imgSelectorBg['image']=self.user_photo

    def edit_user(self,event = None):
        self.peremision_edit_recordUser = messagebox.askquestion("Confirm","آیا از تغییر اطلاعات کاربر مطمِن هستید؟")
        if self.peremision_edit_recordUser == 'yes':
            self.con = sql.connect('mydb.db')
            self.cur = self.con.cursor()
            self.pesonnelName=self.e_nameUser.get()
            self.pesonnelLast=self.e_lastUser.get()
            self.nationalCode=self.e_nationalCode.get()
            self.gender=self.c_gender.get()
            self.phoneNum=self.e_phoneNum.get()
            self.accountType=self.c_accountType.get()
            self.personnelId=self.e_personnelId.get()
            fullname_user=self.pesonnelName+' '+self.pesonnelLast
            self.listUser.item(self.selected ,values = (self.accountType,self.phoneNum,self.nationalCode,self.gender,fullname_user,self.personnelId,self.row_num))
            self.cur.execute(''' UPDATE user SET id = "{}" , name = "{}", last_name = "{}",national_code = "{}",
            gender = "{}",phone_number = "{}",account_type ="{}" WHERE id="{}" '''.format(self.personnelId,
                                                        self.pesonnelName,self.pesonnelLast,self.nationalCode,self.gender,
                                                        self.phoneNum,self.accountType,self.values[5]))
            self.con.commit()
            self.b_sabtTaghirat_user.place(x=-100,y=-100)
            self.b_delete_user.place(x=-50,y=-50)
            self.b_edit_user.place(x=-50,y=-50)
            self.e_nameUser.delete(0,END)
            self.e_lastUser.delete(0,END)
            self.e_nationalCode.delete(0,END)
            self.e_phoneNum.delete(0,END)
            self.e_personnelId.delete(0,END)
            self.c_accountType.set('یک گزینه را انتخاب کنید')
            self.c_gender.set('یک گزینه را انتخاب کنید')
            self.imgSelectorBg['image']=self.UserImg


    #____________________________________________________________________________________________________________________
    #________________________________________________ warehouse Stock page ______________________________________________
    def warehouse_stock_page(self):

        self.h_stockImg = PhotoImage(file='image/headerStock.png')
        self.searchBtnImg_stock   = PhotoImage(file='image/searchBtnImg.png')
        self.filterBtnImg = PhotoImage(file='image/filterBtnImg.png')
        self.deleteBtnImg_stock = PhotoImage(file='image/deleteBtnImg.png')
        self.chartBtnImg = PhotoImage(file='image/chartBtnImg.png')

        stock_page.title('نرم افزار انبارداری')
        stock_page.resizable(False,False)
        stock_page.iconbitmap('image/warehouseIco.ico')
        stock_page.geometry ('1400x800+250+100')
        stock_page.configure (bg='#F6F5F5')

        self.dateFrm_stock=Label(stock_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label_stock = Label(self.dateFrm_stock)
        self.date_label_stock = Label(self.dateFrm_stock)
        self.l_headerStock=Label(stock_page,image=self.h_stockImg)
        self.b_filterStock=Button(stock_page,image=self.filterBtnImg,bd=0,activebackground='white',command=self.filter_stock)
        self.c_filterStock = ttk.Combobox(stock_page,width = 20 , font = ('B Koodak' , 12),state='readonly',
                                          justify = 'right',values=["همه ی کالا ها","لوازم الکترونیکی","لوازم آشپزخانه", "مواد غذایی"])
        self.c_filterStock.set("یک گزینه را انتخاب کنید")
        self.l_filterStock=Label(stock_page,text=' : گروه کالا',font=('Lalezar',17))
        self.e_searchStock = Entry(stock_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchStock= Button(stock_page,image=self.searchBtnImg_stock,activebackground='#F6F5F5',bd=0,cursor='hand2',command=self.search_id_stock)
        self.b_chart_stock=Button(stock_page,image=self.chartBtnImg,bd=0,activebackground='#F6F5F5',cursor='hand2',command=self.chartKala)

        #list
        self.listStock= ttk.Treeview(stock_page,show='headings',height=15)

        self.listStock['columns']=('purchase','number','category','type','name','id','row')
        #columns
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
        self.e_searchStock.insert(0,'جستجوی کد کالا')
        self.e_searchStock.bind('<Button-1>', lambda event : self.e_searchStock.delete(0,END))
    
        self.b_openNav_stock=Button(stock_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_stock_nav,cursor='hand2')
        self.navFrm_stock=Frame(stock_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_stock=LabelFrame(self.navFrm_stock,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_stock=Button(self.closeFrm_stock,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_stock_nav)
        self.b_mainPage_stock=Button(self.navFrm_stock,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_main)
        self.b_addKala_stock=Button(self.navFrm_stock,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_kala)
        self.b_addUser_stock=Button(self.navFrm_stock,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_user)
        self.b_WrStock_stock=Button(self.navFrm_stock,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_Receipt_stock=Button(self.navFrm_stock,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_receipt)
        self.b_request_stock=Button(self.navFrm_stock,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_request)
        self.b_order_stock=Button(self.navFrm_stock,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_order)
        self.b_exitKala_stock=Button(self.navFrm_stock,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_exit)
        self.b_history_stock=Button(self.navFrm_stock,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_history)
        self.b_issuance_stock=Button(self.navFrm_stock,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.stock_to_bill)
        self.b_exit_stock=Button(self.navFrm_stock,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')
        
        self.dateFrm_stock.place(x=0,y=0)
        self.date_label_stock.place(x=15,y=4)
        self.time_label_stock.place(x=190,y=4)
        self.b_openNav_stock.place(x=1340,y=20)
        self.navFrm_stock.place(x=1400,y=0)
        self.closeFrm_stock.place(x=0,y=0)
        self.b_closeNav_stock.place(x=15,y=15)
        self.b_mainPage_stock.place(x=0,y=50)
        self.b_addKala_stock.place(x=0,y=115)
        self.b_addUser_stock.place(x=0,y=180)
        self.b_WrStock_stock.place(x=0,y=245)
        self.b_Receipt_stock.place(x=0,y=310)
        self.b_request_stock.place(x=0,y=375)
        self.b_order_stock.place(x=0,y=440)
        self.b_exitKala_stock.place(x=0,y=505)
        self.b_history_stock.place(x=0,y=570)
        self.b_issuance_stock.place(x=0,y=635)
        self.b_exit_stock.place(x=0,y=700)
        self.l_headerStock.place(x=580,y=0)
        self.b_filterStock.place(x=860,y=130)
        self.c_filterStock.place(x=1020,y=135)
        self.l_filterStock.place(x=1230,y=135)
        self.e_searchStock.place(x=245,y=135)
        self.b_searchStock.place(x=85,y=130)
        self.listStock.place(x=85,y=185)
                    
    def update_time_stock(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_stock.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_stock.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_stock.after(1000, self.update_time_stock)     

    def switch_stock_nav(self):
        if self.btnState is True:
            self.navFrm_stock.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_stock.place(x=1180, y=0)
            self.btnState = True
    
    def stock_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page .state('normal')
        stock_page.state('withdraw')
        self.btnState = True

    def stock_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = True
    
    def stock_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = True
    
    def stock_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = True

    def stock_to_bill(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        stock_page.state('withdraw')
        self.btnState = True

    def stock_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = True

    def stock_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = True

    def stock_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = True

    def stock_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = True


    def data_to_list_stock(self):
        self.count=0
        self.lst=[]
        for item in self.listStock.get_children():
            self.listStock.delete(item)
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

    def chartkala_page(self,event=None):
        chart_page.geometry('550x600+700+200')
        chart_page.protocol("WM_DELETE_WINDOW", lambda : chart_page.state('withdraw'))

    def chartKala(self,event=None):
        chart_page.state('normal')
        self.ChartX=[]
        self.ChartY=[]
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        row = self.cur.execute('SELECT * FROM orders WHERE IdKala="{}"'.format(self.rowlistStock))
        row=list(row)
        for i in row:
            if i[6] == 'وارد انبار شد' or i[6] == 'تحویل داده شد':
                self.ChartX.append(i[7])
                self.ChartY.append(i[4])
        self.plotFrm = LabelFrame(chart_page,text='Plot',padx=5,pady=10)
        self.plotFrm.place(x=20,y=20)
        fig = plt.figure(figsize=(5,5))
        self.ChartY.sort(reverse=True)
        plt.plot(self.ChartX,self.ChartY,
                 linewidth=2,
                 linestyle='--',
                 marker='o',
                 markersize=5,
                 markerfacecolor='blue')
        plt.grid(which='both')
        self.bar = FigureCanvasTkAgg(fig,self.plotFrm)
        self.bar.get_tk_widget().pack(side=LEFT,fill=BOTH)

    def select_record_stock(self,event=None):
        self.selected = self.listStock.focus()
        self.values = self.listStock.item(self.selected , "values")
        self.rowlistStock=self.values[5]
        self.row_id = self.listStock.identify_row(event.y)
        start = self.listStock.bbox(self.row_id, column=None)
        self.y1 = start[1]+185
        self.b_chart_stock.place(x=40,y=self.y1)

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
        
        receipt_page.title('نرم افزار انبارداری')
        receipt_page.resizable(False,False)
        receipt_page.iconbitmap('image/warehouseIco.ico')
        receipt_page.configure (bg='#F6F5F5')
        receipt_page.geometry ('1400x800+250+100')
        
        self.searchUserFrm = LabelFrame(receipt_page,bg='#DFDFDF',width=1410,height=170,bd=5,relief=SOLID)
        self.h_vorodKala_receipt = Label(self.searchUserFrm,image=self.headerVorodKalaImg)
        self.l_attention_receipt = Label(self.searchUserFrm,text='.توجه : لطفا ابتدا کد ملی متقاضی مورد نظر را وارد کنید',font=('Lalezar',17),bg='#DFDFDF')
        self.e_searchUser_receipt  = Entry(self.searchUserFrm,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUser_receipt = Button(self.searchUserFrm,bg='#DFDFDF',image=self.searchBtnImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.search_idUser_receipt)
        self.dateFrm_receipt=Label(self.searchUserFrm,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label_receipt = Label(self.dateFrm_receipt)
        self.date_label_receipt = Label(self.dateFrm_receipt)
        self.e_searchKala_receipt = Entry(receipt_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid',fg='#717171')
        self.e_searchKala_receipt.insert(0,'جستجوی کد کالا')
        self.b_searchKala_receipt = Button(receipt_page,bg='#DFDFDF',image=self.searchBtnImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.search_idKala)
        self.infoKalaFrm_receipt = LabelFrame(receipt_page,bg='#EAEAEA',width=1280,height=240,bd=5,relief=SOLID)
        self.l_nameUser_receipt = Label(receipt_page,text=' : نام',font=('Lalezar',17),bg='#EAEAEA')
        self.nameUserLbl_receipt = Label(receipt_page,text='{: ^15}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=12,fg='#4F4E4E')
        self.l_nameKala_receipt = Label(receipt_page,text=' : نام کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.nameKalaLbl_receipt = Label(receipt_page,text='{: ^15}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=12,fg='#4F4E4E')
        self.l_kalaType_receipt = Label(receipt_page,text=' : نوع کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.kalaTypeLbl_receipt =Label(receipt_page,text='{: ^15}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_lastUser_receipt = Label(receipt_page,text=' : نام خانوادگی',font=('Lalezar',17),bg='#EAEAEA')
        self.lastUserLbl_receipt = Label(receipt_page,text='{: ^15}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_kalaId_receipt = Label(receipt_page,text=' : کد کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.kalaIdLbl_receipt = Label(receipt_page,text='{: ^15}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_groupKala_receipt = Label(receipt_page,text=' : گروه کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.groupKalaLbl_receipt = Label(receipt_page,text='{: ^15}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=15,fg='#4F4E4E')
        self.l_stock_receipt = Label(receipt_page,text=' : موجودی',font=('Lalezar',17),bg='#EAEAEA')
        self.stockLbl_receipt = Label(receipt_page,text='{: <6}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=6,fg='#4F4E4E')
        self.l_purchase_receipt = Label(receipt_page,text=' : نقطه خرید',font=('Lalezar',17),bg='#EAEAEA')
        self.purchaseLbl_receipt = Label(receipt_page,text='{: <6}'.format(''),font=('Lalezar',17),bg='#EAEAEA',width=6,fg='#4F4E4E')
        self.l_imgSelector_receipt = Label(receipt_page,text='تصویر',font=('Lalezar',17))
        self.imgSelectorBg_receipt = Label(receipt_page,bg='#F3F3F3',image=self.kalaImg,width=150,height=150)
        self.kalaNumFrm_receipt = LabelFrame(receipt_page,bg='#EAEAEA',width=820,height=70,bd=5,relief=SOLID)
        self.kalaNum_receipt = Label(self.kalaNumFrm_receipt,text=' : تعداد کالا',font=('Lalezar',17),bg='#EAEAEA')
        self.e_kalaNum_receipt = Entry(self.kalaNumFrm_receipt,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid',fg='#717171')
        self.l_date_receipt = Label(self.kalaNumFrm_receipt,text=' : تاریخ',font=('Lalezar',17),bg='#EAEAEA')
        self.date_receipt = DateEntry(self.kalaNumFrm_receipt,font=('Lalezar',14))
        self.b_addKalaNum_receipt = Button(self.kalaNumFrm_receipt,bg='#DFDFDF',image=self.addKalaNumImg,activebackground='#DFDFDF',bd=0,cursor='hand2',command=self.funcAddNum)
        #list
        self.listReceipt= ttk.Treeview(receipt_page,show='headings',height=5)
        self.listReceipt['columns']=('date','kalaNum','receiptId','kalaId','kalaName','fullname','row')
        #columns
        self.listReceipt.column('date',width=150,anchor=E)
        self.listReceipt.column('kalaNum',width=150,anchor=E)
        self.listReceipt.column('receiptId',width=220,anchor=E)
        self.listReceipt.column('kalaId',width=150,anchor=E)
        self.listReceipt.column('kalaName',width=200,anchor=E)
        self.listReceipt.column('fullname',width=240,anchor=E)
        self.listReceipt.column('row',width=120,anchor=E)
        #heading
        self.listReceipt.heading('date',text=' : تاریخ',anchor=E)
        self.listReceipt.heading('kalaNum',text=' : تعداد',anchor=E)
        self.listReceipt.heading('receiptId',text=' : کد خرید',anchor=E)
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
        
        self.b_openNav_receipt=Button(receipt_page,image=self.openBtnImg,bg='#DFDFDF',activebackground='#DFDFDF',bd=0,command=self.switch_receipt_nav,cursor='hand2')
        self.navFrm_receipt=Frame(receipt_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_receipt=LabelFrame(self.navFrm_receipt,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_receipt=Button(self.closeFrm_receipt,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_receipt_nav)
        self.b_mainPage_receipt=Button(self.navFrm_receipt,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_main)
        self.b_addKala_receipt=Button(self.navFrm_receipt,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_kala)
        self.b_addUser_receipt=Button(self.navFrm_receipt,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_user)
        self.b_WrStock_receipt=Button(self.navFrm_receipt,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_stock)
        self.b_Receipt_receipt=Button(self.navFrm_receipt,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_request_receipt=Button(self.navFrm_receipt,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_request)
        self.b_order_receipt=Button(self.navFrm_receipt,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_order)
        self.b_exitKala_receipt=Button(self.navFrm_receipt,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_exit)
        self.b_history_receipt=Button(self.navFrm_receipt,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_history)
        self.b_issuance_receipt=Button(self.navFrm_receipt,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.receipt_to_bill)
        self.b_exit_receipt=Button(self.navFrm_receipt,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.dateFrm_receipt.place(x=0,y=5)
        self.date_label_receipt.place(x=15,y=4)
        self.time_label_receipt.place(x=190,y=4)
        self.b_openNav_receipt.place(x=1340,y=20)
        self.navFrm_receipt.place(x=1400,y=0)
        self.closeFrm_receipt.place(x=0,y=0)
        self.b_closeNav_receipt.place(x=15,y=15)
        self.b_mainPage_receipt.place(x=0,y=50)
        self.b_addKala_receipt.place(x=0,y=115)
        self.b_addUser_receipt.place(x=0,y=180)
        self.b_WrStock_receipt.place(x=0,y=245)
        self.b_Receipt_receipt.place(x=0,y=310)
        self.b_request_receipt.place(x=0,y=375)
        self.b_order_receipt.place(x=0,y=440)
        self.b_exitKala_receipt.place(x=0,y=505)
        self.b_history_receipt.place(x=0,y=570)
        self.b_issuance_receipt.place(x=0,y=635)
        self.b_exit_receipt.place(x=0,y=700)
        self.h_vorodKala_receipt.place(x=610,y=0)
        self.searchUserFrm.place(x=-5,y=-10)
        self.l_attention_receipt.place(x=690,y=90)
        self.e_searchUser_receipt.place(x=475,y=95)
        self.b_searchUser_receipt.place(x=315,y=85)
        self.e_searchKala_receipt.place(x=1115,y=175)
        self.b_searchKala_receipt.place(x=955,y=170)
        self.infoKalaFrm_receipt.place(x=60,y=225)
        self.l_nameUser_receipt.place(x=1275,y=280)
        self.nameUserLbl_receipt.place(x=1095,y=280)
        self.l_nameKala_receipt.place(x=1255,y=360)
        self.nameKalaLbl_receipt.place(x=1095,y=360)
        self.l_lastUser_receipt.place(x=975,y=280)
        self.lastUserLbl_receipt.place(x=795,y=280)
        self.l_kalaId_receipt.place(x=1015,y=360)
        self.kalaIdLbl_receipt.place(x=795,y=360)
        self.l_kalaType_receipt.place(x=700,y=280)
        self.kalaTypeLbl_receipt.place(x=515,y=280)
        self.l_groupKala_receipt.place(x=705,y=360)
        self.groupKalaLbl_receipt.place(x=515,y=360)
        self.l_stock_receipt.place(x=395,y=280)
        self.stockLbl_receipt.place(x=280,y=280)
        self.l_purchase_receipt.place(x=385,y=360)
        self.purchaseLbl_receipt.place(x=280,y=360)
        self.l_imgSelector_receipt.place(x=130,y=400)
        self.imgSelectorBg_receipt.place(x=85,y=250)
        self.kalaNumFrm_receipt.place(x=520,y=460)
        self.kalaNum_receipt.place(x=700,y=10)
        self.e_kalaNum_receipt.place(x=490,y=10)
        self.b_addKalaNum_receipt.place(x=15,y=5)
        self.l_date_receipt.place(x=350,y=10)
        self.date_receipt.place(x=190,y=10)
        self.listReceipt.place(x=85,y=545)
              
    def update_time_receipt(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_receipt.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_receipt.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_receipt.after(1000, self.update_time_receipt)

    def switch_receipt_nav(self):
        if self.btnState is True:
            self.navFrm_receipt.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_receipt.place(x=1180, y=0)
            self.btnState = True
   
    def receipt_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page .state('normal')
        receipt_page.state('withdraw')
        self.btnState = True

    def receipt_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        receipt_page.state('withdraw')
        self.btnState = True
        
    def receipt_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        receipt_page.state('withdraw')
        self.btnState = False

    def receipt_to_bill(self):
        self.navFrm_billing.place(x=1180, y=0)
        sodorbill_page .state('normal')
        receipt_page.state('withdraw')
        self.btnState = True
    
    def receipt_to_stock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        receipt_page.state('withdraw')
        self.btnState = True
    
    def receipt_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        receipt_page.state('withdraw')
        self.btnState = True

    def receipt_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        receipt_page.state('withdraw')
        self.btnState = True

    def receipt_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        receipt_page.state('withdraw')
        self.btnState = True

    def receipt_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        receipt_page.state('withdraw')
        self.btnState = True


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
                    self.fullname_r=self.userInfo[0][1]+' '+self.userInfo[0][2]
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
                self.cur.execute("SELECT photo FROM kala WHERE id = '{}'".format(self.idKala))
                image_data = self.cur.fetchone()[0]
                kala_img = Image.open(io.BytesIO(image_data))
                kala_image = kala_img.resize((150, 150))
                self.kala_photo = ImageTk.PhotoImage(kala_image)
                self.imgSelectorBg_receipt['image']=self.kala_photo

                self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala))
                self.kalaInfo=list(self.row)
                self.nameKalaLbl_receipt['text']=self.kalaInfo[0][1]
                self.kalaTypeLbl_receipt['text']=self.kalaInfo[0][2]
                self.kalaIdLbl_receipt['text']=self.kalaInfo[0][0]
                self.groupKalaLbl_receipt['text']=self.kalaInfo[0][3]
                self.stockLbl_receipt['text']=self.kalaInfo[0][7]
                self.purchaseLbl_receipt['text']=self.kalaInfo[0][4]
                self.e_searchKala_receipt.delete(0,END)
                self.e_searchKala_receipt.insert(0,'جستجوی کد کالا')

    def funcAddNum(self,event=None):
        self.entryNum=self.e_kalaNum_receipt.get()
        self.selected_date_receipt = self.date_receipt.get()
        self.kalaNumber=int(self.entryNum)+int(self.kalaInfo[0][7])
        self.randomId_receipt=str(uuid.uuid4())
        self.randomId_receipt=self.randomId_receipt[:8]
        self.data=(self.kalaInfo[0][0],self.kalaInfo[0][1],self.fullname_r,self.entryNum,self.kalaInfo[0][7],
        self.kalaInfo[0][4],'وارد انبار شد',self.selected_date_receipt,self.randomId_receipt)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS orders (idKala TEXT  NOT NULL ,nameKala TEXT NOT NULL ,nameUser TEXT NOT NULL
        ,numOrder NOT NULL,stock,purchase TEXT NOT NULL,condition TEXT,date INTEGER NOT NULL,orderId)''')
        self.cur.execute('INSERT INTO orders(idKala,nameKala,nameUser,numOrder,stock,purchase,condition,date,orderId) VALUES(?,?,?,?,?,?,?,?,?)',self.data)
        self.cur.execute(''' UPDATE kala SET stock = "{}" WHERE id="{}" '''.format(self.kalaNumber,self.idKala))
        self.cur.execute(''' UPDATE orders SET stock = "{}" WHERE orderId="{}" '''.format(self.kalaNumber,self.randomId_receipt))
        self.con.commit()
        self.num_of_rows = len(self.listReceipt.get_children())
        self.listReceipt.insert(parent='',index='end',text='',
                        values=(self.selected_date_receipt,self.entryNum,self.randomId_receipt,self.kalaInfo[0][0],self.kalaInfo[0][1],self.fullname_r,self.num_of_rows+1))
        self.e_kalaNum_receipt.delete(0,END)
        self.e_searchKala_receipt.delete(0,END)
        self.e_searchKala_receipt.insert(0,'جستجوی کد کالا')
        self.e_searchUser_receipt.delete(0,END)
        self.kalaInfo=[]
        self.fullname=''
        self.nameKalaLbl_receipt['text']=''
        self.kalaTypeLbl_receipt['text']=''
        self.kalaIdLbl_receipt['text']=''
        self.groupKalaLbl_receipt['text']=''
        self.nameUserLbl_receipt['text']=''
        self.lastUserLbl_receipt['text']=''
        self.purchaseLbl_receipt['text']=''
        self.stockLbl_receipt['text']=''
        self.permission=False
        self.imgSelectorBg_receipt['image']=self.kalaImg


    #_____________________________________________________________________________________________________________________________________________
    #______________________________________________________________ request product _____________________________________________________________

    def request_product_page(self):
        
        request_page.title('نرم افزار انبارداری')
        request_page.resizable(False,False)
        request_page.iconbitmap('image/warehouseIco.ico')
        request_page.configure (bg='#F6F5F5')
        request_page.geometry('1400x800+250+100')

        self.headerReguestImg = PhotoImage(file='image/headerRequestImg.png')
        self.requestBtnImg = PhotoImage(file='image/requestBtnImg.png')

        self.dateFrm_request=Label(request_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='#F6F5F5')
        self.time_label_request = Label(self.dateFrm_request)
        self.date_label_request = Label(self.dateFrm_request)
        self.h_requestPage = Label(request_page,image=self.headerReguestImg)
        self.b_requestPage = Button(request_page,image=self.requestBtnImg,bd=0,activebackground='#F6F5F5',command=self.order_kala)
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
        
        self.b_openNav_request=Button(request_page,image=self.openBtnImg,bg='#F6F5F5',activebackground='#F6F5F5',bd=0,command=self.switch_request_nav,cursor='hand2')
        self.navFrm_request=Frame(request_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_request=LabelFrame(self.navFrm_request,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_request=Button(self.closeFrm_request,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_request_nav)
        self.b_mainPage_request=Button(self.navFrm_request,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_main)
        self.b_addKala_request=Button(self.navFrm_request,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_kala)
        self.b_addUser_request=Button(self.navFrm_request,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_user)
        self.b_WrStock_request=Button(self.navFrm_request,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_stock)
        self.b_Receipt_request=Button(self.navFrm_request,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_receipt)
        self.b_request_request=Button(self.navFrm_request,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_order_request=Button(self.navFrm_request,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_order)
        self.b_exitKala_request=Button(self.navFrm_request,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_exit)
        self.b_history_request=Button(self.navFrm_request,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_history)
        self.b_issuance_request=Button(self.navFrm_request,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_bill)
        self.b_exit_request=Button(self.navFrm_request,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.dateFrm_request.place(x=0,y=0)
        self.date_label_request.place(x=15,y=4)
        self.time_label_request.place(x=190,y=4)
        self.b_openNav_request.place(x=1340,y=20)
        self.navFrm_request.place(x=1400,y=0)
        self.closeFrm_request.place(x=0,y=0)
        self.b_closeNav_request.place(x=15,y=15)
        self.b_mainPage_request.place(x=0,y=50)
        self.b_addKala_request.place(x=0,y=115)
        self.b_addUser_request.place(x=0,y=180)
        self.b_WrStock_request.place(x=0,y=245)
        self.b_Receipt_request.place(x=0,y=310)
        self.b_request_request.place(x=0,y=375)
        self.b_order_request.place(x=0,y=440)
        self.b_exitKala_request.place(x=0,y=505)
        self.b_history_request.place(x=0,y=570)
        self.b_issuance_request.place(x=0,y=635)
        self.b_exit_request.place(x=0,y=700)
        #_________________bind_________________
        self.listRequest.bind('<ButtonRelease>',self.select_record_list_request)

        self.h_requestPage.place(x=580,y=0)
        self.listRequest.place(x=85,y=90)
        self.b_requestPage.place(x=600,y=720)
    
    def update_time_request(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_request.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_request.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm.after(1000, self.update_time_request)

    def switch_request_nav(self):
        if self.btnState is True:
            self.navFrm_request.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_request.place(x=1180, y=0)
            self.btnState = True
    
    def request_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page .state('normal')
        request_page.state('withdraw')
        self.btnState = True

    def request_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        request_page.state('withdraw')
        self.btnState = True
    
    def request_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        request_page.state('withdraw')
        self.btnState = False

    def request_to_bill(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        request_page.state('withdraw')
        self.btnState = True

    def request_to_stock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        request_page.state('withdraw')
        self.btnState = True
    
    def request_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        request_page.state('withdraw')
        self.btnState = True

    def request_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        request_page.state('withdraw')
        self.btnState = True

    def request_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        request_page.state('withdraw')
        self.btnState = True

    def request_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        request_page.state('withdraw')
        self.btnState = True

    def data_to_list_request(self):
        self.lst=[]
        for item in self.listRequest.get_children():
            self.listRequest.delete(item)
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
    def order_kala(self):
        if self.btnState == True:
            self.navFrm_receipt.place(x=1180,y=0)
        else:
            self.navFrm_receipt.place(x=1400,y=0)
        receipt_page.state('normal')
        request_page.state('withdraw')
        self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.valuesReq[5]))
        self.row=list(self.row)
        self.limit_order=(self.row[0][4])-int(self.row[0][7])
        self.e_searchKala_receipt.delete(0,END)
        self.e_searchKala_receipt.insert('0',(self.valuesReq[5]))
        self.e_kalaNum_receipt.insert('0',self.limit_order)
        self.con.commit()

    def select_record_list_request(self,event=None):
        self.selected = self.listRequest.focus()
        self.valuesReq = self.listRequest.item(self.selected , "values")
        
#__________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________ order page ______________________________________________________________________________
    def order_kala_page(self):
        order_page.title('نرم افزار انبارداری')
        order_page.resizable(False,False)
        order_page.iconbitmap('image/warehouseIco.ico')
        order_page.configure (bg='#F6F5F5')
        order_page.geometry('1400x800+250+100')
        
        self.headerOrderImg = PhotoImage(file='image/headerOrderKala.png')
        self.sabtOrderBtnImg = PhotoImage(file='image/sabtOrder.png')
        self.searchBtnImg_order = PhotoImage(file='image/searchBtnImg.png')
        self.order_imgSelectorPic = PhotoImage(file='image/imgSelectorBg.png')
        self.order_baresiImg = PhotoImage(file='image/baresiBtnImg.png')
        self.tickImgBtn = PhotoImage(file='image/tickImgBtn.png')

        self.dateFrm_order=Label(order_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='#F6F5F5')
        self.time_label_order = Label(self.dateFrm_order)
        self.date_label_order = Label(self.dateFrm_order)
        self.l_headerOrderPage = Label(order_page,image=self.headerOrderImg)
        self.attention_idUser = Label(order_page,text=' . لطفا کد کاربر موردنطر خود را وارد کنید',font=('Lalezar',17),bg='#F6F5F5')
        self.e_idUser_order = Entry(order_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUserBtnOrder = Button(order_page,image=self.order_baresiImg,bd=0,activebackground='#F6F5F5',command=self.search_idUser_order)
        self.e_idKala_order = Entry(order_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.e_idKala_order.insert(0,'جستجوی کد کالا')
        self.b_searchBtnOrder = Button(order_page,image=self.searchBtnImg_order,bd=0,activebackground='#F6F5F5',command=self.search_idKala_order)
        self.userInfo_order_frm = LabelFrame(order_page,width=510,height=135,bg='#F2F2F2',bd=5,relief=SOLID)
        self.l_nameUser_order = Label(self.userInfo_order_frm,text=' : نام',font=('Lalezar',17),bg='#F2F2F2')
        self.nameUserLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_lastUser_order = Label(self.userInfo_order_frm,text=' : نام خانوادگی',font=('Lalezar',17),bg='#F2F2F2')
        self.lastUserLbl_order =Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_nationalCode_order = Label(self.userInfo_order_frm,text=' : کد ملی',font=('Lalezar',17),bg='#F2F2F2')
        self.nationalCodeLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_userId_order = Label(self.userInfo_order_frm,text=' : کد کاربری',font=('Lalezar',17),bg='#F2F2F2')
        self.userIdLbl_order = Label(self.userInfo_order_frm,text='{: >10}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=8,fg='#4F4E4E')
        self.order_frm_num = LabelFrame(order_page,width=510,height=115,bg='#F2F2F2',bd=5,relief=SOLID)
        self.l_orderNum = Label(self.order_frm_num,text=' : تعداد',font=('Lalezar',17))
        self.e_orderNum = Entry(self.order_frm_num,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.l_date_order = Label(self.order_frm_num,text=' : تاریخ',font=('Lalezar',17),bg='#EAEAEA')
        self.date_order = DateEntry(self.order_frm_num,font=('Lalezar',14))
        self.b_sabtOrder = Button(self.order_frm_num,image=self.sabtOrderBtnImg,bd=0,activebackground='white',command=self.addOrder)
        self.kalaInfo_order_frm = LabelFrame(order_page,width=800,height=240,bg='#D0D0D0',bd=5,relief=SOLID)
        self.l_nameKala_order = Label(self.kalaInfo_order_frm,text=' : نام کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.nameKalaLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_kalaType_order = Label(self.kalaInfo_order_frm,text=' : نوع کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.kalaTypeLbl_order =Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_kalaId_order = Label(self.kalaInfo_order_frm,text=' : کد کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.kalaIdLbl_order = Label(self.kalaInfo_order_frm,text='{: >10}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=10,fg='#4F4E4E')
        self.l_groupKala_order = Label(self.kalaInfo_order_frm,text=' : گروه کالا',font=('Lalezar',17),bg='#D0D0D0')
        self.groupKalaLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_kalaNum_order = Label(self.kalaInfo_order_frm,text=' : موجودی',font=('Lalezar',17),bg='#D0D0D0')
        self.kalaNumLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_purcase_order = Label(self.kalaInfo_order_frm,text=' : نقطه خرید',font=('Lalezar',17),bg='#D0D0D0')
        self.purcaseLbl_order = Label(self.kalaInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#D0D0D0',width=15,fg='#4F4E4E')
        self.l_imgSelector_order = Label(self.kalaInfo_order_frm,text='تصویر',font=('Lalezar',17),bg='#D0D0D0')
        self.imgSelectorBg_order = Label(self.kalaInfo_order_frm,bg='#D0D0D0',image=self.order_imgSelectorPic,width=150,height=150)
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
        
        self.b_openNav_order=Button(order_page,image=self.openBtnImg,bg='#F6F5F5',activebackground='#F6F5F5',bd=0,command=self.switch_order_nav,cursor='hand2')
        self.navFrm_order=Frame(order_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_order=LabelFrame(self.navFrm_order,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_order=Button(self.closeFrm_order,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_order_nav)
        self.b_mainPage_order=Button(self.navFrm_order,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_main)
        self.b_addKala_order=Button(self.navFrm_order,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_kala)
        self.b_addUser_order=Button(self.navFrm_order,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_user)
        self.b_WrStock_order=Button(self.navFrm_order,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_stock)
        self.b_Receipt_order=Button(self.navFrm_order,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_receipt)
        self.b_request_order=Button(self.navFrm_order,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_request)
        self.b_order_order=Button(self.navFrm_order,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_exitKala_order=Button(self.navFrm_order,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_exit)
        self.b_history_order=Button(self.navFrm_order,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_history)
        self.b_issuance_order=Button(self.navFrm_order,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.order_to_bill)
        self.b_exit_order=Button(self.navFrm_order,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')
        
        self.dateFrm_order.place(x=0,y=0)
        self.date_label_order.place(x=15,y=4)
        self.time_label_order.place(x=190,y=4)
        self.b_openNav_order.place(x=1340,y=20)
        self.navFrm_order.place(x=1400,y=0)
        self.closeFrm_order.place(x=0,y=0)
        self.b_closeNav_order.place(x=15,y=15)
        self.b_mainPage_order.place(x=0,y=50)
        self.b_addKala_order.place(x=0,y=115)
        self.b_addUser_order.place(x=0,y=180)
        self.b_WrStock_order.place(x=0,y=245)
        self.b_Receipt_order.place(x=0,y=310)
        self.b_request_order.place(x=0,y=375)
        self.b_order_order.place(x=0,y=440)
        self.b_exitKala_order.place(x=0,y=505)
        self.b_history_order.place(x=0,y=570)
        self.b_issuance_order.place(x=0,y=635)
        self.b_exit_order.place(x=0,y=700)
        self.l_headerOrderPage.place(x=580,y=0)
        self.attention_idUser.place(x=1040,y=90)
        self.e_idUser_order.place(x=835,y=95)
        self.b_searchUserBtnOrder.place(x=670,y=88)
        self.b_searchBtnOrder.place(x=50,y=85)
        self.e_idKala_order.place(x=215,y=90)
        self.order_frm_num.place(x=845,y=275)
        self.l_orderNum.place(x=420,y=15)
        self.e_orderNum.place(x=210,y=15)
        self.l_date_order.place(x=420,y=60)
        self.date_order.place(x=210,y=60)
        self.b_sabtOrder.place(x=20,y=30)
        self.userInfo_order_frm.place(x=845,y=150)
        self.l_nameUser_order.place(x=450,y=10)
        self.nameUserLbl_order.place(x=260,y=10)
        self.l_lastUser_order.place(x=200,y=10)
        self.lastUserLbl_order.place(x=10,y=10)
        self.l_userId_order.place(x=405,y=70)
        self.userIdLbl_order.place(x=300,y=70)
        self.l_nationalCode_order.place(x=220,y=70)
        self.nationalCodeLbl_order.place(x=5,y=70)
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
        self.l_imgSelector_order.place(x=95,y=175)
        self.imgSelectorBg_order.place(x=50,y=25)
        self.listOrder.place(x=60,y=420)

        #________bind___________
        self.listOrder.bind('<ButtonRelease-1>',self.select_record_order)
        self.e_idKala_order.bind('<Button-1>',lambda event :self.e_idKala_order.delete(0,END))
        self.tickBtnOrder.bind('<Button-1>',self.ready_to_delivery)

    def update_time_order(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_order.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_order.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_order.after(1000, self.update_time_order)

    def switch_order_nav(self):
        if self.btnState is True:
            self.navFrm_order.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_order.place(x=1180, y=0)
            self.btnState = True

    def order_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page .state('normal')        
        order_page.state('withdraw')
        self.btnState = False

    def order_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        order_page.state('withdraw')
        self.btnState = False

    def order_to_stock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        order_page.state('withdraw')
        self.btnState = False

    def order_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        order_page.state('withdraw')
        self.btnState = False

    def order_to_bill(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        order_page.state('withdraw')
        self.btnState = True

    def order_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        order_page.state('withdraw')
        self.btnState = False

    def order_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        order_page.state('withdraw')
        self.btnState = False

    def order_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        order_page.state('withdraw')
        self.btnState = False

    def order_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        order_page.state('withdraw')
        self.btnState = False

    def search_idKala_order(self,event=None):
        self.idKala_order=self.e_idKala_order.get()
        if self.permission==True:
            if self.idKala_order !='':
                self.con=sql.connect('mydb.db')
                self.cur=self.con.cursor()
                self.cur.execute("SELECT photo FROM kala WHERE id = '{}'".format(self.idKala_order))
                image_data = self.cur.fetchone()[0]
                procuct_img = Image.open(io.BytesIO(image_data))
                procuct_image = procuct_img.resize((150, 150))
                self.product_photo = ImageTk.PhotoImage(procuct_image)
                self.imgSelectorBg_order['image']=self.product_photo

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
                if self.userInfo_order[0][6]=='کارمند':
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
        self.orderDate=self.date_order.get()
        if self.numKalaOrder != '':
            self.fullNameUser = self.userInfo_order[0][1]+' '+self.userInfo_order[0][2]
            self.data=(self.iInfo_order_list[0][0],self.iInfo_order_list[0][1],self.fullNameUser,self.numKalaOrder,self.iInfo_order_list[0][7],
                       self.iInfo_order_list[0][4],'سفارش داده شد',self.orderDate,self.randomId)
            self.cur.execute('''CREATE TABLE IF NOT EXISTS orders (idKala TEXT  NOT NULL ,nameKala TEXT NOT NULL ,nameUser TEXT NOT NULL
            ,numOrder NOT NULL,stock,purchase TEXT NOT NULL,condition TEXT,date INTEGER NOT NULL,orderId)''')
            self.cur.execute('INSERT INTO orders(idKala,nameKala,nameUser,numOrder,stock,purchase,condition,date,orderId) VALUES(?,?,?,?,?,?,?,?,?)',self.data)
            self.con.commit()
            self.numlist=len(self.listOrder.get_children())
            self.listOrder.insert(parent='',index='end',text='',values=(self.orderDate,self.iInfo_order_list[0][7],self.numKalaOrder,
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
            self.tickBtnOrder.place(x=-50,y=-50)
            self.imgSelectorBg_order['image']=self.order_imgSelectorPic

    def data_to_list_order(self):
        self.lst=[]
        for item in self.listOrder.get_children():
            self.listOrder.delete(item)
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
                    values=(i[7],i[4],i[3],i[8],i[2],i[1],i[0],self.count+1))
                self.count +=1
                
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
        self.con.commit()
        self.data_to_list_order()
        self.tickBtnOrder.place(x=-50,y=-50)

#_____________________________________________________________________________________________________________________________________________
#______________________________________________________________ exit kala page _______________________________________________________________
    def exit_kala_page(self):
        
        exit_page.title('نرم افزار انبارداری')
        exit_page.resizable(False,False)
        exit_page.iconbitmap('image/warehouseIco.ico')
        exit_page.configure (bg='#F6F5F5')
        exit_page.geometry('1400x800+250+100')

        self.h_sabtExitKalaImg = PhotoImage(file='image/sabtExitKala.png')
        self.exitKalaImg = PhotoImage(file='image/sabtExitBtn.png')

        self.dateFrm_exit=Label(exit_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label_exit = Label(self.dateFrm_exit)
        self.date_label_exit = Label(self.dateFrm_exit)
        self.h_exitPage = Label(exit_page,image=self.h_sabtExitKalaImg)
        #list
        self.listExit= ttk.Treeview(exit_page,show='headings',height=15)
        self.listExit['columns']=('date','stock','orderNum','orderId','userName','NameKala','id','row')
        self.b_exit_kala = Button(exit_page,bg='#F6F5F5',image=self.exitKalaImg,activebackground='#F6F5F5',bd=0,cursor='hand2',command=self.sabt_exit_kala)
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
    
        self.b_openNav_exit=Button(exit_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_exit_nav,cursor='hand2')
        self.navFrm_exit=Frame(exit_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_exit=LabelFrame(self.navFrm_exit,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_exit=Button(self.closeFrm_exit,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_exit_nav)
        self.b_mainPage_exit=Button(self.navFrm_exit,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_main)
        self.b_addKala_exit=Button(self.navFrm_exit,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_kala)
        self.b_addUser_exit=Button(self.navFrm_exit,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_user)
        self.b_WrStock_exit=Button(self.navFrm_exit,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_stock)
        self.b_Receipt_exit=Button(self.navFrm_exit,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_receipt)
        self.b_request_exit=Button(self.navFrm_exit,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_request)
        self.b_order_exit=Button(self.navFrm_exit,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_order)
        self.b_exitKala_exit=Button(self.navFrm_exit,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_history_exit=Button(self.navFrm_exit,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_history)
        self.b_issuance_exit=Button(self.navFrm_exit,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.exit_to_bill)
        self.b_exit_exit=Button(self.navFrm_exit,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')
        
        self.dateFrm_exit.place(x=0,y=0)
        self.date_label_exit.place(x=15,y=4)
        self.time_label_exit.place(x=190,y=4)
        self.b_openNav_exit.place(x=1340,y=20)
        self.navFrm_exit.place(x=1400,y=0)
        self.closeFrm_exit.place(x=0,y=0)
        self.b_closeNav_exit.place(x=15,y=15)
        self.b_mainPage_exit.place(x=0,y=50)
        self.b_addKala_exit.place(x=0,y=115)
        self.b_addUser_exit.place(x=0,y=180)
        self.b_WrStock_exit.place(x=0,y=245)
        self.b_Receipt_exit.place(x=0,y=310)
        self.b_request_exit.place(x=0,y=375)
        self.b_order_exit.place(x=0,y=440)
        self.b_exitKala_exit.place(x=0,y=505)
        self.b_history_exit.place(x=0,y=570)
        self.b_issuance_exit.place(x=0,y=635)
        self.b_exit_exit.place(x=0,y=700)
        self.h_exitPage.place(x=590,y=0)
        self.listExit.place(x=60,y=100)
        self.b_exit_kala.place(x=630,y=720)

        self.listExit.bind('<ButtonRelease-1>',self.select_record_exit)
    
    def update_time_exit(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_exit.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_exit.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_exit.after(1000, self.update_time_exit)

    def switch_exit_nav(self):
        if self.btnState is True:
            self.navFrm_exit.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_exit.place(x=1180, y=0)
            self.btnState = True
    
    def exit_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page.state('normal')        
        exit_page.state('withdraw')
        self.btnState = True

    def exit_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        exit_page.state('withdraw')
        self.btnState = True
        
    def exit_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        exit_page.state('withdraw')
        self.btnState = False

    def exit_to_bill(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        exit_page.state('withdraw')
        self.btnState = True

    def exit_to_stock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        exit_page.state('withdraw')
        self.btnState = True
    
    def exit_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        exit_page.state('withdraw')
        self.btnState = True

    def exit_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        exit_page.state('withdraw')
        self.btnState = True

    def exit_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        exit_page.state('withdraw')
        self.btnState = True

    def exit_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        exit_page.state('withdraw')
        self.btnState = True

    def data_to_list_exit(self):
        self.lst=[]
        for item in self.listExit.get_children():
            self.listExit.delete(item)
        self.count=0
        con=sql.connect('mydb.db')
        cur=con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        self.result = cur.fetchone()
        if self.result != None:
            row=cur.execute('SELECT * FROM orders')
            self.list_exit=list(row)
            for i in self.list_exit :
                if i[6] == 'آماده تحویل':
                    self.lst.append(i)
            for i in self.lst:
                self.numlist_exit=len(self.listExit.get_children())
                self.listExit.insert(parent='',index='end',text='',
                    values=(i[7],i[4],i[3],i[8],i[2],i[1],i[0],self.numlist_exit+1))
            con.close()

    def select_record_exit(self ,event=None):
        self.selected_exit = self.listExit.focus()
        self.values_exit_list = self.listExit.item(self.selected_exit , "values")

    def sabt_exit_kala(self,event=None):
        con=sql.connect('mydb.db')
        cur=con.cursor()
        exitIdCheck=self.values_exit_list[3]
        self.new_stock_exit=int(self.values_exit_list[1])-int(self.values_exit_list[2])
        cur.execute(''' UPDATE orders SET condition = ?   WHERE orderId= ? ''',("تحویل داده شد",exitIdCheck))        
        cur.execute(''' UPDATE orders SET stock = ?  WHERE orderId= ? ''',(self.new_stock_exit,exitIdCheck))
        cur.execute(''' UPDATE kala SET stock = ?  WHERE id= ? ''',(self.new_stock_exit,self.values_exit_list[6]))
        con.commit()
        con.close()
        self.data_to_list_exit()
    
    #________________________________________________________________________________________________________________________________________
    #__________________________________________________________ order history page __________________________________________________________

    def order_history_page(self):
        history_page.geometry('1400x800+250+100')
        history_page.configure(bg='white')
        history_page.title('menu')

        self.h_orderHistoryImg = PhotoImage(file='image/headerHistory.png')

        self.dateFrm_history=Label(history_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label_history = Label(self.dateFrm_history)
        self.date_label_history = Label(self.dateFrm_history)
        self.h_orderHistory = Label(history_page,image=self.h_orderHistoryImg)
        #list
        self.listHistory= ttk.Treeview(history_page,show='headings',height=15)
        self.listHistory['columns']=('date','orderNum','IdSefaresh','userName','NameKala','id','sefareshType','row')
        #columns
        self.listHistory.column('date',width=140,anchor=CENTER)
        self.listHistory.column('IdSefaresh',width=210,anchor=E)
        self.listHistory.column('orderNum',width=130,anchor=CENTER)
        self.listHistory.column('userName',width=200,anchor=E)
        self.listHistory.column('NameKala',width=185,anchor=E)
        self.listHistory.column('id',width=130,anchor=CENTER)
        self.listHistory.column('sefareshType',width=170,anchor=E)
        self.listHistory.column('row',width=130,anchor=CENTER)
        #heading
        self.listHistory.heading('date',text=' : تاریخ',anchor=E)
        self.listHistory.heading('IdSefaresh',text=' : کد سفارش',anchor=E)
        self.listHistory.heading('orderNum',text=' : تعداد سفارش',anchor=E)
        self.listHistory.heading('userName',text=' : نام سفارش دهنده',anchor=E)
        self.listHistory.heading('NameKala',text=' : نام کالا',anchor=E)
        self.listHistory.heading('id',text=' : کد کالا',anchor=E)
        self.listHistory.heading('sefareshType',text=' : نوع سفارش',anchor=E)
        self.listHistory.heading('row',text=' : ردیف',anchor=E)
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
    
        self.b_openNav_history=Button(history_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_history_nav,cursor='hand2')
        self.navFrm_history=Frame(history_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_history=LabelFrame(self.navFrm_history,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_history=Button(self.closeFrm_history,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_history_nav)
        self.b_mainPage_history=Button(self.navFrm_history,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_main)
        self.b_addKala_history=Button(self.navFrm_history,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_kala)
        self.b_addUser_history=Button(self.navFrm_history,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_user)
        self.b_WrStock_history=Button(self.navFrm_history,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_stock)
        self.b_Receipt_history=Button(self.navFrm_history,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_receipt)
        self.b_request_history=Button(self.navFrm_history,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_request)
        self.b_order_history=Button(self.navFrm_history,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_order)
        self.b_exitKala_history=Button(self.navFrm_history,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_exit)
        self.b_history_history=Button(self.navFrm_history,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_issuance_history=Button(self.navFrm_history,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',command=self.history_to_bill)
        self.b_exit_history=Button(self.navFrm_history,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')
        
        self.b_openNav_history.place(x=1340,y=20)
        self.navFrm_history.place(x=1400,y=0)
        self.closeFrm_history.place(x=0,y=0)
        self.b_closeNav_history.place(x=15,y=15)
        self.b_mainPage_history.place(x=0,y=50)
        self.b_addKala_history.place(x=0,y=115)
        self.b_addUser_history.place(x=0,y=180)
        self.b_WrStock_history.place(x=0,y=245)
        self.b_Receipt_history.place(x=0,y=310)
        self.b_request_history.place(x=0,y=375)
        self.b_order_history.place(x=0,y=440)
        self.b_exitKala_history.place(x=0,y=505)
        self.b_history_history.place(x=0,y=570)
        self.b_issuance_history.place(x=0,y=635)
        self.b_exit_history.place(x=0,y=700)
        self.dateFrm_history.place(x=0,y=0)
        self.date_label_history.place(x=15,y=4)
        self.time_label_history.place(x=190,y=4)
        self.h_orderHistory.place(x=590,y=0)
        self.listHistory.place(x=50,y=150)        
                    
    def update_time_history(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_history.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_history.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_history.after(1000, self.update_time_history)

    def switch_history_nav(self):
        if self.btnState is True:
            self.navFrm_history.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_history.place(x=1180, y=0)
            self.btnState = True
    
    def history_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page.state('normal')        
        history_page.state('withdraw')
        self.btnState = True

    def history_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        history_page.state('withdraw')
        self.btnState = True
        
    def history_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_history()
        exit_page.state('normal')
        history_page.state('withdraw')
        self.btnState = False

    def history_to_bill(self):
        self.navFrm_bill.place(x=1180, y=0)
        sodorbill_page .state('normal')
        history_page.state('withdraw')
        self.btnState = True

    def history_to_stock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        history_page.state('withdraw')
        self.btnState = True
    
    def history_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        history_page.state('withdraw')
        self.btnState = True

    def history_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        history_page.state('withdraw')
        self.btnState = True

    def history_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        history_page.state('withdraw')
        self.btnState = True

    def history_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        history_page.state('withdraw')
        self.btnState = True

    def data_to_list_history (self):
        self.lst=[]
        for item in self.listHistory.get_children():
            self.listHistory.delete(item)
        count=0
        con=sql.connect('mydb.db')
        cur=con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        self.result = cur.fetchone()
        if self.result != None:
            row=cur.execute('SELECT * FROM orders')
            self.list_history=list(row)
            for i in self.list_history :
                if i[6] == 'وارد انبار شد':
                    self.lst.append(i)
                elif i[6] == 'تحویل داده شد':
                    self.lst.append(i)
            for i in self.lst:
                if i[6] == 'وارد انبار شد':
                    self.numlist_order=len(self.listHistory.get_children())
                    self.listHistory.insert(parent='',index='end',text='',
                        values=(i[7],i[3],i[8],i[2],i[1],i[0],'ورود',self.count+1))
                    self.count +=1
                elif i[6] == 'تحویل داده شد':
                    self.numlist_order=len(self.listHistory.get_children())
                    self.listHistory.insert(parent='',index='end',text='',
                        values=(i[7],i[3],i[8],i[2],i[1],i[0],'خروج',self.count+1))
                    self.count +=1
            con.close()

#______________________________________________________________________________________________________________________________________________
#___________________________________________________________ sodor bill page __________________________________________________________________
    def sodor_bill_kala_page(self):
        
        sodorbill_page.title('نرم افزار انبارداری')
        sodorbill_page.resizable(False,False)
        sodorbill_page.iconbitmap('image/warehouseIco.ico')
        sodorbill_page.configure (bg='#F6F5F5')
        sodorbill_page.geometry('1400x800+250+100')
        
        self.searchBtnImg_kala = PhotoImage(file='image/searchBtnImg.png')
        self.h_billImg = PhotoImage(file='image/headerSodorghabz.png')
        self.billBtnImg = PhotoImage(file='image/sodorGhabzBtn.png')

        self.headerBillPage = Label(sodorbill_page,image=self.h_billImg)
        self.l_SearchKala_bill = Label(sodorbill_page,text='کد کالا یا کد سفارش مورد نظر خود را وارد کنید',font=('Lalezar',17),bg='#F2F2F2')
        self.e_SearchKala_bill = Entry(sodorbill_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_SearchKala_bill =  Button(sodorbill_page,bg='#F3F3F3',image=self.searchBtnImg_user,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.searchIdBill)
        self.b_blii =  Button(sodorbill_page,bg='#F3F3F3',image=self.billBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.sodorBill)
        #list
        self.listBill= ttk.Treeview(sodorbill_page,show='headings',height=14)
        self.listBill['columns']=('date','orderNum','IdSefaresh','userName','NameKala','id','sefareshType','row')
        #columns
        self.listBill.column('date',width=140,anchor=CENTER)
        self.listBill.column('IdSefaresh',width=210,anchor=E)
        self.listBill.column('orderNum',width=130,anchor=CENTER)
        self.listBill.column('userName',width=200,anchor=E)
        self.listBill.column('NameKala',width=185,anchor=E)
        self.listBill.column('id',width=130,anchor=CENTER)
        self.listBill.column('sefareshType',width=170,anchor=E)
        self.listBill.column('row',width=130,anchor=CENTER)
        #heading
        self.listBill.heading('date',text=' : تاریخ',anchor=E)
        self.listBill.heading('IdSefaresh',text=' : کد سفارش',anchor=E)
        self.listBill.heading('orderNum',text=' : تعداد سفارش',anchor=E)
        self.listBill.heading('userName',text=' : نام سفارش دهنده',anchor=E)
        self.listBill.heading('NameKala',text=' : نام کالا',anchor=E)
        self.listBill.heading('id',text=' : کد کالا',anchor=E)
        self.listBill.heading('sefareshType',text=' : نوع سفارش',anchor=E)
        self.listBill.heading('row',text=' : ردیف',anchor=E)
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading",font=('Lalezar', 16),
                            padding=[0, 5, 15, 5],background='#474A56',
                            foreground="white",bd=0,relief='raised')
        self.style.map("Treeview.Heading",
            background=[('active','#686A75')])
        self.style.configure("Treeview", highlightthickness=0, 
                            height=150,
                            bd=0, font=('AraFProgram', 16),
                            background="white",foreground="black",
                            rowheight = 35,fieldbackground="white")
        self.style.map("Treeview",
            background=[('selected', '#7A8BA7')],
            foreground=[('selected', 'white')])
        
        self.dateFrm_bill=Label(sodorbill_page,image=self.bgDateImg, height=45,width=320,bd=0,bg='white')
        self.time_label_bill = Label(self.dateFrm_bill)
        self.date_label_bill = Label(self.dateFrm_bill)
        self.b_openNav_bill=Button(sodorbill_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_bill,cursor='hand2')
        self.navFrm_bill=Frame(sodorbill_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm_bill=LabelFrame(self.navFrm_bill,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav_bill=Button(self.closeFrm_bill,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch_bill)
        self.b_home_page_bill=Button(self.navFrm_bill,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_main)
        self.b_addUser_bill=Button(self.navFrm_bill,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_user)
        self.b_addWare_bill=Button(self.navFrm_bill,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_product)
        self.b_WrStock_bill=Button(self.navFrm_bill,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_stock)
        self.b_Receipt_bill=Button(self.navFrm_bill,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_receipt)
        self.b_request_bill=Button(self.navFrm_bill,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_request)
        self.b_sabtSefareshPage_bill=Button(self.navFrm_bill,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_order)
        self.b_sabtExitKalaPage_bill=Button(self.navFrm_bill,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_exit)
        self.b_historyOrder_bill=Button(self.navFrm_bill,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.bill_to_history)
        self.b_bill_bill=Button(self.navFrm_bill,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_exit_bill=Button(self.navFrm_bill,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.dateFrm_bill.place(x=0,y=0)
        self.date_label_bill.place(x=15,y=4)
        self.time_label_bill.place(x=190,y=4)
        self.b_openNav_bill.place(x=1340,y=20)
        self.navFrm_bill.place(x=1400,y=0)
        self.closeFrm_bill.place(x=0,y=0)
        self.b_closeNav_bill.place(x=15,y=15)
        self.b_home_page_bill.place(x=0,y=50)
        self.b_addWare_bill.place(x=0,y=115)
        self.b_addUser_bill.place(x=0,y=180)
        self.b_WrStock_bill.place(x=0,y=245)
        self.b_Receipt_bill.place(x=0,y=310)
        self.b_request_bill.place(x=0,y=375)
        self.b_sabtSefareshPage_bill.place(x=0,y=440)
        self.b_sabtExitKalaPage_bill.place(x=0,y=505)
        self.b_historyOrder_bill.place(x=0,y=570)
        self.b_bill_bill.place(x=0,y=635)
        self.b_exit_bill.place(x=0,y=700)

        self.headerBillPage.place(x=590,y=0)
        self.l_SearchKala_bill.place(x=1000,y=100)
        self.e_SearchKala_bill.place(x=780,y=100)
        self.b_SearchKala_bill.place(x=620,y=95)
        self.b_blii.place(x=620,y=730)
        self.listBill.place(x=50,y=160)

        self.listBill.bind('<ButtonRelease-1>',self.select_record_bill)

    def update_time_bill(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label_bill.config(text=f"{self.current_time}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.date_label_bill.config(text=f"{self.current_date}",font=('AraFProgram',16),bg='#474A56',fg='white')
        self.dateFrm_bill.after(1000, self.update_time_bill)

    def switch_bill(self):
        if self.btnState is True:
            self.navFrm_bill.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_bill.place(x=1180, y=0)
            self.btnState = True
    
    def bill_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page.state('normal')        
        sodorbill_page.state('withdraw')
        self.btnState = True

    def bill_to_product(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        sodorbill_page.state('withdraw')
        self.btnState = True
        
    def bill_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_history()
        exit_page.state('normal')
        sodorbill_page.state('withdraw')
        self.btnState = False

    def bill_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page .state('normal')
        sodorbill_page.state('withdraw')
        self.btnState = True

    def bill_to_stock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        bill_page.state('withdraw')
        self.btnState = True
    
    def bill_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        sodorbill_page.state('withdraw')
        self.btnState = True

    def bill_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        sodorbill_page.state('withdraw')
        self.btnState = True

    def bill_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        sodorbill_page.state('withdraw')
        self.btnState = True

    def bill_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        sodorbill_page.state('withdraw')
        self.btnState = True

    def searchIdBill(self):
        con=sql.connect('mydb.db')
        cur=con.cursor()
        self.idBill=self.e_SearchKala_bill.get()
        self.count=0
        if self.idBill !='':
            for i in self.listKala.get_children():
                self.listKala.delete(i)
            row=cur.execute('SELECT * FROM orders WHERE idKala = "{}" or orderId = "{}" '.format(self.idBill,self.idBill))
            self.listBillInfo=list(row)
            for i in self.listBillInfo:
                self.count += 1
                if i[6] == 'وارد انبار شد':
                    self.listBill.insert(parent='',index='end',text='',
                                    values=(i[7],i[3],i[8],i[2],i[1],i[0],'ورود',str(self.count)))
                elif i[6] == 'تحویل داده شد':
                    self.listBill.insert(parent='',index='end',text='',
                                    values=(i[7],i[3],i[8],i[2],i[1],i[0],'خروج',str(self.count)))
            con.close()
        else:
            for item in self.listBill.get_children():
                self.listBill.delete(item)

    def select_record_bill(self ,event=None):
        self.selected_bill = self.listBill.focus()
        self.values_bill_list = self.listBill.item(self.selected_bill , "values")
        
    def sodorBill(self):
        con=sql.connect('mydb.db')
        cur=con.cursor()
        row=cur.execute('SELECT type,category FROM kala WHERE id = "{}"'.format(self.idBill))
        row=list(row)
        row2=cur.execute('SELECT stock FROM orders WHERE orderId = "{}"'.format(self.values_bill_list[2]))
        row2=list(row2)
        self.nameUserLbl_bill['text']=self.values_bill_list[3]
        self.dateLbl_bill['text']=self.values_bill_list[0]
        self.nameKalaLbl_bill['text']=self.values_bill_list[4]
        self.orderIdLbl_bill['text']=self.values_bill_list[2]
        self.orderTypeLbl_bill['text']=self.values_bill_list[6]
        self.kalaIdLbl_bill['text']=self.values_bill_list[5]
        self.groupKalaLbl_bill['text']=row[0][1]
        self.typeKalaLbl_bill['text']=row[0][0]
        self.kalaIdLbl_bill['text']=self.values_bill_list[5]
        self.stockKalaLbl_bill['text']=row2[0][0]
        self.orderNumLbl_bill['text']=self.values_bill_list[1]
        self.e_SearchKala_bill.delete(0,END)
        self.searchIdBill()
        bill_page.state('normal')
        sodorbill_page.state('withdraw')
        con.close()
#______________________________________________________________________________________________________________________________________________
#___________________________________________________________ sodor bill page __________________________________________________________________

    def bill_kala_page(self):
        bill_page.geometry('1400x800+250+100')
        bill_page.configure(bg='#F3F3F3')
    
        self.h_billPageImg = PhotoImage(file='image/headerBillPage.png')
        self.printBillBtnImg = PhotoImage(file='image/printBillBtnImg.png')
        self.backBillBtnImg = PhotoImage(file='image/backBillBtnImg.png')

        self.h_billPage = Label(bill_page,image=self.h_billPageImg)
        self.bgBill = LabelFrame(bill_page,height=600,width=1200,bg='#EFEEEE',bd=2,relief='solid')
        self.l_nameUser_bill = Label(bill_page,text=' : نام سفارش دهنده',font=('Lalezar',17),bg='#EFEEEE')
        self.nameUserLbl_bill = Label(bill_page,text='{: >25}'.format(''),font=('Lalezar',17),bg='#EFEEEE',width=15,fg='#4F4E4E')
        self.l_date_bill = Label(bill_page,text=' : تاریخ',font=('Lalezar',17),bg='#EFEEEE')
        self.dateLbl_bill = Label(bill_page,text='{: >11}'.format(''),font=('Lalezar',17),bg='#EFEEEE',width=10,fg='#4F4E4E')
        self.l_nameKala_bill = Label(bill_page,text=' : نام کالا',font=('Lalezar',17),bg='#EFEEEE')
        self.nameKalaLbl_bill = Label(bill_page,text='{: >20}'.format(''),font=('Lalezar',17),bg='#EFEEEE',width=17,fg='#4F4E4E')
        self.l_orderId_bill = Label(bill_page,text=' : کد سفارش',font=('Lalezar',17),bg='#EFEEEE')
        self.orderIdLbl_bill = Label(bill_page,text='{: >11}'.format(''),font=('Lalezar',17),bg='#EFEEEE',width=10,fg='#4F4E4E')
        self.l_groupKala_bill = Label(bill_page,text=' : گروه کالا',font=('Lalezar',17),bg='#EFEEEE')
        self.groupKalaLbl_bill = Label(bill_page,text='{: >20}'.format(''),font=('Lalezar',17),bg='#EFEEEE',width=17,fg='#4F4E4E')
        self.l_typeKala_bill = Label(bill_page,text=' : نوع کالا',font=('Lalezar',17),bg='#EFEEEE')
        self.typeKalaLbl_bill = Label(bill_page,text='{: >20}'.format(''),font=('Lalezar',17),bg='#EFEEEE',width=17,fg='#4F4E4E')
        self.l_orderType_bill = Label(bill_page,text=' : نوع سفارش',font=('Lalezar',17),bg='#EFEEEE')
        self.orderTypeLbl_bill = Label(bill_page,text='{: >4}'.format(''),font=('Lalezar',17),bg='#EFEEEE',fg='#4F4E4E')
        self.l_orderNum_bill = Label(bill_page,text=' : تعداد سفارش',font=('Lalezar',17),bg='#EFEEEE')
        self.orderNumLbl_bill = Label(bill_page,text='{: >5}'.format(''),font=('Lalezar',17),bg='#EFEEEE',fg='#4F4E4E')
        self.l_stockKala_bill = Label(bill_page,text=' : موجودی کالا',font=('Lalezar',17),bg='#EFEEEE')
        self.stockKalaLbl_bill = Label(bill_page,text='{: >5}'.format(''),font=('Lalezar',17),bg='#EFEEEE',fg='#4F4E4E')
        self.l_kalaId_bill = Label(bill_page,text=' : کد کالا',font=('Lalezar',17),bg='#EFEEEE')
        self.kalaIdLbl_bill = Label(bill_page,text='{: >20}'.format(''),font=('Lalezar',17),width=17,bg='#EFEEEE',fg='#4F4E4E')
        self.b_printBill =  Button(bill_page,bg='#F3F3F3',image=self.printBillBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2')
        self.b_back_bill =  Button(bill_page,bg='#F3F3F3',image=self.backBillBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2',command=self.backBill)
        
        self.h_billPage.place(x=590 , y=0)
        self.bgBill.place(x=100 , y=80)
        self.l_nameUser_bill.place(x=1100 , y=140)
        self.nameUserLbl_bill.place(x=900 , y=140)
        self.l_date_bill.place(x=310 , y=140)
        self.dateLbl_bill.place(x=180 , y=140)
        self.l_nameKala_bill.place(x=1060 , y=265)
        self.nameKalaLbl_bill.place(x=850 , y=265)
        self.l_orderId_bill.place(x=405 , y=265)
        self.orderIdLbl_bill.place(x=270 , y=265)
        self.l_groupKala_bill.place(x=1050 , y=465)
        self.groupKalaLbl_bill.place(x=840 , y=465)
        self.l_typeKala_bill.place(x=430 , y=465)
        self.typeKalaLbl_bill.place(x=220 , y=465)
        self.l_orderType_bill.place(x=1025 , y=365)
        self.orderTypeLbl_bill.place(x=950 , y=365)
        self.l_orderNum_bill.place(x=380 , y=565)
        self.orderNumLbl_bill.place(x=300 , y=565)
        self.l_stockKala_bill.place(x=1020 , y=565)
        self.stockKalaLbl_bill.place(x=950 , y=565)
        self.l_kalaId_bill.place(x=440 , y=365)
        self.kalaIdLbl_bill.place(x=230 , y=365)
        self.b_printBill.place(x=515 , y=720)
        self.b_back_bill.place(x=725 , y=720)

    def backBill(self):
        bill_page.state('withdraw')
        sodorbill_page.state('normal')

O = App(main_page)
main_page.mainloop()