from views import *

ctkRoot = ctk.CTk()
ctkRoot.title("Attendance Teacher")
ctkRoot.geometry("500x650")
ctkRoot.resizable(False, False)

showLoginUi(ctkRoot)
ctkRoot.mainloop()
