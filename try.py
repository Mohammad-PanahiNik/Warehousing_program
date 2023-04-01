        self.dateFrm=Label(main_page,image=self.bgDateImg, height=40,width=320,bd=0,bg='white')
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
        self.b_bill=Button(self.navFrm,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit=Button(self.navFrm,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.dateFrm.place(x=0,y=0)
        self.date_label.place(x=15,y=6)
        self.time_label.place(x=190,y=6)
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
        self.b_bill.place(x=0,y=635)
        self.b_exit.place(x=0,y=700)



def update_time(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label.config(text=f"{self.current_time}",font=('Consolas',16),bg='#474A56',fg='white')
        self.date_label.config(text=f"{self.current_date}",font=('Consolas',16),bg='#474A56',fg='white')
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
