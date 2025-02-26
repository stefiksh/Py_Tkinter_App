from tkinter import *
from tkinter import ttk

root1 = Tk()
root1.title("Tkinter")
root1.geometry("300x250")
root1.maxsize(300,250)
root1.minsize(200,150)
root1.attributes("-alpha", 0.95)
label = Label(text="Press Button!")
label.pack()
btn = ttk.Button(text="Pressed me!")
btn.pack()

root1.mainloop()
