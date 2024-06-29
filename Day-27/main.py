from tkinter import *

def clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got Clicked.")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


""" Label """
my_label = Label(text="ShiamSharif", font=("Comic Sans MS", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"


""" Button """
button = Button(text="Click me", command=clicked)
button.grid(column=1, row=1)

""" New Button """
New_button = Button(text="Press me", command=clicked)
New_button.grid(column=2, row=0 )


""" Entry """
input = Entry()
input.grid(column=3, row=3)

""" Text """
# text = Text(height=5, width=30)
# # put cursor in testbox.
# text.focus()
# # add some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # gets the current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# """ Spinbox """
# def spinbox_used():
#     print(spinbox.get())

 

window.mainloop()