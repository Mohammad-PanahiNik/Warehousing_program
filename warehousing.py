from tkinter import *



class A(Tk):
    def __init__(self) :
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('300x200+600+150')
        self.signinFrm = LabelFrame(self,bd=0)
        self.e_Name=Entry (self.signinFrm , font=('arial',16))
        self.e_Last=Entry (self.signinFrm,font=('arial',16))
        self.e_PhoneNum=Entry (self.signinFrm,font=('arial',16))
        self.e_Email=Entry (self.signinFrm,font=('arial',16))
        self.b_register=Button (self.signinFrm,text='register',font=('arial',16),width=10,height=1)

        self.signinFrm.grid (row = 1 , column = 1)
        self.e_Name.grid (row = 1 , column = 1, padx=25 , pady=3)
        self.e_Last.grid (row = 2 , column = 1, padx=25 , pady=3)
        self.e_PhoneNum.grid (row = 3 , column = 1, padx=25 , pady=3)
        self.e_Email.grid (row = 4 , column = 1, padx=25 , pady=3)
        self.b_register.grid (row = 5 , column = 1, padx=25 , pady=10)

        #bind
        self.e_Name.focus()
        self.e_Name.bind('<Return>',lambda event : self.e_Last.focus())
        self.e_Last.bind('<Return>',lambda event : self.e_PhoneNum.focus())
        self.e_PhoneNum.bind('<Return>',lambda event : self.e_Email.focus())
        self.e_Email.bind('<Return>',lambda event : self.b_register.focus())
        self.b_register.bind('<Return>',lambda event : self.f_register())
        
    def f_register(self):
        pass
O = A()
O.mainloop()