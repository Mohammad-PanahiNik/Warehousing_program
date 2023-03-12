from tkinter import *

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('1400x800+250+100')

        #image
        self.addUserImg=PhotoImage(file='image/adduserImg.png')
        self.addWareImg=PhotoImage(file='image/addWareImg.png')
        self.WrStockImg=PhotoImage(file='image/WrStockImg.png')
        self.ReceiptImg=PhotoImage(file='image/ReceiptImg.png')
        self.requestImg=PhotoImage(file='image/requestImg.png')
        self.issuanceImg=PhotoImage(file='image/issuanceImg.png')
        self.exitImg=PhotoImage(file='image/exitImg.png')

        self.navFrm=LabelFrame(width='220px',bg='#777777',bd=0)
        self.b_addUser=Label(self.navFrm,image=self.addUserImg,bg='#777777',bd=0)
        self.b_addWare=Label(self.navFrm,image=self.addWareImg,bg='#777777',bd=0)
        self.b_WrStock=Label(self.navFrm,image=self.WrStockImg,bg='#777777',bd=0)
        self.b_Receipt=Label(self.navFrm,image=self.ReceiptImg,bg='#777777',bd=0)
        self.b_request=Label(self.navFrm,image=self.requestImg,bg='#777777',bd=0)
        self.b_issuance=Label(self.navFrm,image=self.issuanceImg,bg='#777777',bd=0)
        self.b_exit=Label(self.navFrm,image=self.exitImg,bg='#777777',bd=0)

        self.navFrm.pack(side=RIGHT,fill=BOTH)
        self.b_addUser.grid(row=1,column=1)
        self.b_WrStock.grid(row=2,column=1)
        self.b_Receipt.grid(row=3,column=1)
        self.b_request.grid(row=4,column=1)
        self.b_issuance.grid(row=5,column=1)
        self.b_exit.grid(row=6,column=1)

O = A()
O.mainloop()