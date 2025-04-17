import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import sys
import os
import subprocess

# Add the scripts directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))

from networking import fetch_data_from_api

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

        # New features
        self.theme_button = tk.Button(self, text="Change Theme", command=self.change_theme, bg="#FFC107", fg="black")
        self.theme_button.pack(pady=10)

        self.save_button = tk.Button(self, text="Save Results", command=self.save_results, bg="#17A2B8", fg="white")
        self.save_button.pack(pady=10)

        self.clear_button = tk.Button(self, text="Clear Results", command=self.clear_results, bg="#DC3545", fg="white")
        self.clear_button.pack(pady=10)

        self.feedback_button = tk.Button(self, text="Feedback", command=self.get_feedback, bg="#6F42C1", fg="white")
        self.feedback_button.pack(pady=10)

    def submit_name(self):
        name = self.name_entry.get()
        messagebox.showinfo("Hello", f"Hello, {name}!")

    def run_tests(self):
        # Run the tests and capture the output
        result = subprocess.run(['python3', '-m', 'unittest', 'discover', 'tests'], capture_output=True, text=True)
        self.result_label.config(text=result.stdout)

    def change_theme(self):
        # Change the theme of the application
        theme = simpledialog.askstring("Theme Selection", "Enter theme (light/dark):")
        if theme == "dark":
            self.configure(bg="#333")
            self.welcome_label.configure(bg="#333", fg="#FFF")
            self.result_label.configure(bg="#333", fg="#FFF")
        else:
            self.configure(bg="#f0f0f0")
            self.welcome_label.configure(bg="#f0f0f0", fg="#000")
            self.result_label.configure(bg="#f0f0f0", fg="#000")

    def save_results(self):
        # Save the results to a file
        results = self.result_label.cget("text")
        if results:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            with open(file_path, 'w') as file:
                file.write(results)
            messagebox.showinfo("Success", "Results saved successfully!")

    def clear_results(self):
        # Clear the displayed results
        self.result_label.config(text="")

    def get_feedback(self):
        # Get user feedback
        feedback = simpledialog.askstring("Feedback", "Please provide your feedback:")
        if feedback:
            messagebox.showinfo("Thank You", "Your feedback has been received!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
