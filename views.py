from tkinter import *
from tkinter.ttk import *

current_frame = ""


def toggle(root, frame):
    global current_frame
    frame.destroy()
    if current_frame == "login":
        showRegisterUi(root)
    elif current_frame == "register":
        showLoginUi(root)


def showLoginUi(root):
    global current_frame
    current_frame = "login"
    login_frame = Frame(root, style="TFrame")
    login_frame.pack()

    login_label = Label(login_frame, text="Login", style="TLabel", width=15, anchor="center")
    login_label.grid(row=0, column=0, columnspan=2, pady=20)

    username_label = Label(login_frame, text="Username:", style="TSLabel.TLabel")
    username_label.grid(sticky='w', row=1, column=0, padx=5, pady=5)
    username_entry = Entry(login_frame, font=("Helvetica", 18), width=20)
    username_entry.grid(row=1, column=1, padx=5, pady=5)

    password_label = Label(login_frame, text="Password:", style="TSLabel.TLabel")
    password_label.grid(sticky='w', row=2, column=0, padx=5, pady=5)
    password_entry = Entry(login_frame, font=("Helvetica", 18), width=20, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    login_button = Button(login_frame, text="Login", style="TButton")
    login_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    register_button = Button(login_frame, text="Register", style="TButton")
    register_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    register_button.bind("<Button-1>", lambda event: toggle(root, login_frame))


def showRegisterUi(root):
    global current_frame
    current_frame = "register"
    reg_frame = Frame(root, style="TFrame")
    reg_frame.pack()

    login_label = Label(reg_frame, text="Registration", style="TLabel", width=15, anchor="center")
    login_label.grid(row=0, column=0, columnspan=2, pady=20)

    username_label = Label(reg_frame, text="Username:", style="TSLabel.TLabel")
    username_label.grid(sticky='w', row=1, column=0, padx=5, pady=5)
    username_entry = Entry(reg_frame, font=("Helvetica", 18), width=20)
    username_entry.grid(row=1, column=1, padx=5, pady=5)

    fullname_label = Label(reg_frame, text="Fullname:", style="TSLabel.TLabel")
    fullname_label.grid(sticky='w', row=2, column=0, padx=5, pady=5)
    fullname_entry = Entry(reg_frame, font=("Helvetica", 18), width=20)
    fullname_entry.grid(row=2, column=1, padx=5, pady=5)

    email_label = Label(reg_frame, text="Email:", style="TSLabel.TLabel")
    email_label.grid(sticky='w', row=3, column=0, padx=5, pady=5)
    email_entry = Entry(reg_frame, font=("Helvetica", 18), width=20)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    password_label = Label(reg_frame, text="Password:", style="TSLabel.TLabel")
    password_label.grid(sticky='w', row=4, column=0, padx=5, pady=5)
    password_entry = Entry(reg_frame, font=("Helvetica", 18), width=20, show="*")
    password_entry.grid(row=4, column=1, padx=5, pady=5)

    confirm_pass_label = Label(reg_frame, text="Confirm Password:", style="TSLabel.TLabel")
    confirm_pass_label.grid(sticky='w', row=5, column=0, padx=5, pady=5)
    password_entry = Entry(reg_frame, font=("Helvetica", 18), width=20, show="*")
    password_entry.grid(row=5, column=1, padx=5, pady=5)

    continue_button = Button(reg_frame, text="Continue", style="TButton")
    continue_button.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    continue_button.bind("<Button-1>", lambda event: toggle(root, reg_frame))
