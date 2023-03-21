import tkinter as tk
import random

class Page1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg=self.get_random_color())
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Page 1!", font=("Arial", 20))
        self.label.pack(pady=50)
        self.button = tk.Button(self, text="Go to Page 2", command=self.go_to_page2)
        self.button.pack()

    def go_to_page2(self):
        self.master.switch_frame(Page2)

    def get_random_color(self):
        r = lambda: random.randint(0, 255)
        return '#{:02x}{:02x}{:02x}'.format(r(), r(), r())

class Page2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg=self.get_random_color())
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Page 2!", font=("Arial", 20))
        self.label.pack(pady=50)
        self.button = tk.Button(self, text="Go to Page 1", command=self.go_to_page1)
        self.button.pack()

    def go_to_page1(self):
        self.master.switch_frame(Page1)

    def get_random_color(self):
        r = lambda: random.randint(0, 255)
        return '#{:02x}{:02x}{:02x}'.format(r(), r(), r())

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self._frame = None
        self.geometry(f"{random.randint(300, 500)}x{random.randint(300, 500)}")
        self.title("Simple OOP App")
        self.switch_frame(Page1)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
