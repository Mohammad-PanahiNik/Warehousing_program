from tkinter import *

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.btnState = False
        self.main()

    def main(self):
        self.geometry('1400x800+250+100')
        self.configure(bg='white')
        
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

        self.b_openNav=Button(self,image=self.openBtnImg,bg='white',activebackground='white',bd=0,command=self.switch,cursor='hand2')
        self.navFrm=Frame(self,height=800,width=220,bg='#777777',bd=0)
        self.closeFrm=LabelFrame(self.navFrm,width=220,bg='#2E2E2E',bd=0,height=50)
        self.b_closeNav=Button(self.closeFrm,image=self.closeBtnImg,bd=0,bg='#2E2E2E',activebackground='#2E2E2E',cursor='hand2',command=self.switch)
        self.b_addUser=Label(self.navFrm,image=self.addUserImg,bg='#777777',bd=0,cursor='hand2')
        self.b_addWare=Label(self.navFrm,image=self.addWareImg,bg='#777777',bd=0,cursor='hand2')
        self.b_WrStock=Label(self.navFrm,image=self.WrStockImg,bg='#777777',bd=0,cursor='hand2')
        self.b_Receipt=Label(self.navFrm,image=self.ReceiptImg,bg='#777777',bd=0,cursor='hand2')
        self.b_request=Label(self.navFrm,image=self.requestImg,bg='#777777',bd=0,cursor='hand2')
        self.b_issuance=Label(self.navFrm,image=self.issuanceImg,bg='#777777',bd=0,cursor='hand2')
        self.b_exit=Label(self.navFrm,image=self.exitImg,bg='#777777',bd=0,cursor='hand2')

        self.b_openNav.place(x=1340,y=20)
        self.navFrm.place(x=1400,y=0)
        self.closeFrm.place(x=0,y=0)
        self.b_closeNav.place(x=15,y=15)
        self.b_addUser.place(x=0,y=50)
        self.b_WrStock.place(x=0,y=115)
        self.b_Receipt.place(x=0,y=180)
        self.b_request.place(x=0,y=245)
        self.b_issuance.place(x=0,y=310)
        self.b_exit.place(x=0,y=375)

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

O = A()
O.mainloop()