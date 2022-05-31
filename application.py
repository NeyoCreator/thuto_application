#0.IMPORTS
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

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

    showinfo(
        title='Selected File',
        message=filename
    )
    x =filename[-10:]

    # IMAGE STUFF
    image1 = Image.open(f"images/{x}")
    test = ImageTk.PhotoImage(image1)
    label1 = ttk.Label(image=test)
    label1.image = test
    label1.place(x=50, y=50)
    label1.forget()
    return x

#2.SHOW FUNCTION
def show_widget():
   label.pack()
   label1.pack()
   b1.configure(text="Hide", command=hide_widget)

#3.HIDE FUNCTION
def hide_widget():
   label.pack_forget()
   label1.forget()
   b1.configure(text="Show", command=show_widget)



#4.DISPLAY BUTTON
b1 = ttk.Button(win, text="Hide", command=hide_widget)
b1.pack(pady=20)

# Add a label widget
label = ttk.Label(win, text="Eat, Sleep, Code and Repeat", font=('Aerial 11'))
label.pack(pady=30)



# open button
open_button = ttk.Button(
    win,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

win.mainloop()