import tkinter

def calculate():
    km = float(miles_input.get()) * 1.6093
    km_output = round(km, 2)
    km_output_label.config(text = km_output)


window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(300, 200)
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=7)
miles_input.grid(row=0, column=1,padx=10, pady = 10)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
is_equal_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="km")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

km_output_label = tkinter.Label()
km_output_label.grid(row=1, column=1)
km_output_label.config(padx=10, pady=10)

calc_button = tkinter.Button(text="Calculate", command=calculate)
calc_button.grid(row=2, column=1)
calc_button.config(padx=10, pady=10)






window.mainloop()