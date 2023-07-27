from tkinter import *
from tkinter.ttk import *
from views import *

# Create the root window
root = Tk()
root.geometry("600x400")
root.title("Attendance Teacher")
root.configure(background="#fff")
root.resizable(False, False)

style = Style()
style.configure("TLabel", font=("Helvetica", 20, 'bold'), background="#fff")
style.configure("TSLabel.TLabel", font=("Helvetica", 16), background="#fff")
style.configure("TEntry", font=("Helvetica", 20), background="#fff")
style.configure("TButton", font=("Helvetica", 18, 'bold'), background="#ccc")
style.configure("TFrame", background="#fff", borderwidth=2, relief="flat",bordercolor="#fff")

showLoginUi(root)

root.mainloop()
