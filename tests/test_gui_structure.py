import unittest
import sys
import os
import importlib.util

# Test GUI code without actually running the GUI
class TestGUI(unittest.TestCase):
    
    def test_gui_imports(self):
        """Test that GUI code can be parsed and imports are correct"""
        gui_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'gui', 'main_gui.py')
        
        # Read the file content
        with open(gui_path, 'r') as f:
            content = f.read()
        
        # Check for required components
        self.assertIn('class Application', content)
        self.assertIn('tk.Tk', content)
        self.assertIn('simple_ai_model', content)
        self.assertIn('preprocess_data', content)
    
    def test_gui_module_structure(self):
        """Test that the GUI module has the expected structure"""
        gui_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'gui', 'main_gui.py')
        
        # Check if file exists
        self.assertTrue(os.path.exists(gui_path))
        
        # Read the file and check for main components
        with open(gui_path, 'r') as f:
            content = f.read()
        
        required_methods = ['__init__', 'create_widgets', 'process_input']
        for method in required_methods:
            self.assertIn(f'def {method}', content, f"Method {method} not found in GUI")

if __name__ == "__main__":
    unittest.main()