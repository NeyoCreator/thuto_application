#0.IMPORTS
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
import os

#1.FRAMES
win = Tk()
win.geometry("700x350")

def select_file():
    global label1
    filetypes = (
        ('PNG image', '*.png'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )
    x =filename[-10:]

    head, tail = os.path.split(filename)
    print(tail)

    # IMAGE STUFF
    image1 = Image.open(f"images/{tail}")
    test = ImageTk.PhotoImage(image1)
    label1 = ttk.Label(image=test)
    label1.image = test
    label1.place(x=50, y=50)




# open button
open_button = ttk.Button(
    win,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

win.mainloop()