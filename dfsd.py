from tkinter import *
root = Tk()
loginpage = Toplevel()
registerpage = Toplevel()
#---------PagesBGs-Images---------------
img1 = PhotoImage(file = "pics/login.png")
img2 = PhotoImage(file = 'pics/mainpg.png')
img3 = PhotoImage(file = 'pics/register-page.png')
#---------Main-PageBtns-Images----------
img4 = PhotoImage(file = 'pics/fish.png')
img5 = PhotoImage(file = 'pics/darkhast.png')
img6 = PhotoImage(file = 'pics/mojodi.png')
img7 = PhotoImage(file = 'pics/resid.png')
img8 = PhotoImage(file = 'pics/sabtKala.png')
img9 = PhotoImage(file = 'pics/sabtKarbar.png')
#---------login-PageBtns-Images----------
img10 = PhotoImage(file = 'pics/login-btn.png')
class app:
    def __init__(self,event = None): 
        self.MainPage()
        self.loginPage()
        self.registerPage()
    def MainPage(self, event = None) :
        root.geometry('1200x720+150+20')
        root.state('withdraw')
        self.main_lbl = Label(root, width = 1184 , height = 709 , bg = 'white' , image = img2 )

        self.fishBtn = Button(root, width = 157 , height  = 62 , image = img4 , activebackground= '#EEEEEE', borderwidth = 0)
        self.fishBtn.place(x = 90 , y = 139)

        self.fishBtn.bind('<Enter>',lambda event : self.hoverBtn(img4,'pics/fish-hover.png'))
        self.fishBtn.bind('<Leave>',lambda event : self.hoverBtn(img4,'pics/fish.png'))
        
        self.residBtn = Button(root, width = 157 , height  = 62 , image = img7 ,activebackground= '#EEEEEE', borderwidth = 0)
        self.residBtn.place(x = 263 , y = 139)  

        self.residBtn.bind('<Enter>',lambda event : self.hoverBtn(img7,'pics/resid-hover.png'))
        self.residBtn.bind('<Leave>',lambda event : self.hoverBtn(img7,'pics/resid.png'))


        self.darkhastBtn = Button(root, width = 157 , height  = 62 , image = img5,activebackground= '#EEEEEE', borderwidth = 0)
        self.darkhastBtn.place(x = 436 , y = 139)

        self.darkhastBtn.bind('<Enter>',lambda event : self.hoverBtn(img5,'pics/darkhast-hover.png'))
        self.darkhastBtn.bind('<Leave>',lambda event : self.hoverBtn(img5,'pics/darkhast.png'))

        self.mojodiBtn = Button(root, width = 157 , height  = 62 , image = img6 , activebackground= '#EEEEEE', borderwidth = 0)
        self.mojodiBtn.place(x = 609 , y = 139)

        self.mojodiBtn.bind('<Enter>',lambda event : self.hoverBtn(img6,'pics/mojodi-hover.png'))
        self.mojodiBtn.bind('<Leave>',lambda event : self.hoverBtn(img6,'pics/mojodi.png'))

        self.sbtKarbarBtn = Button(root, width = 157 , height  = 63 , image = img9,activebackground= '#EEEEEE', borderwidth = 0)
        self.sbtKarbarBtn.place(x = 782 , y = 139)

        self.sbtKarbarBtn.bind('<Enter>',lambda event : self.hoverBtn(img9,'pics/sabtKarbar-hover.png'))
        self.sbtKarbarBtn.bind('<Leave>',lambda event : self.hoverBtn(img9,'pics/sabtKarbar.png'))

        self.sbtKalaBtn = Button(root, width = 157 , height  = 62 , image = img8,activebackground= '#EEEEEE', borderwidth = 0)
        self.sbtKalaBtn.place(x = 955 , y = 136)

        self.sbtKalaBtn.bind('<Enter>',lambda event : self.hoverBtn(img8,'pics/sabtKala-hover.png'))
        self.sbtKalaBtn.bind('<Leave>',lambda event : self.hoverBtn(img8,'pics/sabtKala.png'))

        self.main_lbl.place(x = 5 , y = 0)
    def loginPage(self, event = None):
        self.loginpage = loginpage
        self.loginpage.state('normal')
        self.loginpage.geometry('852x588+250+20')
        self.login_main_lbl = Label(self.loginpage , width = 852 , height = 588 , bg = 'white')
        self.login_main_lbl.place(x = 0 , y = 0)
        self.login_lbl = Label(self.loginpage , width = 815 , height = 550 , bg = 'white' , image = img1 )
        self.login_lbl.place(x = 15, y = 15)

        self.login_btn = Button(self.loginpage , bg = 'white' , width = 211 , height = 65 , image = img10 ,activebackground= '#ffffff', borderwidth = 0)
        self.login_btn.place( x = 528 , y = 376)

        self.login_btn.bind('<Enter>',lambda event : self.hoverBtn(img10,'pics/login-btn-hover.png'))
        self.login_btn.bind('<Leave>',lambda event : self.hoverBtn(img10,'pics/login-btn.png'))




    def registerPage(self, event = None):
        self.registerpage = registerpage
        self.registerpage.state('withdraw')
        self.registerpage.geometry('852x588+250+20')
        self.register_lbl = Label(self.registerpage , width = 815 , height = 550 , bg = 'white' , image = img3 )
        
        self.register_lbl.place(x = 15, y = 15)

    def hoverBtn(self,img,url):
        img['file'] = url


app = app(root)
root.mainloop()