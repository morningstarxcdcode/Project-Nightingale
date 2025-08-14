"""Tests for configuration management functionality."""

import pytest
import sys
import os
import json
import tempfile
from pathlib import Path
from unittest.mock import patch, mock_open

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.config import Config, get_config, reset_config
from scripts.exceptions import ConfigurationError


class TestConfig:
    """Test cases for configuration management."""
    
    def test_config_initialization(self) -> None:
        """Test Config class initialization with defaults."""
        config = Config()
        
        # Test default values
        assert config.get("app.name") == "Project Nightingale"
        assert config.get("app.version") == "1.0.0"
        assert config.get("app.debug") is False
        assert config.get("database.file") == "project_nightingale.db"
        assert config.get("database.timeout") == 30
        assert config.get("ai.model_timeout") == 60
        assert config.get("gui.window_size") == "800x600"
    
    def test_config_get_with_dot_notation(self) -> None:
        """Test getting configuration values with dot notation."""
        config = Config()
        
        # Test nested access
        assert config.get("app.name") == "Project Nightingale"
        assert config.get("database.timeout") == 30
        assert config.get("ai.preprocessing.lowercase") is True
        
        # Test with default values
        assert config.get("nonexistent.key", "default") == "default"
        assert config.get("app.nonexistent", 999) == 999
    
    def test_config_set_with_dot_notation(self) -> None:
        """Test setting configuration values with dot notation."""
        config = Config()
        
        # Set existing value
        config.set("app.name", "Modified Name")
        assert config.get("app.name") == "Modified Name"
        
        # Set new nested value
        config.set("new.section.key", "new_value")
        assert config.get("new.section.key") == "new_value"
        
        # Set deep nested value
        config.set("deep.nested.very.deep.key", 42)
        assert config.get("deep.nested.very.deep.key") == 42
    
    def test_config_load_from_file(self) -> None:
        """Test loading configuration from JSON file."""
        test_config = {
            "app": {
                "name": "Test App",
                "debug": True
            },
            "database": {
                "timeout": 60
            }
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_config, f)
            config_file = f.name
        
        try:
            config = Config(config_file)
            
            # Test that file values override defaults
            assert config.get("app.name") == "Test App"
            assert config.get("app.debug") is True
            assert config.get("database.timeout") == 60
            
            # Test that non-overridden defaults remain
            assert config.get("app.version") == "1.0.0"
            assert config.get("database.file") == "project_nightingale.db"
            
        finally:
            os.unlink(config_file)
    
    def test_config_load_from_nonexistent_file(self) -> None:
        """Test loading from non-existent file doesn't fail."""
        config = Config("nonexistent_file.json")
        
        # Should have default values
        assert config.get("app.name") == "Project Nightingale"
    
    def test_config_load_invalid_json(self) -> None:
        """Test loading invalid JSON raises ConfigurationError."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("invalid json content {")
            config_file = f.name
        
        try:
            with pytest.raises(ConfigurationError) as exc_info:
                Config(config_file)
            assert "Failed to load configuration" in str(exc_info.value)
            
        finally:
            os.unlink(config_file)
    
    def test_config_environment_overrides(self) -> None:
        """Test environment variable overrides."""
        env_vars = {
            "NIGHTINGALE_DEBUG": "true",
            "NIGHTINGALE_DB_FILE": "custom.db",
            "NIGHTINGALE_LOG_LEVEL": "DEBUG",
            "NIGHTINGALE_GUI_SIZE": "1024x768"
        }
        
        with patch.dict(os.environ, env_vars):
            config = Config()
            
            assert config.get("app.debug") is True
            assert config.get("database.file") == "custom.db"
            assert config.get("logging.level") == "DEBUG"
            assert config.get("gui.window_size") == "1024x768"
    
    def test_config_environment_boolean_parsing(self) -> None:
        """Test boolean parsing from environment variables."""
        test_cases = [
            ("true", True),
            ("1", True),
            ("yes", True),
            ("on", True),
            ("false", False),
            ("0", False),
            ("no", False),
            ("off", False),
        ]
        
        for env_value, expected in test_cases:
            with patch.dict(os.environ, {"NIGHTINGALE_DEBUG": env_value}):
                config = Config()
                assert config.get("app.debug") is expected
    
    def test_config_save_to_file(self) -> None:
        """Test saving configuration to file."""
        config = Config()
        config.set("app.name", "Saved App")
        config.set("custom.key", "custom_value")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            config_file = f.name
        
        try:
            config.save_to_file(config_file)
            
            # Load and verify
            with open(config_file, 'r') as f:
                saved_config = json.load(f)
            
            assert saved_config["app"]["name"] == "Saved App"
            assert saved_config["custom"]["key"] == "custom_value"
            
        finally:
            os.unlink(config_file)
    
    def test_config_validation(self) -> None:
        """Test configuration validation."""
        config = Config()
        
        # Valid configuration should pass
        assert config.validate() is True
        
        # Test invalid app name
        config.set("app.name", 123)
        with pytest.raises(ConfigurationError) as exc_info:
            config.validate()
        assert "app.name must be a string" in str(exc_info.value)
        
        # Reset and test invalid timeout
        config = Config()
        config.set("database.timeout", -1)
        with pytest.raises(ConfigurationError) as exc_info:
            config.validate()
        assert "must be a positive integer" in str(exc_info.value)
    
    def test_config_missing_key_error(self) -> None:
        """Test error when accessing non-existent key without default."""
        config = Config()
        
        with pytest.raises(ConfigurationError) as exc_info:
            config.get("nonexistent.key.path")
        assert "Configuration key not found" in str(exc_info.value)
    
    def test_config_to_dict(self) -> None:
        """Test converting configuration to dictionary."""
        config = Config()
        config.set("custom.key", "value")
        
        config_dict = config.to_dict()
        
        assert isinstance(config_dict, dict)
        assert config_dict["app"]["name"] == "Project Nightingale"
        assert config_dict["custom"]["key"] == "value"
        
        # Ensure it's a copy, not reference
        config_dict["app"]["name"] = "Modified"
        assert config.get("app.name") == "Project Nightingale"
    
    def test_global_config_instance(self) -> None:
        """Test global configuration instance management."""
        # Reset to ensure clean state
        reset_config()
        
        # Get config instances
        config1 = get_config()
        config2 = get_config()
        
        # Should be the same instance
        assert config1 is config2
        
        # Modify through one instance
        config1.set("test.key", "test_value")
        assert config2.get("test.key") == "test_value"
        
        # Reset and verify new instance
        reset_config()
        config3 = get_config()
        assert config3 is not config1
        
        # Should not have the test key
        assert config3.get("test.key", "default") == "default"
    
    def test_config_merge_behavior(self) -> None:
        """Test configuration merging behavior."""
        # Create base config
        base_config = {
            "app": {
                "name": "Base App",
                "version": "1.0.0",
                "debug": False
            },
            "database": {
                "file": "base.db"
            }
        }
        
        # Create override config
        override_config = {
            "app": {
                "name": "Override App",
                "debug": True,
                "new_key": "new_value"
            },
            "new_section": {
                "key": "value"
            }
        }
        
        config = Config()
        config._config = base_config.copy()
        config._merge_config(config._config, override_config)
        
        # Test merged values
        assert config.get("app.name") == "Override App"  # Overridden
        assert config.get("app.version") == "1.0.0"  # Preserved
        assert config.get("app.debug") is True  # Overridden
        assert config.get("app.new_key") == "new_value"  # Added
        assert config.get("database.file") == "base.db"  # Preserved
        assert config.get("new_section.key") == "value"  # Added
    
    @pytest.mark.parametrize("invalid_data,expected_error", [
        (123, "must be a string"),
        ([], "must be a string"),
        ({}, "must be a string"),
        (None, "must be a string"),
    ])
    def test_config_invalid_app_name_types(self, invalid_data: any, expected_error: str) -> None:
        """Test validation with various invalid app name types."""
        config = Config()
        config.set("app.name", invalid_data)
        
        with pytest.raises(ConfigurationError) as exc_info:
            config.validate()
        assert expected_error in str(exc_info.value)
    
    def test_config_file_search_order(self) -> None:
        """Test configuration file search order."""
        # Create a temporary config file for testing
        test_config = {"app": {"name": "Found Config"}}
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_config, f)
            config_file = f.name
        
        try:
            # Test loading with explicit file path
            reset_config()
            config = Config(config_file)
            
            # Should have found and loaded the config
            assert config.get("app.name") == "Found Config"
            
        finally:
            os.unlink(config_file)
    
    def test_config_deep_nesting(self) -> None:
        """Test deeply nested configuration access."""
        config = Config()
        
        # Set deeply nested value
        config.set("level1.level2.level3.level4.key", "deep_value")
        
        # Retrieve deeply nested value
        assert config.get("level1.level2.level3.level4.key") == "deep_value"
        
        # Test partial path access
        level3_dict = config.get("level1.level2.level3")
        assert isinstance(level3_dict, dict)
        assert level3_dict["level4"]["key"] == "deep_value"