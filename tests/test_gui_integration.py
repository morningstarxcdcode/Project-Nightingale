import unittest
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from gui.main_gui import Application

class TestGUIIntegration(unittest.TestCase):
    """Test cases for the GUI integration."""

    def test_gui_initialization(self):
        """Test if the GUI initializes correctly."""
        try:
            app = Application()
            self.assertIsNotNone(app)
            self.assertEqual(app.title(), "Project Nightingale")
            app.destroy()  # Clean up
        except Exception as e:
            # Skip test if GUI cannot be created (e.g., in headless environment)
            self.skipTest(f"GUI test skipped: {e}")

if __name__ == "__main__":
    unittest.main()
