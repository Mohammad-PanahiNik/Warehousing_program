from tkinter import *
from tkinter import ttk

class A(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.main()

    def main(self):
        self.geometry('500x500')
        self.my_tree= ttk.Treeview(self)

        self.my_tree['columns']=('name','id','favorite')

        #columns
        self.my_tree.column('#0',width=120,minwidth=25)
        self.my_tree.column('name',width=120,anchor=W)
        self.my_tree.column('id',width=80,anchor=CENTER)
        self.my_tree.column('favorite',width=120,anchor=W)

        #heading
        self.my_tree.heading('#0',text='label',anchor=W)
        self.my_tree.heading('name',text='name',anchor=W)
        self.my_tree.heading('id',text='id',anchor=CENTER)
        self.my_tree.heading('favorite',text='fav',anchor=W)

        #add data to list
        self.my_tree.insert(parent='',index='end',iid=0,text='',values=('ali','5','agha ali'))
        self.my_tree.insert(parent='',index='end',iid=1,text='',values=('ali','5','agha ali'))
        self.my_tree.insert(parent='',index='end',iid=2,text='',values=('ali','5','agha ali'))
        self.my_tree.insert(parent='',index='end',iid=3,text='',values=('ali','5','agha ali'))

        self.my_tree.place(x=0,y=0)

O=A()
O.mainloop()