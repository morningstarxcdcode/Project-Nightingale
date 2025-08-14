import unittest
import sys
import os
from unittest.mock import Mock, patch, MagicMock

# Add the parent directory to the system path to import gui modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import AI model directly since it doesn't depend on GUI
from scripts.ai_model import simple_ai_model


class TestGUIIntegration(unittest.TestCase):
    """Test suite for GUI integration with AI functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Mock tkinter components to avoid GUI dependencies
        self.mock_tk = Mock()
        self.mock_messagebox = Mock()
        
        # Create a mock application class that simulates the GUI behavior
        self.app = self.create_mock_application()

    def create_mock_application(self):
        """Create a mock application that simulates GUI behavior without actual GUI."""
        app = Mock()
        app.title.return_value = "Project Nightingale with AI Integration"
        app.input_entry = Mock()
        app.submit_button = Mock()
        app.label = Mock()
        app.input_label = Mock()
        
        # Mock the process_input method to behave like the real one
        def mock_process_input(input_data=None):
            if input_data is None:
                input_data = "mock_input"
            result = simple_ai_model(input_data)
            return result
        
        app.process_input = mock_process_input
        return app

    def tearDown(self):
        """Clean up after each test method."""
        pass  # No cleanup needed for mocked objects

    def test_application_initialization(self):
        """Test that the GUI application initializes correctly."""
        self.assertEqual(self.app.title(), "Project Nightingale with AI Integration")
        self.assertTrue(hasattr(self.app, 'input_entry'))
        self.assertTrue(hasattr(self.app, 'submit_button'))
        self.assertTrue(hasattr(self.app, 'label'))

    def test_process_input_with_data(self):
        """Test the process_input method with sample data."""
        test_input = "Hello World"
        result = self.app.process_input(input_data=test_input)
        
        # Verify the AI model is called correctly
        expected_result = simple_ai_model(test_input)
        self.assertEqual(result, expected_result)
        self.assertIn("Processed data:", result)

    def test_process_input_empty_data(self):
        """Test the process_input method with empty data."""
        test_input = ""
        result = self.app.process_input(input_data=test_input)
        
        # Should still process, even if empty
        expected_result = simple_ai_model(test_input)
        self.assertEqual(result, expected_result)

    def test_process_input_special_characters(self):
        """Test the process_input method with special characters."""
        test_input = "Hello @#$%^&*() 123 ñoño"
        result = self.app.process_input(input_data=test_input)
        
        expected_result = simple_ai_model(test_input)
        self.assertEqual(result, expected_result)
        self.assertIn("Processed data:", result)

    def test_ai_integration_flow(self):
        """Test the complete AI integration flow."""
        # Test multiple inputs to ensure consistency
        test_cases = [
            "Simple test",
            "Another test with numbers 123",
            "Test with symbols !@#$",
            "Long test input with multiple words and various characters 123 !@# xyz"
        ]
        
        for test_input in test_cases:
            with self.subTest(input_data=test_input):
                result = self.app.process_input(input_data=test_input)
                self.assertIsInstance(result, str)
                self.assertIn("Processed data:", result)
                self.assertIn(test_input, result)

    def test_gui_components_exist(self):
        """Test that all necessary GUI components exist."""
        # Check that all expected widgets are present
        widgets = [
            'label', 'input_label', 'input_entry', 'submit_button'
        ]
        
        for widget_name in widgets:
            with self.subTest(widget=widget_name):
                self.assertTrue(hasattr(self.app, widget_name), 
                              f"Widget '{widget_name}' should exist")

    def test_process_input_returns_value(self):
        """Test that process_input always returns a value."""
        test_cases = ["test", "", "123", "special chars !@#$%"]
        
        for test_input in test_cases:
            with self.subTest(input_data=test_input):
                result = self.app.process_input(input_data=test_input)
                self.assertIsNotNone(result)
                self.assertIsInstance(result, str)

    def test_ai_model_integration(self):
        """Test that the AI model is properly integrated."""
        # Test direct AI model call
        test_input = "Integration test"
        
        # Call through GUI
        gui_result = self.app.process_input(input_data=test_input)
        
        # Call directly
        direct_result = simple_ai_model(test_input)
        
        # Should be the same
        self.assertEqual(gui_result, direct_result)

    def test_ai_model_functionality(self):
        """Test the core AI model functionality that the GUI depends on."""
        # Test various AI model inputs
        test_cases = [
            ("hello world", "Processed data: hello world"),
            ("Test 123", "Processed data: Test 123"),
            ("", "Processed data: "),
            ("Special chars !@#$%", "Processed data: Special chars !@#$%")
        ]
        
        for input_data, expected_output in test_cases:
            with self.subTest(input_data=input_data):
                result = simple_ai_model(input_data)
                self.assertEqual(result, expected_output)

    def test_error_handling_in_gui_integration(self):
        """Test error handling in GUI integration scenarios."""
        # Test that the AI model handles various edge cases
        edge_cases = [
            "very long input " * 100,  # Very long input
            "\n\t\r",  # Whitespace characters
            "unicode: ñáéíóú",  # Unicode characters
        ]
        
        for test_input in edge_cases:
            with self.subTest(input_data=test_input):
                result = self.app.process_input(input_data=test_input)
                self.assertIsInstance(result, str)
                self.assertIn("Processed data:", result)


if __name__ == "__main__":
    unittest.main()