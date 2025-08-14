import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import os

# Add the scripts directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from ai_model import simple_ai_model  # Importing the AI model

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Nightingale with AI Integration")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Project Nightingale with AI Integration!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.input_label = tk.Label(self, text="Enter data for AI model:")
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(self)
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.process_input)
        self.submit_button.pack(pady=20)

    def process_input(self, input_data=None):
        """Process input data with AI model. Can be called with input_data parameter for testing."""
        if input_data is None:
            input_data = self.input_entry.get()
        result = simple_ai_model(input_data)  # Call the AI model
        if hasattr(self, 'input_entry'):  # Only show messagebox if GUI is properly initialized
            messagebox.showinfo("AI Result", result)  # Display the result
        return result

if __name__ == "__main__":
    app = Application()
    app.mainloop()
