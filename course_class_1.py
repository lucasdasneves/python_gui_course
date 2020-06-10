# python's gui
# Check out the classes link: https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

from tkinter import *

# first thing we are going to create is the widget root
root = Tk()

# Creating something in tk demands two steps: to define the thing and put it up on the screen
# Creating a Label Widget
myLabel = Label(root, text="Hello World!")

# Now we put the thing onto the root widget or the window. There are to steps to do that: pack and (next class)
# Shoving in onto the screen

myLabel.pack()

root.mainloop()