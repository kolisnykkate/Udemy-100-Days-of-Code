from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = ([random.choice(letters) for _ in range(nr_letters)]
                     + [random.choice(symbols) for _ in range(nr_symbols)]
                     + [random.choice(numbers) for _ in range(nr_numbers)])


    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Oops", "Please fill all required fields.")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"Check your info before saving:\nEmail: {email}\n"
                                                   f"Password: {password}\nDo you wish to continue?")

        if is_ok:
            with open("saved_data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)

website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_lbl = Label(text="Email/Username:")
email_lbl.grid(row=2, column=0)

email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "test@test.com")

password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_bttn = Button(text = "Generate Password", width=12, command=generate_password)
generate_bttn.grid(row=3, column=2)

add_bttn = Button(text = "Add", width=35, command=save_data)
add_bttn.grid(row=4, column=1, columnspan=2)


window.mainloop()