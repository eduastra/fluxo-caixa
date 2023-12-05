import tkinter as tk
from UI import Application

def run():
    app = tk.Tk()
    app.title("Adega Olaria System")
    Application(app)
    app.geometry("1280x720")
    app.mainloop()

