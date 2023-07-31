from tkinter import *
from tkinter.ttk import *
from views import *
from repo import *

root = Tk()
root.geometry("650x450")
root.title("Attendance Teacher")
root.configure(background="#fff")
root.resizable(False, False)

style = Style()
style.configure("TLabel", font=("Helvetica", 20, 'bold'), background="#fff")
style.configure("TSLabel.TLabel", font=("Helvetica", 16), background="#fff")
style.configure("Warning.TLabel", font=("Helvetica", 10), background="#fff", foreground="red")
style.configure("TEntry", font=("Helvetica", 20), background="#000")
style.configure("TButton", font=("Helvetica", 18, 'bold'), background="#ccc")
style.configure("TFrame", background="#fff", borderwidth=2, relief="flat", bordercolor="#fff")

showLoginUi(root)

root.mainloop()
