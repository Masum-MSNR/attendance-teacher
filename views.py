import string
import random
from datetime import date, datetime
from tkinter import *
from tkinter.ttk import *
from PIL import Image
from scrollable import ScrollableLabelButtonFrame
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
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True)

    warning_text = ctk.StringVar()

    title = ctk.CTkLabel(frame,
                         text="Login",
                         font=("Arial", 30, 'bold'),
                         text_color="white",
                         corner_radius=10,
                         width=400,
                         )
    title.pack(pady=15, ipady=10)

    username_entry = ctk.CTkEntry(frame,
                                  width=400,
                                  placeholder_text="Username",
                                  placeholder_text_color="grey",
                                  corner_radius=10
                                  )
    username_entry.pack(pady=15, ipady=10)

    password_entry = ctk.CTkEntry(frame,
                                  width=400,
                                  placeholder_text="Password",
                                  placeholder_text_color="grey",
                                  corner_radius=10,
                                  show="*"
                                  )
    password_entry.pack(pady=15, ipady=10)

    login_button = ctk.CTkButton(frame,
                                 text="Login",
                                 width=400,
                                 corner_radius=10,
                                 font=("Arial", 18, 'bold'),
                                 )
    login_button.pack(pady=15, ipady=10)
    login_button.bind("<Button-1>",
                      lambda event: login(root, frame, username_entry.get(), password_entry.get(), warning_text))

    or_label = ctk.CTkLabel(frame,
                            text="or",
                            font=("Arial", 15, 'bold'),
                            )

    or_label.pack()

    register_button = ctk.CTkButton(frame,
                                    text="Register",
                                    fg_color="transparent",
                                    hover=False,
                                    )
    register_button.pack()
    register_button.bind("<Button-1>", lambda event: toggle(root, frame, "register"))

    warning_label = ctk.CTkLabel(frame, textvariable=warning_text, text_color="red", anchor="center")
    warning_label.pack()


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
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True)

    warning_text = ctk.StringVar()

    title = ctk.CTkLabel(frame,
                         text="Registration",
                         font=("Arial", 30, 'bold'),
                         text_color="white",
                         corner_radius=10,
                         width=400,
                         )
    title.pack(pady=15, ipady=10)

    username_entry = ctk.CTkEntry(frame,
                                  width=400,
                                  placeholder_text="Username",
                                  placeholder_text_color="grey",
                                  corner_radius=10
                                  )
    username_entry.pack(pady=15, ipady=10)

    fullname_entry = ctk.CTkEntry(frame,
                                  width=400,
                                  placeholder_text="Fullname",
                                  placeholder_text_color="grey",
                                  corner_radius=10
                                  )
    fullname_entry.pack(pady=15, ipady=10)

    email_entry = ctk.CTkEntry(frame,
                               width=400,
                               placeholder_text="Email",
                               placeholder_text_color="grey",
                               corner_radius=10
                               )
    email_entry.pack(pady=15, ipady=10)

    password_entry = ctk.CTkEntry(frame,
                                  width=400,
                                  placeholder_text="Password",
                                  placeholder_text_color="grey",
                                  corner_radius=10,
                                  show="*"
                                  )
    password_entry.pack(pady=15, ipady=10)

    confirm_password_entry = ctk.CTkEntry(frame,
                                          width=400,
                                          placeholder_text="Confirm Password",
                                          placeholder_text_color="grey",
                                          corner_radius=10,
                                          show="*"
                                          )
    confirm_password_entry.pack(pady=15, ipady=10)

    continue_button = ctk.CTkButton(frame,
                                    text="Continue",
                                    width=400,
                                    corner_radius=10,
                                    font=("Arial", 18, 'bold'),
                                    )
    continue_button.pack(pady=15, ipady=10)
    continue_button.bind("<Button-1>",
                         lambda event: register(root, frame, username_entry.get(), fullname_entry.get(),
                                                email_entry.get(), password_entry.get(), confirm_password_entry.get(),
                                                warning_text))

    or_label = ctk.CTkLabel(frame,
                            text="or",
                            font=("Arial", 15, 'bold'),
                            )

    or_label.pack()

    login_button = ctk.CTkButton(frame,
                                 text="Login",
                                 fg_color="transparent",
                                 hover=False,
                                 )
    login_button.pack()
    login_button.bind("<Button-1>", lambda event: toggle(root, frame, "login"))

    warning_label = ctk.CTkLabel(frame, textvariable=warning_text, text_color="red", anchor="center")
    warning_label.pack()


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
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True)

    welcome_label = ctk.CTkLabel(frame,
                                 text="Welcome",
                                 font=("Arial", 30, 'bold'),
                                 text_color="white",
                                 anchor="sw",
                                 height=40,
                                 width=190,
                                 )

    welcome_label.place(x=50, y=15)

    logout_button = ctk.CTkButton(frame,
                                  text="Logout",
                                  width=190,
                                  corner_radius=10,
                                  height=40,
                                  font=("Arial", 18, 'bold'),
                                  )
    logout_button.place(x=450, y=15, anchor="ne")
    logout_button.bind("<Button-1>", lambda event: toggle(root, frame, 'login'))

    create_class_button = ctk.CTkButton(frame,
                                        text="Create Class",
                                        width=190,
                                        corner_radius=10,
                                        height=40,
                                        font=("Arial", 18, 'bold'),
                                        )
    create_class_button.place(x=50, y=75)
    create_class_button.bind("<Button-1>", lambda event: toggle(root, frame, 'create_class'))

    take_attendance_button = ctk.CTkButton(frame,
                                           text="Take Attendance",
                                           width=190,
                                           corner_radius=10,
                                           height=40,
                                           font=("Arial", 18, 'bold'),
                                           )
    take_attendance_button.place(x=450, y=75, anchor="ne")
    take_attendance_button.bind("<Button-1>", lambda event: toggle(root, frame, 'take_attendance'))

    classes_label = ctk.CTkLabel(frame,
                                 text="Classes",
                                 font=("Arial", 20, 'bold'),
                                 text_color="white",
                                 fg_color="green",
                                 corner_radius=10,
                                 width=400,
                                 height=40,
                                 )
    classes_label.place(x=50, y=150)

    classes = getClassesByUsername(current_user["username"])

    classes_scrollbar = ScrollableLabelButtonFrame(root, frame, classes["data"].values(), command=goShowAttendanceUi,
                                                   width=380,
                                                   height=400)
    classes_scrollbar.place(x=50, y=215)

    for value in classes["data"].values():
        classes_scrollbar.add_item(value["class_name"])


