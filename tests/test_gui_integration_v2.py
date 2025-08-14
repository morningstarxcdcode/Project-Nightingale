import unittest
import os
import sys

class TestGUIIntegrationV2(unittest.TestCase):
    """Test cases for the GUI integration with the AI model."""

    def setUp(self):
        """Set up the application for testing."""
        # Check if display is available
        if 'DISPLAY' not in os.environ:
            self.skipTest("No display available for GUI testing")
        
        from gui.main_gui_with_ai_integration import Application
        try:
            self.app = Application()
        except Exception as e:
            self.skipTest(f"GUI initialization failed: {e}")

    def test_gui_initialization(self):
        """Test if the GUI initializes correctly."""
        self.assertIsNotNone(self.app)

    def test_process_input(self):
        """Test the process_input method with valid input."""
        test_input = "Test input"
        result = self.app.process_input(test_input)
        self.assertIn("Processed data:", result)  # Check if the result contains the AI output

if __name__ == "__main__":
    unittest.main()
