from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{"email": email,
                   "password": password}
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message="Please make sure the website and password are entered correctly")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n email: {email} \n Password entered : {password}\n Is it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data =  json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0,END)
                password_input.delete(0, END)

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message = "File does not exists")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"email: {email}\n password: {password}")
            else:
                messagebox.showinfo(title="Alert", message="No details for the input found in the json file")
            


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

website_button = Button(text="search", width=13, command=find_password)
website_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)


email_input = Entry(width=35)
email_input.grid(column=1, row=2,columnspan = 2)
email_input.insert(0,"tejaswi.kotaru@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=18)
password_input.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)

add_entry = Button(text="Add", width=36, command=save)
add_entry.grid(column=1, row=4,columnspan = 2)


window.mainloop()