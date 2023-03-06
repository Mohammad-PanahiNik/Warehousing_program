from tkinter import *

class A(Tk):
    def __init__(self) :
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('300x200+600+150')
        self.signinFrm = LabelFrame(self)
        self.e_Name=Entry (self.signinFrm , font=18)
        self.e_Last=Entry (self.signinFrm,font=18)
        self.e_PhoneNum=Entry (self.signinFrm,font=18)
        self.e_Email=Entry (self.signinFrm,font=18)
        self.b_register=Button (self.signinFrm,text='register',font=18)

        self.signinFrm.grid (row = 1 , column = 1)
        self.e_Name.grid (row = 1 , column = 1)
        self.e_Last.grid (row = 2 , column = 1)
        self.e_PhoneNum.grid (row = 3 , column = 1)
        self.e_Email.grid (row = 4 , column = 1)
        self.b_register.grid (row = 5 , column = 1)

        

O = A()
O.mainloop()