def goShowAttendanceUi(root, frame, classes, index):
    global current_class
    current_class = list(classes)[index]
    print(current_class)
    toggle(root, frame, 'attendances')


def showCreateClassUi(root):
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True)
    warning_text = ctk.StringVar()

    im = Image.open("back-arrow.png")
    im = ctk.CTkImage(im)
    back_arrow = ctk.CTkButton(frame,
                               image=im,
                               fg_color="transparent",
                               width=50,
                               text=""
                               )
    back_arrow.place(x=50, y=30)
    back_arrow.bind("<Button-1>", lambda event: toggle(root, frame, 'main'))

    title = ctk.CTkLabel(frame,
                         text="Create Class",
                         font=("Arial", 30, 'bold'),
                         text_color="white",
                         corner_radius=10,
                         width=300,
                         )
    title.pack(pady=15, ipady=10)

    class_name_entry = ctk.CTkEntry(frame,
                                    width=400,
                                    placeholder_text="Class Name",
                                    placeholder_text_color="grey",
                                    corner_radius=10,
                                    )
    class_name_entry.pack(pady=15, ipady=10)

    class_code_entry = ctk.CTkEntry(frame,
                                    width=400,
                                    placeholder_text="Class Code",
                                    placeholder_text_color="grey",
                                    corner_radius=10,
                                    )
    class_code_entry.pack(pady=15, ipady=10)

    class_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    class_code_entry.insert(0, class_code)
    class_code_entry.configure(state=DISABLED)

    continue_button = ctk.CTkButton(frame,
                                    text="Continue",
                                    width=400,
                                    corner_radius=10,
                                    font=("Arial", 18, 'bold'),
                                    )
    continue_button.pack(pady=15, ipady=10)
    continue_button.bind("<Button-1>",
                         lambda event: createClass(root, frame, class_name_entry.get(), class_code_entry.get(),
                                                   warning_text))

    warning_label = ctk.CTkLabel(frame, textvariable=warning_text, text_color="red", anchor="center")
    warning_label.pack()


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
