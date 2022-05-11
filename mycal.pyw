from tkinter import *
from tkcalendar import *
root = Tk()
root.title('Calendar-codevision')
root.geometry('600x400')
cal = Calendar(root,selectmode='day')
cal.pack(fill=BOTH,expand=True)
root.mainloop()