from tkinter import messagebox


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


if __name__ == "__main__":
    print("=====")