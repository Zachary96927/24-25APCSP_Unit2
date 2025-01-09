#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
from cProfile import label

# main window
root = tk.Tk()
root.wm_geometry("200x200")
# create empty frame
frame_login = tk.Frame(root)

#create empty frame
frame_login.grid()

#frame login widget

lbl_username = tk.Label(frame_login, text='Username:', font=("TkMenuFont 15"))
lbl_username.pack(padx=50, pady=50)

ent_username = tk.Entry(frame_login,bd=3)
ent_username.pack()

root.mainloop()