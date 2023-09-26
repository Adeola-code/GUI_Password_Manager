from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]
    password_list= password_numbers+password_letters+password_symbols


    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data={website:{
        "email": email,
        "password": password
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field(s) empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def search():
    with open("data.json", "r") as data_file:
        # Reading old data
        data = json.load(data_file)
        try:
            user_data=(data[website_entry.get().lower()])
            user_email=(user_data["email"])
            user_password=(user_data["password"])
            messagebox.showinfo("Info",message=f"Email: {user_email}\nPassword: {user_password}")
        except KeyError:
            messagebox.showinfo(title="Oops",message="Error, No data file found!")

# ---------------------------- UI SETUP ------------------------------- #
FONT = ("Arial", 12, "normal")
window = Tk()
window.title("My Password Manager")
window.config(pady=20, padx=50)
# window.minsize(600,350)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
website_label = Label(text="Website: ", font=FONT)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=FONT)
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string="adeola@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", font=FONT,command=generate_password)
generate_button.grid(row=3, column=2)
search_button = Button(text="Search", font=FONT, width=10, command=search)
search_button.grid(row=1, column=2)
add_button = Button(text="Add", font=FONT, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
