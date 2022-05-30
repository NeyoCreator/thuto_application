import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#0.ROOT WINDOW
root = tk.Tk()
root.geometry('700x500')
root.resizable(False, False)
root.title('Button Demo')

#1.MESSAGE FUNCTION
def load_image():
    print("We are here")
#Load_Image
load_button = ttk.Button(
    root,
    text='Load Image',
    command=load_image()
)
load_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#2.WORKING WITH IMAGE
img = ImageTk.PhotoImage(Image.open("image1.PNG"))
# Create a Label Widget to display the text or Image
label = ttk.Label(root, image = img)
label.pack()

root.mainloop()