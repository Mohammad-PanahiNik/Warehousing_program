from tkinter import *

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('400x510+750+300')

        #image
        self.logFrmImg = PhotoImage(file='image/loginFrm.png')
        self.logoImg = PhotoImage(file='image/logoImg.png')
        self.logBtnImg = PhotoImage(file='image/loginBtn.png')
        self.eyeImg = PhotoImage(file='image/openEye.png')

        self.logFrmBg=Label(self,image=self.logFrmImg)
        self.logoImgLog=Label(self.logFrmBg,image=self.logoImg,bg='white')
        self.e_userNameLog=Entry(self.logFrmBg,font=('arial',18),bd=0,justify=RIGHT)
        self.e_passwordLog=Entry(self.logFrmBg,font=('arial',18),bd=0,justify=RIGHT)
        self.showBtn=Button(self.logFrmBg,image=self.eyeImg,bd=0,activebackground='white')
        self.b_enterBtn=Button(self.logFrmBg,image=self.logBtnImg ,activebackground='white',bd=0)

        self.logFrmBg.grid(row=1,column=1)
        self.logoImgLog.place(x=135,y=10)
        self.e_userNameLog.place(x=80,y=215)
        self.e_passwordLog.place(x=80,y=316)
        self.showBtn.place(x=20,y=310)
        self.b_enterBtn.place(x=120,y=400)

        self.e_userNameLog.focus()
        self.e_userNameLog.bind('<Return>',lambda event : self.e_passwordLog.focus())
        self.e_passwordLog.bind('<Return>',lambda event : self.b_enterBtn.focus())
    
O = A()
O.mainloop()
