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

""" Text """
text = Text(height=5, width=30)
# put cursor in testbox.
text.focus()
# add some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# gets the current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

""" Spinbox """
def spinbox_used():
    print(spinbox.get())

 

window.mainloop()