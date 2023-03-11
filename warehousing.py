from tkinter import *

class A(Tk):
    def __init__(self) :
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('1000x600+450+200')

        # Images
        self.signin_mainImg = PhotoImage(file='image/signInMainImg.png')
        self.profileImg_s = PhotoImage(file='image/profile-img.png')
        self.signInImg_filds = PhotoImage(file='image/signIn_filds.png')

        self.signinImgFrm  = LabelFrame(self,bd=0)
        self.img_signin = Label(self.signinImgFrm,image=self.signin_mainImg)
        self.signinFrm  = Label(self,bd=0 ,image=self.signInImg_filds)
        self.e_Name     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.e_Last     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.user_name     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)
        self.password     = Entry (self.signinFrm,font=('arial',18),bd=0,justify=RIGHT)

        self.signinImgFrm.grid  (row=1,column=1)
        self.img_signin.grid (row=1,column=1)
        self.signinFrm.grid  (row=1,column=2)
        self.e_Name.place(x=100,y=175)
        self.e_Last.place(x=100,y=264)
        self.user_name.place(x=100,y=353)
        self.password.place(x=100,y=442)

        # #bind
        self.e_Name.focus()
        self.e_Name.bind     ('<Return>',lambda event : self.e_Last.focus())
        self.e_Last.bind     ('<Return>',lambda event : self.user_name.focus())
        self.user_name.bind ('<Return>',lambda event : self.password.focus())
        # self.password.bind    ('<Return>',lambda event : self.password.focus())
        
    def f_register(self):
        pass
O = A()
O.mainloop()