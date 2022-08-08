from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.geometry("500x500")
root.title("Class Activity 171")
clock_img = ImageTk.PhotoImage(Image.open("clock.jpg"))

india_label = Label(root, text = "India : ")
india_label.place(relx = 0.4, rely = 0.1, anchor = CENTER)
india_clock = Label(root)
india_clock.place(relx = 0.3, rely = 0.5, anchor = CENTER)
india_clock["image"] = clock_img
india_time = Label(root)
india_time.place(relx = 0.6, rely = 0.1, anchor = CENTER)

us_label = Label(root, text = "United States : ")
us_label.place(relx = 0.4, rely = 0.2, anchor = CENTER)
us_clock = Label(root)
us_clock.place(relx = 0.7, rely = 0.5, anchor = CENTER)
us_clock["image"] = clock_img
us_time = Label(root)
us_time.place(relx = 0.6, rely = 0.2, anchor = CENTER)

class indian_time() :
    def times(self) :
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "time : " + current_time
        india_time.after(200, self.times)
        
class us_time() :
    def times(self) :
        home = pytz.timezone('US/Eastern')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        us_time["text"] = "time : " + current_time
        us_time.after(200, self.times)

obj1 = indian_time()
obj2 = us_time()
btn1 = Button(root, text = "Show Indian Time", command = obj1.times)
btn2 = Button(root, text = "Show US Time", command = obj2.times)
btn1.place(relx = 0.4, rely = 0.8, anchor = CENTER)
btn2.place(relx = 0.6, rely = 0.8, anchor = CENTER)
root.mainloop()