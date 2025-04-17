import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Nightingale")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Add a welcome label with animation
        self.welcome_label = tk.Label(self, text="Welcome to Project Nightingale!", font=("Helvetica", 24), bg="#f0f0f0")
        self.welcome_label.pack(pady=20)

        # Add a button to start the application
        self.start_button = tk.Button(self, text="Start", command=self.start_application, bg="#4CAF50", fg="white", font=("Helvetica", 16))
        self.start_button.pack(pady=10)

    def start_application(self):
        messagebox.showinfo("Info", "Starting the application...")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
