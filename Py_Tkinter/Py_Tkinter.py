from tkinter import *
from tkinter import ttk

root1 = Tk()
root1.title("Tkinter")
root1.geometry("300x250")
root1.maxsize(300,250)
root1.minsize(200,150)
root1.attributes("-alpha", 0.95)
btn = ttk.Button(text="Button")
btn.pack()
label = Label(text="Hello World!")
label.pack()

root1.mainloop()
