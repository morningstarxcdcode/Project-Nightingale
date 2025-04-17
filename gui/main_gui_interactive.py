import tkinter as tk
from tkinter import messagebox
from scripts.networking import fetch_data_from_api

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Nightingale")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Add a welcome label with animation
        self.welcome_label = tk.Label(self, text="Welcome to Project Nightingale!", font=("Helvetica", 24), bg="#f0f0f0")
        self.welcome_label.pack(pady=20)

        # User input form
        self.input_label = tk.Label(self, text="Enter your name:", bg="#f0f0f0")
        self.input_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_name, bg="#007BFF", fg="white")
        self.submit_button.pack(pady=10)

    def submit_name(self):
        name = self.name_entry.get()
        messagebox.showinfo("Hello", f"Hello, {name}!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
