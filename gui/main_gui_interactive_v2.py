import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the scripts directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))

from networking.networking import fetch_data_from_api
import unittest
import subprocess

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

        # Test execution buttons
        self.test_button = tk.Button(self, text="Run Tests", command=self.run_tests, bg="#28a745", fg="white")
        self.test_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", bg="#f0f0f0")
        self.result_label.pack(pady=20)

    def submit_name(self):
        name = self.name_entry.get()
        messagebox.showinfo("Hello", f"Hello, {name}!")

    def run_tests(self):
        # Run the tests and capture the output
        result = subprocess.run(['python3', '-m', 'unittest', 'discover', 'tests'], capture_output=True, text=True)
        self.result_label.config(text=result.stdout)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
