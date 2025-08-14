"""Integration tests for GUI functionality."""

import os
import sys
from unittest.mock import patch

import pytest

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Try to import tkinter, skip tests if not available
tkinter = None
try:
    import tkinter  # noqa: F401

    from gui.main_gui import Application

    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    Application = None

pytestmark = pytest.mark.skipif(not TKINTER_AVAILABLE, reason="tkinter not available")


class TestGUIIntegration:
    """Test cases for GUI integration."""

    @pytest.mark.gui
    def test_application_initialization(self) -> None:
        """Test that the GUI application can be initialized."""
        if not TKINTER_AVAILABLE:
            pytest.skip("tkinter not available")

        with patch("gui.main_gui.tk.Tk.__init__") as mock_init:
            mock_init.return_value = None

            with patch("gui.main_gui.Application.create_widgets"):
                app = Application()
                assert app is not None

    @pytest.mark.gui
    def test_gui_imports(self) -> None:
        """Test that GUI imports work correctly."""
        if not TKINTER_AVAILABLE:
            pytest.skip("tkinter not available")

        # Test that we can import the GUI module
        from gui.main_gui import Application, main

        assert Application is not None
        assert main is not None

    @pytest.mark.gui
    def test_gui_main_function(self) -> None:
        """Test the main GUI function handles missing tkinter gracefully."""
        # This test can run even without tkinter
        from gui.main_gui import main

        with patch("gui.main_gui.Application") as mock_app:
            if not TKINTER_AVAILABLE:
                # Should handle ImportError gracefully
                with patch("builtins.print") as mock_print:
                    result = main()
                    assert result == 1  # Error code
                    mock_print.assert_called()
            else:
                mock_app.return_value.mainloop.return_value = None
                result = main()
                assert result == 0  # Success code
