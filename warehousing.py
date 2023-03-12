from tkinter import *

class A(Tk):
    def __init__(self) :
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('1000x600+450+200')

        # Images
        self.signin_mainImg = PhotoImage(file='image/signInMainImg.png')
        self.logoImg = PhotoImage(file='image/logoImg.png')
        self.signInImg_filds = PhotoImage(file='image/signIn_filds.png')
        self.signInBtn = PhotoImage(file='image/registerBtn.png')

        self.signinImgFrm  = LabelFrame(self,bd=0)
        self.img_signin = Label(self.signinImgFrm,image=self.signin_mainImg)
        self.signinFrm  = Label(self,bd=0 ,image=self.signInImg_filds)
        self.signIn_logo  = Label(self.signinFrm,bd=0 ,image=self.logoImg,bg='white')
        self.e_Name     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.e_Last     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.e_user_name     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.e_password     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.b_signin_btn     = Button (self.signinFrm,image=self.signInBtn,bd=0)
        self.l_description = Label(self.signinFrm,text='                           ! لطفا برای ورود به برنامه ابتدا ثبت نام کنید *   ', bg='white',font=('Lalezar',14),fg='#5D5555')

        self.signinImgFrm.grid  (row=1,column=1)
        self.img_signin.grid (row=1,column=1)
        self.signinFrm.grid  (row=1,column=2)
        self.signIn_logo.place(x=175,y=10)
        self.e_Name.place(x=100,y=175)
        self.e_Last.place(x=100,y=264)
        self.e_user_name.place(x=100,y=353)
        self.e_password.place(x=100,y=442)
        self.b_signin_btn.place(x=150,y=495)
        self.l_description.place(x=0,y=560)

        #bind
        self.e_Name.focus()
        self.e_Name.bind     ('<Return>',lambda event : self.e_Last.focus())
        self.e_Last.bind     ('<Return>',lambda event : self.e_user_name.focus())
        self.e_user_name.bind ('<Return>',lambda event : self.e_password.focus())
        self.e_password.bind    ('<Return>',lambda event : self.b_signin_btn.focus())
        self.b_signin_btn.bind    ('<Enter>',lambda event : self.funcBtnHover(self.signInBtn,'image/registerBtnH.png'))
        self.b_signin_btn.bind    ('<Leave>',lambda event : self.funcBtnHover(self.signInBtn,'image/registerBtn.png'))
        # self.b_signin_btn.bind    ('<Return>',lambda event : self.signin_btn.focus())

    def funcBtnHover(self,img,url):
        img['file'] = url

    def f_register(self):
        pass
O = A()
O.mainloop()