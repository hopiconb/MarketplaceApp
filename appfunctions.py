import csv
from tkinter import messagebox
from main import *


def frame_change(old, new):
    old.grid_forget()
    new.grid(row=1, column=0, columnspan=3)

def wrong_cred():
    messagebox.showwarning("Warning", "Username or password are wrong")

def user_taken():
    messagebox.showwarning("Warning", "Username already registered\nplease retry with something else")

def success_r():
    messagebox.showinfo("Success", "Account created\nProced to login")

def print_something(something):
    print(something)

def user_long(username):
    messagebox.showwarning("Warning", f"{username} is too long\ntry something 8 characters or under")

def open_browse_prod():
    print()

def success_s():
    messagebox.showinfo("Success", "Item listed")

def sell(name, desc, user, price, contact, window):
    db = open("products.csv", "a+", newline="")
    if len(name) <= 10:
        if len(desc) <= 20:
            with db:
                write = csv.writer(db)
                write.writerow([name.strip(), desc.strip(), user, price.strip(), contact.strip()])
                success_s()
                window.destroy()
        else:
            messagebox.showwarning("Warning", "Description is too long\nplease use 20 or less characters")
    else:
        messagebox.showwarning("Warning", "Name is too long\nplease use 10 or less characters")

def show_items(name, desc, user, price, contact, list, canvas):
    db = open("products.csv", "r+")
    reader = csv.reader(db)
    for row in reader:
        frame = Frame(list, relief="solid")
        name_label = Label(frame, text=row[0]).pack()
        desc_label = Label(frame, text=row[1]).pack()
        user_label = Label(frame, text=row[2]).pack()
        price_label = Label(frame, text=row[3]).pack()
        contact_label = Label(frame, text=row[4]).pack()
        frame.pack()
    list.update_idletask()
    canvas.config(scrollregion=canvas.bbox("all"))



if __name__ == "__main__":
    print("=====")





