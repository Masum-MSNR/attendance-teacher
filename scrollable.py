import customtkinter as ctk


class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, root, master, classes, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.root = root
        self.frame = master
        self.classes = classes
        self.command = command
        self.radiobutton_variable = ctk.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item):
        label = ctk.CTkLabel(self, text=item, compound="left", padx=5, anchor="w")
        button = ctk.CTkButton(self, text="View Attendance", height=24)
        if self.command is not None:
            button.configure(
                command=lambda: self.command(self.root, self.frame, self.classes, self.label_list.index(label)))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)
