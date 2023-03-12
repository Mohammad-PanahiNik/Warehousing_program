from tkinter import *
# class A(Tk):
#     def __init__(self) :
#         Tk.__init__(self)
#         self.main()

#     def main(self):
#         self.geometry('1000x600+450+200')
#         self.title_bar =Frame(self, bg="blue", relief="raised", bd=1)
#         self.title_label =Label(self, text="Custom Title", bg="blue", fg="white")
#         self.title_bar.pack(expand=True, fill="x")
#         self.title_label.pack(side="left")
class TitleBar:
    def init(self, master):
        self.master = master
        self.master.title("Default Title")
        self.master.geometry("300x200")

        # Create a custom title bar
        self.title_bar = Frame(self.master, bg="blue", relief="raised", bd=1)
        self.title_bar.pack(expand=True, fill="x")

        # Create a label for the custom title bar
        self.title_label = Label(self.title_bar, text="Custom Title", bg="blue", fg="white")
        self.title_label.pack(side="left")

root = Tk()
app = TitleBar()
root.mainloop()
