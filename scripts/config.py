"""Configuration management for Project Nightingale."""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, Optional

from .exceptions import ConfigurationError

logger = logging.getLogger(__name__)


class Config:
    """Configuration manager for Project Nightingale."""

    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize configuration manager.

        Args:
            config_file (Optional[str]): Path to configuration file.
        """
        self._config: Dict[str, Any] = {}
        self._config_file = config_file
        self._load_defaults()

        if config_file:
            self.load_from_file(config_file)

        # Load environment overrides
        self._load_from_environment()

    def _load_defaults(self) -> None:
        """Load default configuration values."""
        self._config = {
            "app": {"name": "Project Nightingale", "version": "1.0.0", "debug": False},
            "database": {
                "file": "project_nightingale.db",
                "timeout": 30,
                "backup": True,
            },
            "ai": {
                "model_timeout": 60,
                "max_input_length": 10000,
                "preprocessing": {"lowercase": True, "strip_whitespace": True},
            },
            "gui": {
                "window_size": "800x600",
                "theme": "default",
                "auto_clear_input": True,
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "file": None,
            },
            "performance": {
                "enable_profiling": False,
                "max_memory_usage": 1024,  # MB
                "cache_size": 100,
            },
        }

    def load_from_file(self, config_file: str) -> None:
        """
        Load configuration from JSON file.

        Args:
            config_file (str): Path to configuration file.

        Raises:
            ConfigurationError: If file cannot be loaded.
        """
        try:
            config_path = Path(config_file)
            if not config_path.exists():
                logger.warning(f"Configuration file not found: {config_file}")
                return

            with open(config_path, "r", encoding="utf-8") as f:
                file_config = json.load(f)

            # Merge with existing config
            self._merge_config(self._config, file_config)
            logger.info(f"Configuration loaded from {config_file}")

        except (json.JSONDecodeError, IOError) as e:
            raise ConfigurationError(
                f"Failed to load configuration from {config_file}: {str(e)}",
                config_key="file_load",
            ) from e

    def _load_from_environment(self) -> None:
        """Load configuration overrides from environment variables."""
        env_mapping = {
            "NIGHTINGALE_DEBUG": ("app", "debug", bool),
            "NIGHTINGALE_DB_FILE": ("database", "file", str),
            "NIGHTINGALE_LOG_LEVEL": ("logging", "level", str),
            "NIGHTINGALE_GUI_SIZE": ("gui", "window_size", str),
        }

        for env_var, (section, key, type_func) in env_mapping.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                try:
                    if type_func == bool:
                        value = env_value.lower() in ("true", "1", "yes", "on")
                    else:
                        value = type_func(env_value)

                    self._config[section][key] = value
                    logger.debug(f"Environment override: {env_var} = {value}")

                except (ValueError, KeyError) as e:
                    logger.warning(f"Invalid environment variable {env_var}: {e}")

    def _merge_config(self, base: Dict[str, Any], override: Dict[str, Any]) -> None:
        """
        Recursively merge configuration dictionaries.

        Args:
            base (Dict[str, Any]): Base configuration.
            override (Dict[str, Any]): Override configuration.
        """
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation.

        Args:
            key (str): Configuration key (e.g., "app.name" or "database.file").
            default (Any): Default value if key not found.

        Returns:
            Any: Configuration value.

        Example:
            >>> config = Config()
            >>> app_name = config.get("app.name")
            >>> debug_mode = config.get("app.debug", False)
        """
        keys = key.split(".")
        current = self._config

        try:
            for k in keys:
                current = current[k]
            return current
        except (KeyError, TypeError):
            if default is not None:
                return default
            raise ConfigurationError(
                f"Configuration key not found: {key}", config_key=key
            )

    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value using dot notation.

        Args:
            key (str): Configuration key.
            value (Any): Value to set.
        """
        keys = key.split(".")
        current = self._config

        # Navigate to parent dictionary
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        # Set the value
        current[keys[-1]] = value

    def save_to_file(self, config_file: str) -> None:
        """
        Save current configuration to file.

        Args:
            config_file (str): Path to save configuration.

        Raises:
            ConfigurationError: If file cannot be saved.
        """
        try:
            config_path = Path(config_file)
            config_path.parent.mkdir(parents=True, exist_ok=True)

            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(self._config, f, indent=2)

            logger.info(f"Configuration saved to {config_file}")

        except IOError as e:
            raise ConfigurationError(
                f"Failed to save configuration to {config_file}: {str(e)}",
                config_key="file_save",
            ) from e

    def validate(self) -> bool:
        """
        Validate current configuration.

        Returns:
            bool: True if configuration is valid.

        Raises:
            ConfigurationError: If configuration is invalid.
        """
        # Validate required sections
        required_sections = ["app", "database", "ai", "logging"]
        for section in required_sections:
            if section not in self._config:
                raise ConfigurationError(
                    f"Missing required configuration section: {section}",
                    config_key=section,
                )

        # Validate specific values
        if not isinstance(self.get("app.name"), str):
            raise ConfigurationError("app.name must be a string", config_key="app.name")

        if (
            not isinstance(self.get("database.timeout"), int)
            or self.get("database.timeout") <= 0
        ):
            raise ConfigurationError(
                "database.timeout must be a positive integer",
                config_key="database.timeout",
            )

        logger.info("Configuration validation passed")
        return True

    def to_dict(self) -> Dict[str, Any]:
        """
        Get configuration as dictionary.

        Returns:
            Dict[str, Any]: Complete configuration.
        """
        import copy

        return copy.deepcopy(self._config)


# Global configuration instance
_config_instance: Optional[Config] = None


def get_config() -> Config:
    """
    Get the global configuration instance.

    Returns:
        Config: Global configuration instance.
    """
    global _config_instance
    if _config_instance is None:
        # Look for config file in standard locations
        config_paths = [
            "config.json",
            "config/config.json",
            os.path.expanduser("~/.nightingale/config.json"),
            "/etc/nightingale/config.json",
        ]

        config_file = None
        for path in config_paths:
            if os.path.exists(path):
                config_file = path
                break

        _config_instance = Config(config_file)

    return _config_instance


def reset_config() -> None:
    """Reset the global configuration instance."""
    global _config_instance
    _config_instance = None
