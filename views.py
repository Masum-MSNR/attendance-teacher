import string
import random
from datetime import date, datetime
from tkinter import *
from tkinter.ttk import *
from validators import *
from funcs import *

import customtkinter as ctk

current_user = {}
current_class = {}

g_current_date = ""
current_attendances = []


def toggle(root, frame, ui):
    frame.destroy()
    if ui == "login":
        showLoginUi(root)
    elif ui == "register":
        showRegisterUi(root)
    elif ui == "main":
        showMainUi(root)
    elif ui == "create_class":
        showCreateClassUi(root)
    elif ui == "take_attendance":
        selectClassToTakeAttendanceUi(root)
    elif ui == "attendance_taking":
        attendanceTakingUi(root)
    elif ui == "attendances":
        classAttendanceUi(root)
    elif ui == "attendance_by_date":
        attendanceByDateUi(root)


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
    username_entry.insert(0, "masum")

    password_label = Label(login_frame, text="Password:", style="TSLabel.TLabel")
    password_label.grid(sticky='w', row=2, column=0, padx=5, pady=5)
    password_entry = Entry(login_frame, font=("Helvetica", 18), width=20, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)
    password_entry.insert(0, "12345678")

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
        global current_user
        current_user = res["data"]
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
    welcome_label.grid(row=0, column=0, pady=20)

    logout_button = Button(home_frame, text="Logout", style="TButton")
    logout_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    logout_button.bind("<Button-1>", lambda event: toggle(root, home_frame, 'login'))

    create_class_button = Button(home_frame, text="Create Class", style="TButton")
    create_class_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    create_class_button.bind("<Button-1>", lambda event: toggle(root, home_frame, 'create_class'))

    take_attendance_button = Button(home_frame, text="Take Attendance", style="TButton")
    take_attendance_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    take_attendance_button.bind("<Button-1>", lambda event: toggle(root, home_frame, 'take_attendance'))

    classes_label = Label(home_frame, text="Classes", style="TLabel", width=15, anchor="center")
    classes_label.grid(row=2, column=0, columnspan=2, pady=20, sticky="w")

    listbox = Listbox(home_frame, border=0, highlightthickness=0,
                      font=("Helvetica", 18))
    listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    listbox.bind("<Double-Button-1>",
                 lambda event: goShowAttendanceUi(root, home_frame, classes["data"].values(), listbox.curselection()))

    classes = getClassesByUsername(current_user["username"])

    for value in classes["data"].values():
        listbox.insert(END, value["class_name"])


def goShowAttendanceUi(root, frame, classes, index):
    global current_class
    current_class = list(classes)[index[0]]
    toggle(root, frame, 'attendances')


def showCreateClassUi(root):
    warning_text = StringVar()
    create_class_frame = Frame(root, style="TFrame")
    create_class_frame.pack()

    create_class_label = Label(create_class_frame, text="Create Class", style="TLabel", width=15, anchor="center")
    create_class_label.grid(row=0, column=0, columnspan=2, pady=20)

    class_name_label = Label(create_class_frame, text="Class Name:", style="TSLabel.TLabel")
    class_name_label.grid(sticky='w', row=1, column=0, padx=5, pady=5)
    class_name_entry = Entry(create_class_frame, font=("Helvetica", 18), width=20)
    class_name_entry.grid(row=1, column=1, padx=5, pady=5)

    class_code_label = Label(create_class_frame, text="Class Code:", style="TSLabel.TLabel")
    class_code_label.grid(sticky='w', row=2, column=0, padx=5, pady=5)
    class_code_entry = Entry(create_class_frame, font=("Helvetica", 18), width=20)
    class_code_entry.grid(row=2, column=1, padx=5, pady=5)

    class_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    class_code_entry.insert(0, class_code)
    class_code_entry.configure(state=DISABLED)

    continue_button = Button(create_class_frame, text="Continue", style="TButton")
    continue_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    continue_button.bind("<Button-1>",
                         lambda event: createClass(root, create_class_frame, class_name_entry.get(),
                                                   class_code_entry.get(), warning_text))

    back_button = Button(create_class_frame, text="Back", style="TButton")
    back_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    back_button.bind("<Button-1>", lambda event: toggle(root, create_class_frame, 'main'))

    warning_label = Label(create_class_frame, textvariable=warning_text, style="Warning.TLabel", anchor="center")
    warning_label.grid(row=5, column=0, columnspan=2, pady=5)


def createClass(root, frame, className, classCode, warning_text):
    res = createClassValidator(className)
    if res["status"] is False:
        warning_text.set(res["message"])
        return False
    res = doCreateClass(className, classCode, current_user["username"])
    if res["status"] is False:
        warning_text.set(res["message"])
    else:
        toggle(root, frame, "main")


