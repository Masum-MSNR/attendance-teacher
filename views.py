from tkinter import *
from tkinter.ttk import *
from validators import *
from funcs import *


def toggle(root, frame, ui):
    frame.destroy()
    if ui == "login":
        showLoginUi(root)
    elif ui == "register":
        showRegisterUi(root)
    elif ui == "main":
        showMainUi(root)


def showLoginUi(root):
    warning_text = StringVar()
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
    login_button.bind("<Button-1>",
                      lambda event: login(root, login_frame, username_entry.get(), password_entry.get(), warning_text))

    register_button = Button(login_frame, text="Register", style="TButton")
    register_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    register_button.bind("<Button-1>", lambda event: toggle(root, login_frame, 'register'))

    warning_label = Label(login_frame, textvariable=warning_text, style="Warning.TLabel", anchor="center")
    warning_label.grid(row=8, column=0, columnspan=2, pady=5)


def login(root, frame, username, password, warning_text):
    res = loginValidator(username, password)
    if res["status"] is False:
        warning_text.set(res["message"])
        return False
    res = doLogin(username, password)
    if res["status"] is False:
        warning_text.set(res["message"])
    else:
        toggle(root, frame, "main")


def showRegisterUi(root):
    warning_text = StringVar()
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
    confirm_pass_entry = Entry(reg_frame, font=("Helvetica", 18), width=20, show="*")
    confirm_pass_entry.grid(row=5, column=1, padx=5, pady=5)

    continue_button = Button(reg_frame, text="Continue", style="TButton")
    continue_button.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    continue_button.bind("<Button-1>",
                         lambda event: register(root, reg_frame, username_entry.get(), fullname_entry.get(),
                                                email_entry.get(), password_entry.get(), confirm_pass_entry.get(),
                                                warning_text))

    back_button = Button(reg_frame, text="Back", style="TButton")
    back_button.grid(row=7, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    back_button.bind("<Button-1>", lambda event: toggle(root, reg_frame, 'login'))

    warning_label = Label(reg_frame, textvariable=warning_text, style="Warning.TLabel", anchor="center")
    warning_label.grid(row=8, column=0, columnspan=2, pady=5)


def register(root, frame, username, fullname, email, password, confirm_pass, warning_text):
    res = registerValidator(username, fullname, email, password, confirm_pass)
    if res["status"] is False:
        warning_text.set(res["message"])
        return False
    res = doRegister(username, password, fullname, email)
    if res["status"] is False:
        warning_text.set(res["message"])
    else:
        toggle(root, frame, "login")


def showMainUi(root):
    home_frame = Frame(root, style="TFrame")
    home_frame.pack()

    welcome_label = Label(home_frame, text="Welcome", style="TLabel", width=15, anchor="center")
    welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

    logout_button = Button(home_frame, text="Logout", style="TButton")
    logout_button.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    logout_button.bind("<Button-1>", lambda event: toggle(root, home_frame, 'login'))
