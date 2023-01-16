import tkinter
from tkinter import *
from PIL import ImageTk,Image
from authenticate import *
from appfunctions import *

if __name__ == "__main__":
    # window properties
    root = Tk()
    root.title("Marketplace")
    root.iconbitmap("icon.ico")
    root.resizable(width=False, height=False)
    root.geometry("600x1000")

    register_user = tkinter.StringVar()
    register_pass = tkinter.StringVar()
    login_user = tkinter.StringVar()
    login_pass = tkinter.StringVar()

    # credential storage
    username = StringVar()
    password = StringVar()

    # Images



    # window skeleton
    root.rowconfigure(0,weight=10)
    root.rowconfigure(1,weight=88)
    root.rowconfigure(2,weight=2)


    # logo frame and image properties
    logo_frame = Frame(root, width=600, height=100)
    logo_frame.grid(row=0, column=0, columnspan=3, sticky=N)

    logo_image = ImageTk.PhotoImage(Image.open("logo.png"))
    logo_label = Label(logo_frame, image=logo_image).pack()


    # auth frame
    auth_frame = Frame(root, width=600, height=700)
    auth_frame.grid(row=1, column=0, columnspan=3)


    # register/login buttons
    login_select_button = Button(auth_frame, text="Login", command=lambda: frame_change(auth_frame,login_frame)).pack()
    register_select_button = Button(auth_frame, text="Register", command=lambda: frame_change(auth_frame,register_frame)).pack()


    # login frame
    login_frame = Frame(root, width=600, height=700)
    login_title = Label(login_frame, text="Login window", font="Helvetica").pack()
    login_u_label = Label(login_frame, text="Username:").pack()
    login_entry_u = Entry(login_frame, width=25, textvariable=login_user).pack()
    login_p_label = Label(login_frame, text="Password:").pack()
    login_entry_p = Entry(login_frame, width=25, textvariable=login_pass).pack()

    # buttons
    login_button = Button(login_frame, text="Login", command=lambda: login(login_user.get(),login_pass.get(),login_frame,main_frame_menu, username, password)).pack()
    login_back_button = Button(login_frame, text="Back", command=lambda: frame_change(login_frame,auth_frame)).pack()


    # register frame
    register_frame = Frame(root, width=600, height=700)
    register_title = Label(register_frame, text="Register window", font="Helvetica").pack()
    register_u_label = Label(register_frame, text="Username:").pack()
    register_entry_u = Entry(register_frame, width=25, textvariable=register_user).pack()
    register_p_label = Label(register_frame, text="Password:").pack()
    register_entry_p = Entry(register_frame, width=25, textvariable=register_pass).pack()

    # buttons
    register_button = Button(register_frame, text="Register", command=lambda: register(register_user.get(),register_pass.get(),register_frame,login_frame)).pack()
    register_back_button = Button(register_frame, text="Back", command=lambda: frame_change(register_frame,auth_frame)).pack()


    # main frame
    main_frame_menu = Frame(root, width=600, height=700)
    way_label = Label(main_frame_menu, text="What are you?", font="Helvetica").pack()
    empty_label1 = Label(main_frame_menu).pack()
    seller_button = Button(main_frame_menu, text="Seller", width=40, command=lambda: print_something(username)).pack()
    empty_label2 = Label(main_frame_menu).pack()
    buyer_button = Button(main_frame_menu, text="Buyer", width=40).pack()
    empty_label3 = Label(main_frame_menu).pack()
    settings_button = Button(main_frame_menu, text="Settings", width=40).pack()


    # version frame
    version_frame = Frame(root)
    version_label = Label(root, text="v1.0", relief=SUNKEN, padx=10)
    version_label.grid(row=2, column=2, sticky=E+S)

    root.mainloop()
