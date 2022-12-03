import tkinter as tk
from tkinter.ttk import Frame
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image

#creating main window
m=tk.Tk()
m.geometry("300x380")
frame=Frame(m)
frame.pack()
bottomframe=Frame(m)
bottomframe.pack(side=tk.BOTTOM)

#setting name for the window
m.title('Emergency Broadcast System')
#creating a label
l1=tk.Label(text="EMERGENCY HELP SERVICES", fg='black')
l1.config(width='150')
emer=ImageTk.PhotoImage(Image.open("emergency.png"))
my_pic=Label(frame,image=emer)
l1.pack()
l2=tk.Label(text="SERVICES AVAILABLE")
l2.config(width='100')
l2.pack()
my_pic.pack()
def OnClick1():
    tkinter.messagebox.showinfo("Confirm","Are you sure? Click Ok to place a call")
#creating a button
b1=tk.Button(m,text='Ambulance',width=10,height=2,bg='blue',fg='yellow',command=OnClick1)
b1.pack(side=tk.LEFT,pady=50)
def OnClick():
    tkinter.messagebox.showinfo("Confirm","Are you sure? Click Ok to continue")
b2=tk.Button(m,text='Fire Emergency',width=20,height=2,bg='green',fg='black',command=OnClick)
b2.pack(side=tk.LEFT,pady=50)
b3= tk.Button(m,text='Police',width=10,height=2,bg='red',fg='white',command=OnClick1)
b3.pack(side=tk.LEFT,pady=50)
#entering event main loop
m.mainloop() 