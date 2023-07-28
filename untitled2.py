# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:41:49 2023

@author: User
"""

from tkinter import*
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x450")
image_clock = ImageTk.PhotoImage(Image.open("clock.jpg"))

india_label = Label(root,text="india")
india_label.place(relx=0.2,rely=0.05, anchor= CENTER)

india_clock = Label(root)
india_clock["image"]=image_clock
india_clock.place(relx=0.2,rely=0.35,anchor = CENTER)

india_time=Label(root)
india_time.place(relx=0.2,rely=0.65,anchor= CENTER)

usa_label = Label(root,text="usa")
usa_label.place(relx=0.7,rely=0.05, anchor=CENTER)

usa_clock = Label(root)
usa_clock["image"] =image_clock
usa_clock.place(relx=0.7,rely=0.35, anchor = CENTER)

usa_time=Label(root)
usa_time.place(relx=0.7,rely=0.65,anchor= CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time :"+ current_time
        india_time.after(200,self.times)
        
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time :"+ current_time
        usa_time.after(200,self.times)
        
obj_india=India()
obj_usa=USA()
india_btn=Button(root,text="show time", command=obj_india.times)
india_btn.place(relx=0.2,rely=0.8,anchor = CENTER)
usa_btn=Button(root,text="show time", command=obj_usa.times)
usa_btn.place(relx=0.7,rely=0.8, anchor = CENTER)
root.mainloop()

