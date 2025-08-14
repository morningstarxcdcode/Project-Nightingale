# Main GUI application for Project Nightingale

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from scripts.ai_model import simple_ai_model
from scripts.ai_utilities import preprocess_data

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Nightingale")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the GUI widgets."""
        # Main title
        self.label = tk.Label(
            self, 
            text="Welcome to Project Nightingale!", 
            font=("Helvetica", 16),
            bg="#f0f0f0"
        )
        self.label.pack(pady=20)

        # Description
        self.desc_label = tk.Label(
            self,
            text="A health monitoring and prediction system",
            font=("Helvetica", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        self.desc_label.pack(pady=5)

        # Input section
        self.input_label = tk.Label(
            self, 
            text="Enter health data for AI analysis:",
            bg="#f0f0f0"
        )
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(self, width=50)
        self.input_entry.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(
            self, 
            text="Analyze Data", 
            command=self.process_input,
            bg="#007BFF",
            fg="white",
            padx=20,
            pady=5
        )
        self.submit_button.pack(pady=20)

        # Result display
        self.result_text = tk.Text(
            self,
            height=10,
            width=80,
            bg="white",
            relief="sunken",
            borderwidth=2
        )
        self.result_text.pack(pady=20, padx=20, fill="both", expand=True)

    def process_input(self):
        """Process the user input through the AI model."""
        input_data = self.input_entry.get()
        
        if not input_data.strip():
            messagebox.showwarning("Input Error", "Please enter some data to analyze.")
            return
        
        try:
            # Preprocess the data
            preprocessed_data = preprocess_data(input_data)
            
            # Process with AI model
            result = simple_ai_model(preprocessed_data)
            
            # Display result
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, f"Analysis Result:\n\n{result}\n\nInput: {input_data}")
            
            # Clear input
            self.input_entry.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Processing Error", f"An error occurred: {str(e)}")

def main():
    """Main entry point for the GUI application."""
    try:
        app = Application()
        app.mainloop()
    except ImportError as e:
        print(f"GUI dependencies not available: {e}")
        print("Please install tkinter or run the console version with: python src/main.py")
        return 1
    except Exception as e:
        print(f"Error starting GUI: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
