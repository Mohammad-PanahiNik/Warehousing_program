from tkinter import *

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('400x510+750+300')
        self.config(bg='white')

        #image
        self.logFrmImg = PhotoImage(file='image/loginFrm.png')
        self.logoImg = PhotoImage(file='image/logoImg.png')
        self.logBtnImg = PhotoImage(file='image/loginBtn.png')
        self.eyeImg = PhotoImage(file='image/openEye.png')

        # self.logFrmBg=Label(self,image=self.logFrmImg,bg='white')
        self.logoImgLog=Label(self,image=self.logoImg,bg='white')
        self.l_userNameLog = Label(self,text=' : نام کاربری',font=('Lalezar',17),bg='white')
        self.e_userNameLog=Entry(self,font=('arial',18),justify=RIGHT,bd=2,relief='solid')
        self.l_passwordLog = Label(self,text=' : رمز عبور',font=('Lalezar',17),bg='white')
        self.e_passwordLog=Entry(self,font=('arial',18),justify=RIGHT,bd=2,relief='solid',show='*')
        self.showBtn=Button(self,image=self.eyeImg,bd=0,activebackground='white')
        self.b_enterBtn=Button(self,image=self.logBtnImg ,activebackground='white',bd=0)

        # self.logFrmBg.grid(row=1,column=1)
        self.logoImgLog.place(x=135,y=10)
        self.l_userNameLog.place(x=250,y=175)
        self.e_userNameLog.place(x=80,y=215)
        self.l_passwordLog.place(x=270,y=275)
        self.e_passwordLog.place(x=80,y=316)
        self.showBtn.place(x=20,y=310)
        self.b_enterBtn.place(x=120,y=400)

        self.e_userNameLog.focus()
        self.e_userNameLog.bind('<Return>',lambda event : self.e_passwordLog.focus())
        self.e_passwordLog.bind('<Return>',lambda event : self.b_enterBtn.focus())
        self.showBtn.bind('<Button-1>',self.funcShow)
        

    def funcShow(self,event=None):
        if self.e_passwordLog['show']=='*':
            self.e_passwordLog['show']=''
            self.eyeImg['file']='image/closeEye.png'
        else:
            self.e_passwordLog['show']='*'
            self.eyeImg['file']='image/openEye.png'


O = A()
O.mainloop()
