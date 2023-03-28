from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import sqlite3 as sql
from tkinter import messagebox
import uuid
from datetime import datetime
from tkcalendar import Calendar, DateEntry

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
history_page = Toplevel()

class App:
    def __init__(self,event=None):
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
        self.request_product_page()
        self.order_kala_page()
        self.exit_kala_page()
        self.order_history_page()
        self.data_to_list_history()
        self.update_time()

    def main(self):
        main_page.geometry('1400x800+250+100')
        main_page.configure(bg='white')
        main_page.title('menu')
        main_page.state('normal')
        
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
        
        self.dateFrm=Label(main_page,image=self.bgDateImg, height=90,width=220,bd=0,bg='white')
        self.time_label = Label(self.dateFrm)
        self.date_label = Label(self.dateFrm)
        self.b_openNav=Button(main_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch,cursor='hand2')
        self.navFrm=Frame(main_page,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm=LabelFrame(self.navFrm,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav=Button(self.closeFrm,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch)
        self.b_home_page=Button(self.navFrm,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_addUser=Button(self.navFrm,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.open_addUser_page)
        self.b_addWare=Button(self.navFrm,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.open_addKala_page)
        self.b_WrStock=Button(self.navFrm,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.open_stock_page)
        self.b_Receipt=Button(self.navFrm,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.open_receipt_page)
        self.b_request=Button(self.navFrm,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.open_request_page)
        self.b_sabtSefareshPage=Button(self.navFrm,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.open_sabtSefaresh_page)
        self.b_sabtExitKalaPage=Button(self.navFrm,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.open_sabtExit_page)
        self.b_historyOrder=Button(self.navFrm,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.open_history_page)
        self.b_billing=Button(self.navFrm,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit=Button(self.navFrm,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.dateFrm.place(x=0,y=0)
        self.date_label.place(x=45,y=10)
        self.time_label.place(x=55,y=50)
        self.b_openNav.place(x=1340,y=20)
        self.navFrm.place(x=1400,y=0)
        self.closeFrm.place(x=0,y=0)
        self.b_closeNav.place(x=15,y=15)
        self.b_home_page.place(x=0,y=50)
        self.b_addWare.place(x=0,y=115)
        self.b_addUser.place(x=0,y=180)
        self.b_WrStock.place(x=0,y=245)
        self.b_Receipt.place(x=0,y=310)
        self.b_request.place(x=0,y=375)
        self.b_sabtSefareshPage.place(x=0,y=440)
        self.b_sabtExitKalaPage.place(x=0,y=505)
        self.b_historyOrder.place(x=0,y=570)
        self.b_billing.place(x=0,y=635)
        self.b_exit.place(x=0,y=700)

            
    def update_time(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label.config(text=f"{self.current_time}",font=('Consolas',18),bg='#6050AB',fg='white')
        self.date_label.config(text=f"{self.current_date}",font=('Consolas',18),bg='#6050AB',fg='white')
        self.dateFrm.after(1000, self.update_time)

    def switch(self):
        if self.btnState is True:
            self.navFrm.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm.place(x=1180, y=0)
            self.btnState = True

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

    # def open_billing_page(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_kala()
    #     billing_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

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

        self.signinImgFrm.grid (row=1,column=1)
        self.img_signin.grid (row=1,column=1)
        self.signinFrm.grid (row=1,column=2)
        self.signIn_logo.place(x=175,y=10)
        self.e_Name.place(x=100,y=175)
        self.e_Last.place(x=100,y=264)
        self.e_user_name.place(x=100,y=353)
        self.e_password.place(x=100,y=442)
        self.b_signin_btn.place(x=150,y=495)
        self.l_description.place(x=80,y=560)

        #bind
        self.e_Name.focus()
        self.e_Name.bind ('<Return>',lambda event : self.e_Last.focus())
        self.e_Last.bind ('<Return>',lambda event : self.e_user_name.focus())
        self.e_user_name.bind ('<Return>',lambda event : self.e_password.focus())
        self.e_password.bind ('<Return>',lambda event : self.b_signin_btn.focus())
        self.b_signin_btn.bind ('<Enter>',lambda event : self.funcBtnHover(self.signInBtn,'image/registerBtnH.png'))
        self.b_signin_btn.bind ('<Leave>',lambda event : self.funcBtnHover(self.signInBtn,'image/registerBtn.png'))

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
        self.searchBtnImg_kala = PhotoImage(file='image/searchBtnImg.png')
        self.h_sabtKalaImg = PhotoImage(file='image/headerSabtKala.png')
        self.addKalaBtnImg = PhotoImage(file='image/addKalaBtn.png')
        self.deleteBtnImg_kala = PhotoImage(file='image/deleteBtnImg.png')
        self.editBtnImg_kala = PhotoImage(file='image/editBtnImg.png')
        self.sabtTaghirKalaBtn = PhotoImage(file='image/sabtEdit.png')

        product_page.geometry ('1400x800+250+100')
        product_page.state ('withdraw')
        product_page.configure (bg='#F3F3F3')

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
        self.b_mainpage_product=Button(self.navFrm_product,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_main)
        self.b_addKala_product=Button(self.navFrm_product,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_addUser_product=Button(self.navFrm_product,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_user)
        self.b_WrStock_product=Button(self.navFrm_product,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_WrStock)
        self.b_Receipt_product=Button(self.navFrm_product,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_Receipt)
        self.b_request_product=Button(self.navFrm_product,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_request)
        self.b_order_product=Button(self.navFrm_product,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_order)
        self.b_exitKala_product=Button(self.navFrm_product,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_exit)
        self.b_history_product=Button(self.navFrm_product,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.pruduct_to_history)
        self.b_issuance_product=Button(self.navFrm_product,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_product=Button(self.navFrm_product,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

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

        #_______ hover button ________
        # self.e_search_kala.insert(0,'جستجو کد کالا  ')
        # self.e_search_kala.bind('<Button-1>',lambda event :self.e_search_kala.delete(0,END))
        # self.b_search_kala.bind('<Enter>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImgH.png'))
        # self.b_search_kala.bind('<Leave>',lambda event : self.funcBtnHover(self.searchBtnImg,'image/searchBtnImg.png'))
        # self.b_delete_kala.bind('<Enter>',lambda event : self.funcBtnHover(self.deleteBtnImg,'image/deleteBtnImgH.png'))
        # self.b_delete_kala.bind('<Leave>',lambda event : self.funcBtnHover(self.deleteBtnImg,'image/deleteBtnImg.png'))
        # self.b_edit_kala.bind('<Enter>',lambda event : self.funcBtnHover(self.editBtnImg,'image/editBtnImgH.png'))
        # self.b_edit_kala.bind('<Leave>',lambda event : self.funcBtnHover(self.editBtnImg,'image/editBtnImg.png'))
    
    def pruduct_to_main(self):
        self.navFrm.place(x=1180, y=0)
        main_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True
        
    def pruduct_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        main_page.state('withdraw')
        self.btnState = True

    # def product_to_billing(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     billing_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

    def pruduct_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True
    
    def pruduct_to_WrStock(self):
        self.navFrm_stock.place(x=1180, y=0)
        self.data_to_list_stock()
        stock_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True
    
    def pruduct_to_Receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def pruduct_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def pruduct_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        product_page.state('withdraw')
        self.btnState = True

    def pruduct_to_exit(self):
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
        self.listUser.column('type',width=200,anchor=E)
        self.listUser.column('phoneNum',width=200,anchor=E)
        self.listUser.column('nationalCode',width=200,anchor=E)
        self.listUser.column('last',width=200,anchor=E)
        self.listUser.column('name',width=200,anchor=E)
        self.listUser.column('personnelId',width=150,anchor=E)
        self.listUser.column('row',width=100,anchor=E)
        #heading
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
        self.b_mainPage_user=Button(self.navFrm_user,image=self.homePageBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_main)
        self.b_addKala_user=Button(self.navFrm_user,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_kala)
        self.b_addUser_user=Button(self.navFrm_user,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2',state='disabled')
        self.b_WrStock_user=Button(self.navFrm_user,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_stock)
        self.b_Receipt_user=Button(self.navFrm_user,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_receipt)
        self.b_request_user=Button(self.navFrm_user,image=self.requestImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_request)
        self.b_order_user=Button(self.navFrm_user,image=self.sabtSefareshBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_order)
        self.b_exitKala_user=Button(self.navFrm_user,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_exit)
        self.b_history_user=Button(self.navFrm_user,image=self.historyBtnImg,bg='#777777',bd=0,cursor='hand2',command=self.user_to_history)
        self.b_issuance_user=Button(self.navFrm_user,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_user=Button(self.navFrm_user,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

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
        main_page.state('withdraw')
        self.btnState = True

    # def open_billing_page(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     billing_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

    
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
        self.b_issuance_stock=Button(self.navFrm_stock,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_stock=Button(self.navFrm_stock,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')
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
        self.btnState = False

    def stock_to_kala(self):
        self.navFrm_product.place(x=1180, y=0)
        self.data_to_list_kala()
        product_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = False
    
    def stock_to_user(self):
        self.navFrm_user.place(x=1180, y=0)
        self.data_to_list_user()
        user_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = False
    
    def stock_to_history(self):
        self.navFrm_history.place(x=1180, y=0)
        self.data_to_list_history()
        history_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = False

    # def product_to_billing(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     billing_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

    def stock_to_receipt(self):
        self.navFrm_receipt.place(x=1180, y=0)
        receipt_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = False

    def stock_to_request(self):
        self.navFrm_request.place(x=1180, y=0)
        self.data_to_list_request()
        request_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = False

    def stock_to_order(self):
        self.navFrm_order.place(x=1180, y=0)
        self.data_to_list_order()
        order_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = False

    def stock_to_exit(self):
        self.navFrm_exit.place(x=1180, y=0)
        self.data_to_list_exit()
        exit_page.state('normal')
        stock_page.state('withdraw')
        self.btnState = False


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
        self.l_imgSelector_receipt = Label(receipt_page,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg_receipt = Label(receipt_page,bg='#F3F3F3',image=self.kalaImg,cursor='hand2',width=150,height=150)
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
        self.b_issuance_receipt=Button(self.navFrm_receipt,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_receipt=Button(self.navFrm_receipt,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')


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
        self.e_searchUser_receipt.place(x=475,y=90)
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
        self.l_imgSelector_receipt.place(x=110,y=400)
        self.imgSelectorBg_receipt.place(x=85,y=250)
        self.kalaNumFrm_receipt.place(x=520,y=460)
        self.kalaNum_receipt.place(x=700,y=10)
        self.e_kalaNum_receipt.place(x=490,y=10)
        self.b_addKalaNum_receipt.place(x=15,y=5)
        self.l_date_receipt.place(x=350,y=10)
        self.date_receipt.place(x=190,y=10)
        self.listReceipt.place(x=85,y=545)
    
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

    # def receipt_to_billing(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     billing_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True
    
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
                self.row=self.cur.execute('SELECT * FROM kala WHERE id="{}"'.format(self.idKala))
                self.kalaInfo=list(self.row)
                self.nameKalaLbl_receipt['text']=self.kalaInfo[0][1]
                self.kalaTypeLbl_receipt['text']=self.kalaInfo[0][2]
                self.kalaIdLbl_receipt['text']=self.kalaInfo[0][0]
                self.groupKalaLbl_receipt['text']=self.kalaInfo[0][3]
                self.stockLbl_receipt['text']=self.kalaInfo[0][7]
                self.purchaseLbl_receipt['text']=self.kalaInfo[0][4]

    def funcAddNum(self,event=None):
        self.entryNum=self.e_kalaNum_receipt.get()
        self.selected_date_receipt = self.date_receipt.get_date()
        self.kalaNumber=int(self.entryNum)+int(self.kalaInfo[0][7])
        self.randomId_receipt=str(uuid.uuid4())
        self.randomId_receipt=self.randomId_receipt[:8]
        self.data=(self.kalaInfo[0][0],self.kalaInfo[0][1],self.fullname_r,self.entryNum,self.kalaInfo[0][7],
        self.kalaInfo[0][4],'وارد انبار شد',self.selected_date_receipt,self.randomId_receipt)
        self.cur.execute('''CREATE TABLE IF NOT EXISTS orders (idKala TEXT  NOT NULL ,nameKala TEXT NOT NULL ,nameUser TEXT NOT NULL
        ,numOrder NOT NULL,stock,purchase TEXT NOT NULL,condition TEXT,date INTEGER NOT NULL,orderId)''')
        self.cur.execute('INSERT INTO orders(idKala,nameKala,nameUser,numOrder,stock,purchase,condition,date,orderId) VALUES(?,?,?,?,?,?,?,?,?)',self.data)
        self.cur.execute(''' UPDATE kala SET stock = "{}" WHERE id="{}" '''.format(self.kalaNumber,self.idKala))
        self.cur.execute(''' UPDATE orders SET stock = "{}" WHERE idKala="{}" '''.format(self.kalaNumber,self.idKala))
        self.con.commit()
        self.num_of_rows = len(self.listReceipt.get_children())
        self.listReceipt.insert(parent='',index='end',text='',
                        values=(self.selected_date_receipt,self.entryNum,self.randomId_receipt,self.kalaInfo[0][0],self.kalaInfo[0][1],self.fullname_r,self.num_of_rows+1))
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
        self.purchaseLbl_receipt['text']=''
        self.stockLbl_receipt['text']=''
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
        
        self.b_openNav_request=Button(request_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_request_nav,cursor='hand2')
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
        self.b_history_request=Button(self.navFrm_request,image=self.exitKalaBtnMenuImg,bg='#777777',bd=0,cursor='hand2',command=self.request_to_history)
        self.b_issuance_request=Button(self.navFrm_request,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_request=Button(self.navFrm_request,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')


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

    # def request_to_billing(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     request_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

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
        order_page.geometry('1400x800+250+100')
        order_page.configure(bg='white')
        order_page.title('menu')
        order_page.state('withdraw')

        self.headerOrderImg = PhotoImage(file='image/headerRequestImg.png')
        self.sabtOrderBtnImg = PhotoImage(file='image/sabtOrder.png')
        self.searchBtnImg_order = PhotoImage(file='image/searchBtnImg.png')
        self.order_imgSelectorPic = PhotoImage(file='image/imgSelectorBg.png')
        self.order_baresiImg = PhotoImage(file='image/baresiBtnImg.png')
        self.tickImgBtn = PhotoImage(file='image/tickImgBtn.png')

        self.l_headerOrderPage = Label(order_page,image=self.headerOrderImg)
        self.attention_idUser = Label(order_page,text=' . لطفا کد کاربر موردنطر خود را وارد کنید',font=('Lalezar',17),bg='white')
        self.e_idUser_order = Entry(order_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchUserBtnOrder = Button(order_page,image=self.order_baresiImg,bd=0,activebackground='white',command=self.search_idUser_order)
        self.e_idKala_order = Entry(order_page,font=('AraFProgram', 16),bd=1,justify=RIGHT,width=18,relief='solid')
        self.b_searchBtnOrder = Button(order_page,image=self.searchBtnImg_order,bd=0,activebackground='white',command=self.search_idKala_order)
        self.userInfo_order_frm = LabelFrame(order_page,width=510,height=135,bg='#F2F2F2',bd=5,relief=SOLID)
        self.l_nameUser_order = Label(self.userInfo_order_frm,text=' : نام',font=('Lalezar',17),bg='#F2F2F2')
        self.nameUserLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_lastUser_order = Label(self.userInfo_order_frm,text=' : نام خانوادگی',font=('Lalezar',17),bg='#F2F2F2')
        self.lastUserLbl_order =Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_nationalCode_order = Label(self.userInfo_order_frm,text=' : کد ملی',font=('Lalezar',17),bg='#F2F2F2')
        self.nationalCodeLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=15,fg='#4F4E4E')
        self.l_userId_order = Label(self.userInfo_order_frm,text=' : کد کاربری',font=('Lalezar',17),bg='#F2F2F2')
        self.userIdLbl_order = Label(self.userInfo_order_frm,text='{: ^20}'.format(''),font=('Lalezar',17),bg='#F2F2F2',width=8,fg='#4F4E4E')
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
        
        self.b_openNav_order=Button(order_page,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch_order_nav,cursor='hand2')
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
        self.b_issuance_order=Button(self.navFrm_order,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_order=Button(self.navFrm_order,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

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
        self.e_idUser_order.place(x=835,y=90)
        self.b_searchUserBtnOrder.place(x=670,y=85)
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
        self.userIdLbl_order.place(x=260,y=70)
        self.l_nationalCode_order.place(x=190,y=70)
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
        self.l_imgSelector_order.place(x=65,y=175)
        self.imgSelectorBg_order.place(x=50,y=25)
        self.listOrder.place(x=60,y=420)

        #________bind___________
        self.listOrder.bind('<ButtonRelease-1>',self.select_record_order)
        self.tickBtnOrder.bind('<Button-1>',self.ready_to_delivery)
    
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

    # def order_to_billing(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     order_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

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
                    values=(self.orderDate,i[4],i[3],i[8],i[2],i[1],i[0],self.count+1))
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
        exit_page.geometry('1400x800+250+100')
        exit_page.configure(bg='white')
        exit_page.title('menu')
        exit_page.state('withdraw')

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
        self.b_issuance_exit=Button(self.navFrm_exit,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit_exit=Button(self.navFrm_exit,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

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

    # def exit_to_billing(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     exit_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

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
                    values=(i[7],i[4],i[3],i[8],i[2],i[1],i[0],self.numlist_exit+1))

    def select_record_exit(self ,event=None):
        self.selected_exit = self.listExit.focus()
        self.values_exit_list = self.listExit.item(self.selected_exit , "values")

    def sabt_exit_kala(self,event=None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        exitIdCheck=self.values_exit_list[3]
        self.new_stock_exit=int(self.values_exit_list[1])-int(self.values_exit_list[2])
        self.cur.execute(''' UPDATE orders SET condition = ?   WHERE orderId= ? ''',("تحویل داده شد",exitIdCheck))
        self.cur.execute(''' UPDATE orders SET stock = ?  WHERE idKala= ? ''',(self.new_stock_exit,self.values_exit_list[6]))
        self.cur.execute(''' UPDATE kala SET stock = ?  WHERE id= ? ''',(self.new_stock_exit,self.values_exit_list[6]))
        self.con.commit()
        self.data_to_list_exit()
    
    #________________________________________________________________________________________________________________________________________
    #__________________________________________________________ order history page __________________________________________________________

    def order_history_page(self):
        history_page.geometry('1400x800+250+100')
        history_page.configure(bg='white')
        history_page.title('menu')
        history_page.state('normal')

        self.h_orderHistoryImg = PhotoImage(file='image/headerHistory.png')

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
    
        self.h_orderHistory.place(x=590,y=0)
        self.listHistory.place(x=50,y=150)
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
        self.b_issuance_history=Button(self.navFrm_history,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
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

    # def history_to_billing(self):
    #     self.navFrm_billing.place(x=1180, y=0)
    #     self.data_to_list_billing()
    #     history_page .state('normal')
    #     main_page.state('withdraw')
    #     self.btnState = True

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
        self.count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        self.result = self.cur.fetchone()
        if self.result != None:
            row=self.cur.execute('SELECT * FROM orders')
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

O = App(main_page)
main_page.mainloop()