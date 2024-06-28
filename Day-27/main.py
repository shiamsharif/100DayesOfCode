from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


""" Label """
my_label = Label(text="ShiamSharif", font=("Comic Sans MS", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"


""" Button """
def clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got Clicked.")

button = Button(text="Click me", command=clicked)
button.pack()


""" Entry """
input = Entry()
input.pack()





 

window.mainloop()