def selectClassToTakeAttendanceUi(root):
    select_class_frame = Frame(root, style="TFrame")
    select_class_frame.pack()

    classes = getClassesByUsername(current_user["username"])

    select_class_label = Label(select_class_frame, text="Select Class", style="TLabel", width=15, anchor="center")
    select_class_label.grid(row=0, column=0, columnspan=2, pady=20)

    listbox = Listbox(select_class_frame, border=0, highlightthickness=0,
                      font=("Helvetica", 18))
    listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    listbox.bind("<Double-Button-1>",
                 lambda event: goToAttendanceTakingUi(root, select_class_frame, classes["data"].values(),
                                                      listbox.curselection()[0]))

    for value in classes["data"].values():
        listbox.insert(END, value["class_name"])


def goToAttendanceTakingUi(root, frame, classes, index):
    global current_class
    data_list = list(classes)
    current_class = data_list[index]
    toggle(root, frame, "attendance_taking")


def attendanceTakingUi(root):
    attendance_taking_frame = Frame(root, style="TFrame")
    attendance_taking_frame.pack()

    take_attendance_label = Label(attendance_taking_frame, text=current_class['class_name'] + " Today's Attendance",
                                  style="TLabel", width=30,
                                  anchor="center")
    take_attendance_label.grid(row=0, column=0, columnspan=2, pady=20)

    listbox = Listbox(attendance_taking_frame, border=0, highlightthickness=0,
                      font=("Helvetica", 18))
    listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    back_button = Button(attendance_taking_frame, text="Close", style="TButton")
    back_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    back_button.bind("<Button-1>", lambda event: closeAttendance(root, attendance_taking_frame, "main"))
    openAttendanceInstance(listbox)


def openAttendanceInstance(listbox):
    current_date = datetime.now().strftime("%Y%m%d")
    model = {
        "date": current_date,
        "class_code": current_class['class_code'],
        "open": True,
        "attendance": []
    }
    res = getDb().child("attendance").child(current_class['class_code']).child(current_date).set(model)
    getDb().child("attendance").child(current_class['class_code']).child(current_date).child("attendance").stream(
        lambda event: onAttendanceUpdate(event, listbox))


def onAttendanceUpdate(event, listbox):
    print(event)
    if event["data"] is not None:
        listbox.insert(END, event["data"])


def closeAttendance(root, frame, next_frame):
    current_date = datetime.now().strftime("%Y%m%d")
    res = getDb().child("attendance").child(current_class['class_code']).child(current_date).child("open").set(False)
    toggle(root, frame, next_frame)


def classAttendanceUi(root):
    class_attendance_frame = Frame(root, style="TFrame")
    class_attendance_frame.pack()

    class_attendance_label = Label(class_attendance_frame, text=current_class['class_name'] + " Attendance",
                                   style="TLabel", width=30,
                                   anchor="center")
    class_attendance_label.grid(row=0, column=0, columnspan=2, pady=20)

    listbox = Listbox(class_attendance_frame, border=0, highlightthickness=0,
                      font=("Helvetica", 18))
    listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    listbox.bind("<Double-Button-1>",
                 lambda event: goAttendanceByDateUi(root, class_attendance_frame, data, listbox.curselection()[0]))

    back_button = Button(class_attendance_frame, text="Back", style="TButton")
    back_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    back_button.bind("<Button-1>", lambda event: toggle(root, class_attendance_frame, "main"))

    attendances = getAttendancesByClassCode(current_class['class_code'])
    data = attendances["data"]
    dates = data.keys()
    dates = list(dates)
    dates.reverse()
    for value in dates:
        lDate = datetime.strptime(value, "%Y%m%d").strftime("%d-%m-%Y")
        try:
            if data[value]["attendance"] is not None:
                print(data[value]["attendance"])
        except:
            pass

        listbox.insert(END, lDate)


def goAttendanceByDateUi(root, frame, attendances, index):
    global current_attendances
    data_list = list(attendances.keys())
    data_list.reverse()
    values = attendances.values()
    values = list(values)
    values.reverse()

    try:
        current_attendances = values[index]["attendance"]
    except:
        current_attendances = []
    global g_current_date
    g_current_date = data_list[index]
    toggle(root, frame, "attendance_by_date")


def attendanceByDateUi(root):
    attendance_by_date_frame = Frame(root, style="TFrame")
    attendance_by_date_frame.pack()

    lDate = datetime.strptime(g_current_date, "%Y%m%d").strftime("%d-%m-%Y")

    attendance_by_date_label = Label(attendance_by_date_frame,
                                     text=current_class['class_name'] + " " + lDate + " Attendance",
                                     style="TLabel", width=30, anchor="center")
    attendance_by_date_label.grid(row=0, column=0, columnspan=2, pady=20)

    listbox = Listbox(attendance_by_date_frame, border=0, highlightthickness=0,
                      font=("Helvetica", 18))
    listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    for value in current_attendances:
        listbox.insert(END, value)

    back_button = Button(attendance_by_date_frame, text="Back", style="TButton")
    back_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    back_button.bind("<Button-1>", lambda event: toggle(root, attendance_by_date_frame, "main"))
