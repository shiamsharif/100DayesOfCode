from tkinter import *

window = Tk()
window.title("Mile to Kilometar Conversion")
window.minsize(width=400, height=250)
window.config(padx=20, pady=20)

def Mile_To_Km():
    miles = int(input.get())
    km = miles * 1.60934
    label_output.config(text=km)

""" Label """
my_label = Label(text="is equal to", font=("Comic Sans MS", 16, "normal"))
my_label.config(padx=5, pady=5)
my_label.grid(column=0, row=3)


""" Entry """
input = Entry(width=10)
input.grid(column=3, row=2)


""" label Output """
label_output = Label(text="0",font=("Comic Sans MS", 16, "bold"))
label_output.config(padx=5, pady=5)
label_output.grid(column=3, row=3)


""" Button """
button = Button(text="Run", command=Mile_To_Km)
button.config(padx=5, pady=5)
button.grid(column=3, row=4)

""" Label Miles"""
label_mile = Label(text="Miles",font=("Comic Sans MS", 16, "bold"))
label_mile.config(padx=5, pady=5)
label_mile.grid(column=4, row=2)


""" Label _Km"""
label_Km = Label(text="Km.",font=("Comic Sans MS", 16, "bold"))
label_Km.config(padx=5, pady=5)
label_Km.grid(column=4, row=3)



window.mainloop()