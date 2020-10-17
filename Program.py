import tkinter as tk
from tkinter import filedialog, Text
import os


app = tk.Tk()

app.iconbitmap(r'C:\Users\fsd72\Desktop\unnamed.ico')
app.title('My First program')


myLabel = tk.Label(app, text="Hello World!")
myLabel.pack()
tenttext = tk.Label(app, text="This is my first Program using Python!")
tenttext.pack()

app.mainloop()
