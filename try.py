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
        self.btnState = False
