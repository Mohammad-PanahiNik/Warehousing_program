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


    def pruduct_to_main(self):
        main_page .state('normal')
        product_page.state('withdraw')
        self.btnState = False

    def pruduct_to_user(self):
        user_page.state('normal')
        product_page.state('withdraw')
        self.btnState = False
    
    def pruduct_to_WrStock(self):
        stock_page.state('normal')
        product_page.state('withdraw')
        self.btnState = False
    
    def pruduct_to_Receipt(self):
        receipt_page.state('normal')
        product_page.state('withdraw')
        self.btnState = False

    def pruduct_to_request(self):
        request_page.state('normal')
        product_page.state('withdraw')
        self.btnState = False

    def pruduct_to_order(self):
        order_page.state('normal')
        product_page.state('withdraw')
        self.btnState = False

    def pruduct_to_exit(self):
        exit_page.state('normal')
        product_page.state('withdraw')
        self.btnState = Fal



        def switch_user_nav(self):
        if self.btnState is True:
            self.navFrm_user.place(x=1400, y=0)
            self.btnState = False
        else:
            self.navFrm_user.place(x=1180, y=0)
            self.btnState = True
    
    def user_to_main(self):
        main_page .state('normal')
        user_page.state('withdraw')
        self.btnState = False

    def user_to_kala(self):
        product_page.state('normal')
        user_page.state('withdraw')
        self.btnState = False
    
    def user_to_stock(self):
        stock_page.state('normal')
        user_page.state('withdraw')
        self.btnState = False
    
    def user_to_receipt(self):
        receipt_page.state('normal')
        user_page.state('withdraw')
        self.btnState = False

    def user_to_request(self):
        request_page.state('normal')
        user_page.state('withdraw')
        self.btnState = False

    def user_to_order(self):
        order_page.state('normal')
        user_page.state('withdraw')
        self.btnState = False

    def user_to_exit(self):
        exit_page.state('normal')
        user_page.state('withdraw')
        self.btnState = False



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
        self.b_issuance_user.place(x=0,y=570)
        self.b_exit_user.place(x=0,y=635)

