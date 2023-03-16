from tkinter import *
class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main()
    
    def main(self):
        self.fildsBgImg    = PhotoImage(file='image/fildsBg.png')
        self.fildImg1      = PhotoImage(file='image/fildImg1.png')
        self.fildImg2      = PhotoImage(file='image/imgSelectorBg.png')
        self.fildImg3      = PhotoImage(file='image/fildImg3.png')
        self.listKalaBgImg = PhotoImage(file='image/listSkalaBg.png')
        self.dropdownImg   = PhotoImage(file='image/dropdown.png')
        self.h_sabtKalaImg = PhotoImage(file='image/headerSabtKala.png')
        self.addKalaBtnImg = PhotoImage(file='image/addKalaBtn.png')

        self.geometry  ('1400x800+250+100')
        self.configure (bg='#F3F3F3')

        self.h_sabtKala    = Label(self,image=self.h_sabtKalaImg)
        self.l_productId   = Label(self,text=' : کد کالا',font=('Lalezar',17))
        self.e_productId   = Entry(self,font=('arial',16),bd=1,justify=RIGHT,width=16,relief='solid')
        self.l_productName = Label(self,text=' : نام کالا',font=('Lalezar',17))
        self.e_productName = Entry(self,font=('arial',16),bd=1,justify=RIGHT,width=16,relief='solid')
        self.l_productType = Label(self,text=' : نوع کالا',font=('Lalezar',17))
        self.e_productType = Entry(self,font=('arial',16),bd=1,justify=RIGHT,width=16,relief='solid')
        self.l_groupType   = Label(self,text=' : نام گروه کالا',font=('Lalezar',17))
        self.e_groupType   = Entry(self,font=('arial',16),bd=1,justify=RIGHT,width=16,relief='solid')
        self.l_description = Label(self,text=' : توضیحات',font=('Lalezar',17))
        self.e_description = Entry(self,font=('arial',16),bd=1,justify=RIGHT,width=25,relief='solid')
        self.l_purchase    = Label(self,text=' : نقطه خرید',font=('Lalezar',17))
        self.e_purchase    = Entry(self,font=('arial',16),bd=1,justify=RIGHT,width=16,relief='solid')
        self.l_imgSelector = Label(self,text='انتخاب تصویر',font=('Lalezar',17))
        self.imgSelectorBg = Label(self,bg='#F3F3F3',image=self.fildImg2)
        self.l_search      = Label(self,text=' : جستجو',font=('Lalezar',17))
        self.e_search      = Entry(self,font=('arial',16),bd=1,justify=RIGHT,width=16,relief='solid')
        self.b_dropdownbtn = Label(self,bg='#F3F3F3',image=self.dropdownImg)
        self.b_addKala = Button(self,bg='#F3F3F3',image=self.addKalaBtnImg,activebackground='#F3F3F3',bd=0,cursor='hand2')
        self.listKalaBg    = Label(self,bg='white',image=self.listKalaBgImg)

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
        self.e_productId.place   (x=1000 , y=105)
        self.l_productName.place (x=855 , y=100)
        self.e_productName.place (x=585 , y=100)
        self.l_productType.place (x=1240 , y=180)
        self.e_productType.place (x=1000 , y=180)
        self.l_groupType.place   (x=815 , y=180)
        self.e_groupType.place   (x=585 , y=180)
        self.l_description.place (x=830 , y=250)
        self.e_description.place (x=475 , y=250)
        self.l_purchase.place    (x=1215 , y=255)
        self.e_purchase.place    (x=1000 , y=255)
        self.l_imgSelector.place (x=210 , y=260)
        self.imgSelectorBg.place (x=200 , y=100)
        self.l_search.place      (x=340 , y=370)
        self.e_search.place      (x=130 , y=375)
        self.b_dropdownbtn.place (x=85 , y=370)
        self.b_addKala.place (x=1120 , y=340)
        self.listKalaBg.place    (x=85 , y=420)

        #____
        # self.productIdBg.place   (x=1000 , y=80)
        # self.productNameBg.place (x=380 , y=80)
        # self.productTypeBg.place (x=1000 , y=175)
        # self.groupTypeBg.place   (x=380 , y=175)
        # self.descriptionBg.place (x=890 , y=275)
        # self.purchaseBg.place    (x=380 , y=275)
        # self.searchBg.place      (x=130 , y=360)

        #_____bind_____
        self.e_productId.focus()
        self.e_productId.bind     ('<Return>',lambda event : self.e_productName.focus())
        self.e_productName.bind     ('<Return>',lambda event : self.e_productType.focus())
        self.e_productType.bind ('<Return>',lambda event : self.e_groupType.focus())
        self.e_groupType.bind    ('<Return>',lambda event : self.e_purchase.focus())
        self.e_purchase.bind     ('<Return>',lambda event : self.e_description.focus())
        self.e_description.bind     ('<Return>',lambda event : self.b_addKala.focus())
        # self.b_addKala.bind     ('<Return>',lambda event : )

        self.b_addKala.bind    ('<Enter>',lambda event : self.funcBtnHover(self.addKalaBtnImg,'image/addKalaBtnH.png'))
        self.b_addKala.bind    ('<Leave>',lambda event : self.funcBtnHover(self.addKalaBtnImg,'image/addKalaBtn.png'))


    def funcBtnHover(self,img,url):
        img['file'] = url


O=A()
O.mainloop()