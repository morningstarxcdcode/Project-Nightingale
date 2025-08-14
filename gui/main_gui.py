"""Main GUI application for Project Nightingale."""

import logging
import os
import sys
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from typing import Optional

from scripts.ai_model import simple_ai_model
from scripts.ai_utilities import preprocess_data
from scripts.config import get_config
from scripts.exceptions import DataValidationError, NightingaleError

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

logger = logging.getLogger(__name__)


class Application(tk.Tk):
    """Main GUI application class for Project Nightingale."""

    def __init__(self) -> None:
        """Initialize the GUI application."""
        super().__init__()

        try:
            # Load configuration
            self.config = get_config()

            # Setup window
            self.title(self.config.get("app.name", "Project Nightingale"))
            window_size = self.config.get("gui.window_size", "800x600")
            self.geometry(window_size)
            self.configure(bg="#f0f0f0")
            self.resizable(True, True)

            # Setup logging for GUI
            self._setup_gui_logging()

            # Create widgets
            self.create_widgets()

            # Setup event bindings
            self._setup_bindings()

            logger.info("GUI application initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize GUI: {e}")
            messagebox.showerror(
                "Initialization Error", f"Failed to initialize application: {str(e)}"
            )
            self.destroy()

    def _setup_gui_logging(self) -> None:
        """Setup logging specifically for GUI components."""
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

    def _setup_bindings(self) -> None:
        """Setup keyboard and event bindings."""
        # Bind Enter key to process input
        self.input_entry.bind("<Return>", lambda event: self.process_input())

        # Bind Ctrl+Enter to process input (alternative)
        self.bind("<Control-Return>", lambda event: self.process_input())

        # Bind Escape to clear input
        self.bind("<Escape>", lambda event: self.clear_input())

        # Bind Ctrl+L to clear results
        self.bind("<Control-l>", lambda event: self.clear_results())

    def create_widgets(self) -> None:
        """Create and arrange the GUI widgets."""
        # Main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header section
        self._create_header(main_frame)

        # Input section
        self._create_input_section(main_frame)

        # Control buttons
        self._create_control_buttons(main_frame)

        # Results section
        self._create_results_section(main_frame)

        # Status bar
        self._create_status_bar()

    def _create_header(self, parent: tk.Widget) -> None:
        """Create header section with title and description."""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))

        # Main title
        title_label = ttk.Label(
            header_frame,
            text="Welcome to Project Nightingale!",
            font=("Helvetica", 18, "bold"),
        )
        title_label.pack(pady=(0, 5))

        # Version info
        version = self.config.get("app.version", "1.0.0")
        version_label = ttk.Label(
            header_frame,
            text=f"Version {version}",
            font=("Helvetica", 9),
            foreground="gray",
        )
        version_label.pack()

        # Description
        desc_text = (
            "A health monitoring and prediction system using AI and machine learning"
        )
        desc_label = ttk.Label(
            header_frame,
            text=desc_text,
            font=("Helvetica", 12),
            foreground="#666666",
        )
        desc_label.pack(pady=(5, 0))

    def _create_input_section(self, parent: tk.Widget) -> None:
        """Create input section for health data."""
        input_frame = ttk.LabelFrame(parent, text="Health Data Input", padding=10)
        input_frame.pack(fill=tk.X, pady=(0, 10))

        # Input label with instructions
        input_text = (
            "Enter health data for AI analysis "
            "(e.g., 'heart rate: 72 bpm, temperature: 98.6°F'):"
        )
        input_label = ttk.Label(
            input_frame,
            text=input_text,
        )
        input_label.pack(anchor=tk.W, pady=(0, 5))

        # Input entry with validation
        self.input_entry = ttk.Entry(input_frame, font=("Consolas", 11))
        self.input_entry.pack(fill=tk.X, pady=(0, 10))

        # Character count label
        self.char_count_var = tk.StringVar()
        char_count_label = ttk.Label(
            input_frame,
            textvariable=self.char_count_var,
            font=("Helvetica", 9),
            foreground="gray",
        )
        char_count_label.pack(anchor=tk.E)

        # Bind to update character count
        self.input_entry.bind("<KeyRelease>", self._update_char_count)
        self._update_char_count()

    def _create_control_buttons(self, parent: tk.Widget) -> None:
        """Create control buttons for actions."""
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, pady=(0, 10))

        # Analyze button
        self.analyze_button = ttk.Button(
            button_frame,
            text="🔍 Analyze Data",
            command=self.process_input,
            style="Accent.TButton",
        )
        self.analyze_button.pack(side=tk.LEFT, padx=(0, 10))

        # Clear input button
        clear_input_btn = ttk.Button(
            button_frame, text="🗑️ Clear Input", command=self.clear_input
        )
        clear_input_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Clear results button
        clear_results_btn = ttk.Button(
            button_frame, text="📄 Clear Results", command=self.clear_results
        )
        clear_results_btn.pack(side=tk.LEFT)

        # Add progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            button_frame, variable=self.progress_var, mode="indeterminate"
        )
        self.progress_bar.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))

    def _create_results_section(self, parent: tk.Widget) -> None:
        """Create results display section."""
        results_frame = ttk.LabelFrame(parent, text="Analysis Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True)

        # Results text area with scrollbar
        self.result_text = scrolledtext.ScrolledText(
            results_frame,
            height=12,
            font=("Consolas", 10),
            wrap=tk.WORD,
            relief="sunken",
            borderwidth=1,
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # Configure text tags for styling
        self.result_text.tag_configure(
            "success", foreground="green", font=("Consolas", 10, "bold")
        )
        self.result_text.tag_configure(
            "error", foreground="red", font=("Consolas", 10, "bold")
        )
        self.result_text.tag_configure(
            "info", foreground="blue", font=("Consolas", 10, "italic")
        )

    def _create_status_bar(self) -> None:
        """Create status bar at bottom."""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")

        status_bar = ttk.Label(
            self,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Helvetica", 9),
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _update_char_count(self, event: Optional[tk.Event] = None) -> None:
        """Update character count display."""
        text = self.input_entry.get()
        count = len(text)
        max_length = self.config.get("ai.max_input_length", 10000)

        self.char_count_var.set(f"{count:,} / {max_length:,} characters")

        # Change color if approaching limit
        if count > max_length * 0.9:
            # Near limit - yellow warning
            pass  # Could add color styling here
        elif count > max_length:
            # Over limit - red warning
            pass  # Could add color styling here

    def set_status(self, message: str) -> None:
        """
        Update status bar message.

        Args:
            message (str): Status message to display.
        """
        self.status_var.set(message)
        self.update_idletasks()

    def show_progress(self, show: bool = True) -> None:
        """
        Show or hide progress indicator.

        Args:
            show (bool): Whether to show progress indicator.
        """
        if show:
            self.progress_bar.start(10)
            self.analyze_button.configure(state="disabled")
        else:
            self.progress_bar.stop()
            self.analyze_button.configure(state="normal")

    def clear_input(self) -> None:
        """Clear the input field."""
        self.input_entry.delete(0, tk.END)
        self._update_char_count()
        self.set_status("Input cleared")
        logger.debug("Input field cleared")

    def clear_results(self) -> None:
        """Clear the results display."""
        self.result_text.delete(1.0, tk.END)
        self.set_status("Results cleared")
        logger.debug("Results display cleared")

    def append_result(self, text: str, tag: Optional[str] = None) -> None:
        """
        Append text to results with optional styling.

        Args:
            text (str): Text to append.
            tag (Optional[str]): Style tag to apply.
        """
        self.result_text.insert(tk.END, text)
        if tag:
            # Apply tag to the newly inserted text
            start_index = self.result_text.index(f"end-{len(text)}c")
            end_index = self.result_text.index(tk.END)
            self.result_text.tag_add(tag, start_index, end_index)

        # Auto-scroll to bottom
        self.result_text.see(tk.END)

    def process_input(self) -> None:
        """Process the user input through the AI model."""
        input_data = self.input_entry.get().strip()

        if not input_data:
            messagebox.showwarning(
                "Input Error", "Please enter some health data to analyze."
            )
            self.input_entry.focus()
            return

        try:
            self.set_status("Processing data...")
            self.show_progress(True)

            # Clear previous results if auto-clear is enabled
            if self.config.get("gui.auto_clear_results", False):
                self.clear_results()

            # Log the analysis
            logger.info(f"Processing input: {input_data[:50]}...")

            # Add timestamp to results
            import datetime

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.append_result(f"\n{'='*60}\n", "info")
            self.append_result(f"Analysis started at {timestamp}\n", "info")
            self.append_result(f"Input: {input_data}\n\n", "info")

            # Preprocess the data
            self.set_status("Preprocessing data...")
            preprocessed_data = preprocess_data(input_data)
            self.append_result(f"Preprocessed: {preprocessed_data}\n\n")

            # Process with AI model
            self.set_status("Running AI analysis...")
            result = simple_ai_model(preprocessed_data)

            # Display success result
            self.append_result("✅ Analysis Result:\n", "success")
            self.append_result(f"{result}\n\n")

            # Clear input if auto-clear is enabled
            if self.config.get("gui.auto_clear_input", True):
                self.clear_input()

            self.set_status("Analysis completed successfully")
            logger.info("Analysis completed successfully")

        except DataValidationError as e:
            error_msg = f"❌ Data Validation Error: {e.message}\n\n"
            self.append_result(error_msg, "error")
            self.set_status("Data validation failed")
            logger.warning(f"Data validation error: {e.message}")

        except NightingaleError as e:
            error_msg = f"❌ Processing Error: {e.message}\n\n"
            self.append_result(error_msg, "error")
            self.set_status("Processing failed")
            logger.error(f"Processing error: {e.message}")

        except Exception as e:
            error_msg = f"❌ Unexpected Error: {str(e)}\n\n"
            self.append_result(error_msg, "error")
            self.set_status("Unexpected error occurred")
            logger.error(f"Unexpected error in GUI: {e}")
            messagebox.showerror(
                "Processing Error", f"An unexpected error occurred: {str(e)}"
            )

        finally:
            self.show_progress(False)


def main() -> int:
    """
    Main entry point for the GUI application.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    try:
        # Configure GUI logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

        logger.info("Starting GUI application...")

        app = Application()
        app.mainloop()

        logger.info("GUI application closed")
        return 0

    except ImportError as e:
        error_msg = f"GUI dependencies not available: {e}"
        print(error_msg)
        print(
            "Please install tkinter or run the console version with: python src/main.py"
        )
        logger.error(error_msg)
        return 1

    except Exception as e:
        error_msg = f"Error starting GUI: {e}"
        print(error_msg)
        logger.error(error_msg)
        return 1


if __name__ == "__main__":
    exit(main())
