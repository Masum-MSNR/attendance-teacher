from views import *

ctkRoot = ctk.CTk()  # Create a root window using customtkinter class
ctkRoot.title("Attendance Teacher")  # Set title of the window
ctkRoot.geometry("500x650")  # Set size of the window
ctkRoot.resizable(False, False)  # Disable resizing of the window

showLoginUi(ctkRoot)
ctkRoot.mainloop()  # Start the mainloop of the window
