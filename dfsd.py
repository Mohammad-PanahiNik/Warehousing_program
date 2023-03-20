# import tkinter as tk
# import time
# import math

# class Clock(tk.Canvas):
#     def __init__(self, master, **kwargs):
#         tk.Canvas.__init__(self, master, **kwargs)
#         self.config(width=300, height=300, bg='black', highlightthickness=0)
#         self.hour = self.create_line(0, 0, 0, 0, width=4, fill='white')
#         self.minute = self.create_line(0, 0, 0, 0, width=3, fill='white')
#         self.second = self.create_line(0, 0, 0, 0, width=2, fill='red')
#         self.oval = self.create_oval(5, 5, 295, 295, width=2, outline='white')
#         self.draw_clock()
        
#     def draw_clock(self):
#         current_time = time.localtime()
#         h = current_time.tm_hour % 12
#         m = current_time.tm_min
#         s = current_time.tm_sec
        
#         # Calculate the angle for the hour hand
#         hour_angle = (h * 30) + (m * 0.5)
        
#         # Calculate the angle for the minute hand
#         minute_angle = m * 6
        
#         # Calculate the angle for the second hand
#         second_angle = s * 6
        
#         # Convert angles to radians
#         hour_angle_radians = hour_angle * 3.14 / 180
#         minute_angle_radians = minute_angle * 3.14 / 180
#         second_angle_radians = second_angle * 3.14 / 180
        
#         # Calculate the end points for each hand
#         hour_x = 150 + 60 * math.sin(hour_angle_radians)
#         hour_y = 150 - 60 * math.cos(hour_angle_radians)
#         minute_x = 150 + 80 * math.sin(minute_angle_radians)
#         minute_y = 150 - 80 * math.cos(minute_angle_radians)
#         second_x = 150 + 100 * math.sin(second_angle_radians)
#         second_y = 150 - 100 * math.cos(second_angle_radians)
        
#         # Draw the hands
#         self.coords(self.hour, 150, 150, hour_x, hour_y)
#         self.coords(self.minute, 150, 150, minute_x, minute_y)
#         self.coords(self.second, 150, 150, second_x, second_y)
        
#         # Call the draw_clock method again after 1 second
#         self.after(1000, self.draw_clock)

# root = tk.Tk()
# root.title('Clock')
# clock = Clock(root)
# clock.pack(expand=True, fill='both')
# root.mainloop()

#==================================================================================================================================
# from tkinter import *
# import math
# import time

# class Clock:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Clock")
#         self.canvas = Canvas(self.root, width=400, height=400, bg='black')
#         self.canvas.pack()
#         self.draw_clock_face()
#         self.draw_clock_hands()
#         self.update_clock()
#         self.root.mainloop()

#     def draw_clock_face(self):
#         for i in range(60):
#             angle = math.radians(i * 6)
#             inner_radius = 150
#             outer_radius = 170
#             x1 = 200 + inner_radius * math.sin(angle)
#             y1 = 200 - inner_radius * math.cos(angle)
#             x2 = 200 + outer_radius * math.sin(angle)
#             y2 = 200 - outer_radius * math.cos(angle)
#             if i % 5 == 0:
#                 self.canvas.create_line(x1, y1, x2, y2, width=4, fill='white')
#             else:
#                 self.canvas.create_line(x1, y1, x2, y2, width=2, fill='white')

#     def draw_clock_hands(self):
#         self.hour_hand = self.canvas.create_line(200, 200, 200, 140, width=8, fill='white')
#         self.minute_hand = self.canvas.create_line(200, 200, 200, 100, width=4, fill='white')
#         self.second_hand = self.canvas.create_line(200, 200, 200, 100, width=2, fill='red')

#     def update_clock(self):
#         current_time = time.localtime()
#         hour = current_time.tm_hour % 12
#         minute = current_time.tm_min
#         second = current_time.tm_sec

#         hour_angle = math.radians((hour * 30) + (minute * 0.5))
#         minute_angle = math.radians(minute * 6)
#         second_angle = math.radians(second * 6)

#         self.canvas.coords(self.hour_hand, 200, 200, 200 + 70 * math.sin(hour_angle), 200 - 70 * math.cos(hour_angle))
#         self.canvas.coords(self.minute_hand, 200, 200, 200 + 90 * math.sin(minute_angle), 200 - 90 * math.cos(minute_angle))
#         self.canvas.coords(self.second_hand, 200, 200, 200 + 90 * math.sin(second_angle), 200 - 90 * math.cos(second_angle))

#         self.root.after(1000, self.update_clock)

# Clock()

#==============================================================================================================================================
from tkinter import *
import math
import time

class Clock:
    def __init__(self):
        self.root = Tk()
        self.root.title("Clock")
        self.canvas = Canvas(self.root, width=400, height=400, bg='#222222')
        self.canvas.pack()
        self.draw_clock_face()
        self.draw_clock_hands()
        self.update_clock()
        self.root.mainloop()

    def draw_clock_face(self):
        self.canvas.create_oval(40, 40, 360, 360, width=10, outline='#FDFDFF')
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x1 = 200 + 150 * math.cos(angle)
            y1 = 200 + 150 * math.sin(angle)
            x2 = 200 + 130 * math.cos(angle)
            y2 = 200 + 130 * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=8, fill='#FDFDFF')

    def draw_clock_hands(self):
        self.hour_hand = self.canvas.create_line(200, 200, 200, 170, width=10, fill='#FDFDFF')
        self.minute_hand = self.canvas.create_line(200, 200, 200, 120, width=6, fill='#FDFDFF')
        self.second_hand = self.canvas.create_line(200, 200, 200, 120, width=3, fill='#FF3E4D')

    def update_clock(self):
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        hour_angle = math.radians((hour * 30) + (minute * 0.5))
        minute_angle = math.radians(minute * 6)
        second_angle = math.radians(second * 6)

        self.canvas.coords(self.hour_hand, 200, 200, 200 + 80 * math.sin(hour_angle), 200 - 80 * math.cos(hour_angle))
        self.canvas.coords(self.minute_hand, 200, 200, 200 + 100 * math.sin(minute_angle), 200 - 100 * math.cos(minute_angle))
        self.canvas.coords(self.second_hand, 200, 200, 200 + 100 * math.sin(second_angle), 200 - 100 * math.cos(second_angle))

        self.root.after(1000, self.update_clock)

Clock()


