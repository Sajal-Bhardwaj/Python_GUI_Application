from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

win=Tk()
win.geometry("900x640")
win.title("Admission Form")

s= ttk.Style()
s.configure("new.TFrame", background="orange")

tabs=ttk.Notebook(win)

tab1=ttk.Frame(tabs,style='new.TFrame')
tabs.add(tab1,text="AD")
tabs.pack(expan=1,fil="both")


win.mainloop()
