# Main GUI application for Project Nightingale

import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.ai_model import simple_ai_model
from scripts.ai_utilities import preprocess_data

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Nightingale")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Project Nightingale!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.input_label = tk.Label(self, text="Enter data for AI model:")
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(self, width=50)
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Process with AI", command=self.process_input)
        self.submit_button.pack(pady=20)
        
        # Result display area
        self.result_label = tk.Label(self, text="AI Result will appear here:", font=("Helvetica", 12))
        self.result_label.pack(pady=10)
        
        self.result_text = tk.Text(self, height=10, width=60)
        self.result_text.pack(pady=10)

    def process_input(self):
        input_data = self.input_entry.get()
        if not input_data.strip():
            messagebox.showwarning("Warning", "Please enter some data!")
            return
        
        try:
            # Preprocess the data
            processed_data = preprocess_data(input_data)
            
            # Run through AI model
            ai_result = simple_ai_model(processed_data)
            
            # Display results
            result_text = f"Original Input: {input_data}\n"
            result_text += f"Processed Input: {processed_data}\n"
            result_text += f"AI Result: {ai_result}\n"
            result_text += "-" * 50 + "\n"
            
            self.result_text.insert(tk.END, result_text)
            self.result_text.see(tk.END)
            
            # Clear input
            self.input_entry.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
