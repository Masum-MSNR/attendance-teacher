import customtkinter as ctk


# This is a custom class that inherits from ctk.CTkScrollableFrame class
# This class is used to create a scrollable frame with a label and a button
class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, root, master, classes, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.root = root
        self.frame = master
        self.classes = classes
        self.command = command
        self.label_list = []
        self.button_list = []
        self.code_list = []

    def add_item(self, item, item2):
        label = ctk.CTkLabel(self, text=item, compound="left", padx=5, anchor="w")
        code = ctk.CTkLabel(self, text=item2, compound="left", padx=5, anchor="w")
        button = ctk.CTkButton(self, text="View Attendance", height=24)
        if self.command is not None:
            button.configure(
                command=lambda: self.command(self.root, self.frame, self.classes, self.label_list.index(label)))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        code.grid(row=len(self.code_list), column=1, pady=(0, 10), padx=5)
        button.grid(row=len(self.button_list), column=2, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)
        self.code_list.append(code)


# This is a custom class that inherits from ctk.CTkScrollableFrame class
# This class is used to create a scrollable frame with a button
class ScrollableButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, root, master, classes, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.root = root
        self.frame = master
        self.classes = classes
        self.command = command
        self.button_list = []

    def add_item(self, item):
        button = ctk.CTkButton(self, text=item, height=30, fg_color="transparent")
        if self.command is not None:
            button.configure(
                command=lambda: self.command(self.root, self.frame, self.classes, self.button_list.index(button)))
        button.pack(fill="x", pady=5, padx=5)
        self.button_list.append(button)


# This is a custom class that inherits from ctk.CTkScrollableFrame class
# This class is used to create a scrollable frame with a label
class ScrollableLabelFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.label_list = []

    def add_item(self, item):
        label = ctk.CTkLabel(self, text=item, height=30, text_color="white")
        label.pack(fill="x", pady=5, padx=5)
        self.label_list.append(label)


# This is a custom class that inherits from ctk.CTkScrollableFrame class
# This class is used to create a scrollable frame with a label with click event
class ScrollableLabelFrame2(ctk.CTkScrollableFrame):
    def __init__(self, root, master, data, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.root = root
        self.frame = master
        self.command = command
        self.data = data
        self.label_list = []

    def add_item(self, item):
        label = ctk.CTkLabel(self, text=item, height=30, text_color="white")
        label.pack(fill="x", pady=5, padx=5)
        label.bind("<Button-1>",
                   lambda event: self.command(self.root, self.frame, self.data, self.label_list.index(label)))
        self.label_list.append(label)
