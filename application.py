# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")


# Define a function to show/hide widget
def show_widget():
   label.pack()
   label1.pack()
   b1.configure(text="Hide", command=hide_widget)

def hide_widget():
   label.pack_forget()
   label1.forget()
   b1.configure(text="Show", command=show_widget)

# Add a Button widget
b1 = ttk.Button(win, text="Hide", command=hide_widget)
b1.pack(pady=20)

# Add a label widget
label = ttk.Label(win, text="Eat, Sleep, Code and Repeat", font=('Aerial 11'))
label.pack(pady=30)


# IMAGE STUFF
image1 = Image.open("image1.PNG")
test = ImageTk.PhotoImage(image1)
label1 = ttk.Label(image=test)
label1.image = test
# label1.place(x=50, y=50)
# label1.forget()

win.mainloop()