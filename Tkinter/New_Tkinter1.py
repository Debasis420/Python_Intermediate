from tkinter import *

FONT = ("Arial", 24, "bold")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="I am A Label", font=FONT)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Enter New Text")

# Button
button = Button(text="Click Here", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()
