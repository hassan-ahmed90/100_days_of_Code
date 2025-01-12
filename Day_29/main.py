import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list+=[random.choice(letters) for char in range(random.randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list+=[random.choice(symbols) for sym in range(random.randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list+=[random.choice(letters) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password="".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    print(f"Your password is: {password}")
    password_entry.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    name=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    website_dic={
        name:{
            "Email":email,
            "Password":password
        }
    }

    if len(name) ==0 or len(password) ==0:
        messagebox.showinfo(title="Warning",message="Please dont leave field empty")
    else:
        is_ok=messagebox.askokcancel(title=name,message=f"Email: {email}\n Password: {password}\n Is it ok to save ?")
        if is_ok:
            try:
                # Try reading the existing data
                with open("passwords.json", "r") as data_file:
                    data = json.load(data_file)  # Read JSON content from file
            except FileNotFoundError:
                # If the file doesn't exist, initialize an empty dictionary
                data = {}
            except json.JSONDecodeError:
                # If the file exists but is empty or corrupted, also initialize an empty dictionary
                data = {}

                # Update the old data with the new data
            data.update(website_dic)

            # Save the updated data back to the file
            with open("passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            # Clear input fields after saving
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="Password saved successfully!")

def search():
    name=website_entry.get()
    try:
        with open('passwords.json',"r")as file:
            data=json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No data Found")
    if name in data:
        e=data[name]["Email"]
        p=data[name]["Password"]
        messagebox.showinfo(title=name,message=f"Email:{e}\n Password: {p}")

    else:
        messagebox.showwarning(title="Not Found",message="Data not found")
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas =Canvas(height=200,width=200)
imagesrc=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=imagesrc)
canvas.grid(row=0,column=1)

#Labels
website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label= Label(text="Password")
password_label.grid(row=3,column=0)

#Entries
website_entry=Entry(width=18)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"hassanahmedrajput@gmail.com ")
password_entry=Entry(width=18)
password_entry.grid(row=3,column=1)

#Button
generate_button=Button(width=14,text="Generate Password",command=password_generator)
generate_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(width=14,text="Search",command=search)
search_button.grid(row=1,column=2)

window.mainloop()