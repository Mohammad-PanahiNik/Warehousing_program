self.update_time_product()



        self.dateFrm=Label(main_page,image=self.bgDateImg, height=40,width=320,bd=0,bg='white')
        self.time_label = Label(self.dateFrm)
        self.date_label = Label(self.dateFrm)

        
        self.dateFrm.place(x=0,y=0)
        self.date_label.place(x=15,y=6)
        self.time_label.place(x=190,y=6)


                  
    def update_time(self):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y/%m/%d")
        self.time_label.config(text=f"{self.current_time}",font=('Consolas',16),bg='#474A56',fg='white')
        self.date_label.config(text=f"{self.current_date}",font=('Consolas',16),bg='#474A56',fg='white')
        self.dateFrm.after(1000, self.update_time)