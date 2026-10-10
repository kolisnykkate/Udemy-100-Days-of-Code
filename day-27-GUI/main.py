import tkinter

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
my_label.config(text = "New Text")
# my_label.pack(side="left")
# my_label.place(x=100, y=100)
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)


# Button
my_button = tkinter.Button(text = "Click me", command=button_clicked)
# my_button.pack()
my_button.grid(row=1, column=1)

new_button = tkinter.Button(text = "And me", command=button_clicked)
new_button.grid(row=0, column=2)


# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(row=3, column=3)


window.mainloop()
