#!/usr/bin/env python3
"""
Centralized Error Handler for Slidev PPT Creator
Provides consistent error handling, logging, and recovery mechanisms.
"""

import logging
import sys
import os
import traceback
from typing import Dict, Any, Optional, Callable
from functools import wraps
from pathlib import Path

class SlidevError(Exception):
    """Base exception for Slidev PPT Creator errors."""

    def __init__(self, message: str, error_code: str = None, context: Dict[str, Any] = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.context = context or {}

class TemplateError(SlidevError):
    """Template-related errors."""

class ChartError(SlidevError):
    """Chart generation errors."""

class ValidationError(SlidevError):
    """Validation errors."""

class ContentError(SlidevError):
    """Content analysis errors."""

class ErrorHandler:
    """Centralized error handling and logging."""

    def __init__(self, log_file: str = None):
        self.setup_logging(log_file)
        self.error_counts = {}
        self.recovery_strategies = {}

    def setup_logging(self, log_file: str = None):
        """Setup logging configuration."""
        # Create logs directory if it doesn't exist
        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler(log_file or 'slidev_errors.log') if log_file else logging.NullHandler()
            ]
        )
        self.logger = logging.getLogger('SlidevPPTCreator')

    def log_error(self, error: Exception, context: Dict[str, Any] = None):
        """Log error with context."""
        error_type = type(error).__name__
        self.error_counts[error_type] = self.error_counts.get(error_type, 0) + 1

        error_info = {
            'type': error_type,
            'message': str(error),
            'context': context,
            'count': self.error_counts[error_type]
        }

        if hasattr(error, 'error_code'):
            error_info['error_code'] = error.error_code

        self.logger.error(f"Error occurred: {error_info}")

        # Log full traceback for debugging
        self.logger.debug(traceback.format_exc())

    def handle_error(self, error: Exception, fallback_result: Any = None,
                    context: Dict[str, Any] = None) -> Any:
        """Handle error with optional fallback and recovery."""
        self.log_error(error, context)

        # Try recovery strategy if available
        error_type = type(error).__name__
        if error_type in self.recovery_strategies:
            try:
                return self.recovery_strategies[error_type](error, context)
            except Exception as recovery_error:
                self.logger.error(f"Recovery strategy failed: {recovery_error}")

        # Return fallback result if provided
        if fallback_result is not None:
            self.logger.info(f"Using fallback result for {error_type}")
            return fallback_result

        # Re-raise if no fallback available
        raise error

    def register_recovery_strategy(self, error_type: type, strategy: Callable):
        """Register a recovery strategy for an error type."""
        self.recovery_strategies[error_type.__name__] = strategy

    def get_error_summary(self) -> Dict[str, Any]:
        """Get summary of all errors encountered."""
        return {
            'total_errors': sum(self.error_counts.values()),
            'error_counts': self.error_counts.copy(),
            'error_types': list(self.error_counts.keys())
        }

# Global error handler instance
error_handler = ErrorHandler()

def handle_slidev_errors(fallback_result: Any = None, context: Dict[str, Any] = None):
    """Decorator for automatic error handling."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                # Build context from function arguments
                func_context = {
                    'function': func.__name__,
                    'module': func.__module__,
                    'args_count': len(args),
                    'kwargs': list(kwargs.keys())
                }
                if context:
                    func_context.update(context)

                return error_handler.handle_error(error, fallback_result, func_context)
        return wrapper
    return decorator

def validate_input(validation_func: Callable, error_message: str = None):
    """Decorator for input validation."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Validate first argument (usually self, second is the actual input)
                if len(args) > 1:
                    validation_func(args[1])
                elif 'data' in kwargs:
                    validation_func(kwargs['data'])
                else:
                    raise ValidationError("No input data to validate")
            except Exception as error:
                raise ValidationError(error_message or f"Input validation failed: {error}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

# Recovery strategies
def recover_from_template_error(error: TemplateError, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Recovery strategy for template errors."""
    error_handler.logger.info("Attempting template error recovery")

    # Return a basic template structure
    return {
        'frontmatter': {
            'title': 'Fallback Presentation',
            'theme': 'default'
        },
        'slides': [
            {
                'title': 'Error Recovery',
                'content': 'Template generation encountered an issue. Using fallback template.'
            }
        ]
    }

def recover_from_chart_error(error: ChartError, context: Dict[str, Any] = None) -> str:
    """Recovery strategy for chart errors."""
    error_handler.logger.info("Attempting chart error recovery")

    # Return a simple text-based chart representation
    return """
<div class="simple-chart">
  <h4>Chart (Fallback Mode)</h4>
  <p>Chart generation encountered an issue. Please check data format.</p>
</div>
"""

def recover_from_validation_error(error: ValidationError, context: Dict[str, Any] = None) -> bool:
    """Recovery strategy for validation errors."""
    error_handler.logger.info("Attempting validation error recovery")

    # For validation errors, we can often continue by logging the issue
    return True

def recover_from_content_error(error: ContentError, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Recovery strategy for content analysis errors."""
    error_handler.logger.info("Attempting content error recovery")

    # Return basic content analysis
    return {
        'presentation_type': 'general',
        'complexity': 'intermediate',
        'sections': ['Introduction', 'Main Content', 'Conclusion'],
        'visual_elements': [],
        'confidence': 0.5
    }

# Register recovery strategies
error_handler.register_recovery_strategy(TemplateError, recover_from_template_error)
error_handler.register_recovery_strategy(ChartError, recover_from_chart_error)
error_handler.register_recovery_strategy(ValidationError, recover_from_validation_error)
error_handler.register_recovery_strategy(ContentError, recover_from_content_error)

# Validation functions
def validate_string_input(data: Any, field_name: str = "input"):
    """Validate string input."""
    if not isinstance(data, str):
        raise ValidationError(f"{field_name} must be a string")
    if not data.strip():
        raise ValidationError(f"{field_name} cannot be empty")
    if len(data) > 10000:  # Reasonable limit
        raise ValidationError(f"{field_name} too long (max 10000 characters)")

def validate_dict_input(data: Any, required_keys: list = None):
    """Validate dictionary input."""
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")

    if required_keys:
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            raise ValidationError(f"Missing required keys: {missing_keys}")

def validate_file_path(file_path: str, must_exist: bool = False):
    """Validate file path."""
    if not isinstance(file_path, str):
        raise ValidationError("File path must be a string")

    if must_exist and not os.path.exists(file_path):
        raise ValidationError(f"File does not exist: {file_path}")

    # Check for invalid characters
    invalid_chars = ['<', '>', ':', '"', '|', '?', '*']
    if any(char in file_path for char in invalid_chars):
        raise ValidationError(f"Invalid characters in file path: {file_path}")

def validate_chart_data(data: Dict[str, Any]):
    """Validate chart data structure."""
    validate_dict_input(data)

    if 'labels' in data and 'values' in data:
        if not isinstance(data['labels'], list) or not isinstance(data['values'], list):
            raise ValidationError("Chart labels and values must be lists")

        if len(data['labels']) != len(data['values']):
            raise ValidationError("Chart labels and values must have same length")

        if len(data['labels']) == 0:
            raise ValidationError("Chart data cannot be empty")

class SafeFileOperations:
    """Safe file operations with error handling."""

    @staticmethod
    @handle_slidev_errors(fallback_result=False, context={'operation': 'file_read'})
    def read_file(file_path: str, encoding: str = 'utf-8') -> str:
        """Safely read file contents."""
        validate_file_path(file_path, must_exist=True)

        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            raise ValidationError(f"File encoding error: {file_path}")
        except IOError as e:
            raise ValidationError(f"IO error reading file {file_path}: {e}")

    @staticmethod
    @handle_slidev_errors(fallback_result=False, context={'operation': 'file_write'})
    def write_file(file_path: str, content: str, encoding: str = 'utf-8') -> bool:
        """Safely write file contents."""
        validate_file_path(file_path)
        validate_string_input(content, "file content")

        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w', encoding=encoding) as f:
                f.write(content)
            return True
        except IOError as e:
            raise ValidationError(f"IO error writing file {file_path}: {e}")

    @staticmethod
    @handle_slidev_errors(fallback_result=[], context={'operation': 'directory_list'})
    def list_directory(dir_path: str, pattern: str = "*") -> list:
        """Safely list directory contents."""
        validate_file_path(dir_path, must_exist=True)

        if not os.path.isdir(dir_path):
            raise ValidationError(f"Path is not a directory: {dir_path}")

        try:
            from glob import glob
            return glob(os.path.join(dir_path, pattern))
        except Exception as e:
            raise ValidationError(f"Error listing directory {dir_path}: {e}")

class SafeJSONOperations:
    """Safe JSON operations with error handling."""

    @staticmethod
    @handle_slidev_errors(fallback_result={}, context={'operation': 'json_load'})
    def load_json(file_path: str) -> Dict[str, Any]:
        """Safely load JSON file."""
        content = SafeFileOperations.read_file(file_path)

        try:
            import json
            return json.loads(content)
        except json.JSONDecodeError as e:
            raise ValidationError(f"Invalid JSON in file {file_path}: {e}")

    @staticmethod
    @handle_slidev_errors(fallback_result=False, context={'operation': 'json_save'})
    def save_json(file_path: str, data: Dict[str, Any], indent: int = 2) -> bool:
        """Safely save JSON file."""
        try:
            import json
            content = json.dumps(data, indent=indent, ensure_ascii=False)
            return SafeFileOperations.write_file(file_path, content)
        except TypeError as e:
            raise ValidationError(f"Data not JSON serializable: {e}")

# Utility functions for robust error handling
def safe_execute(func: Callable, *args, fallback_result: Any = None, **kwargs) -> Any:
    """Safely execute a function with error handling."""
    try:
        return func(*args, **kwargs)
    except Exception as error:
        return error_handler.handle_error(error, fallback_result, {'function': func.__name__})

def retry_on_failure(func: Callable, max_retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to retry function on failure."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        last_error = None

        for attempt in range(max_retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                last_error = error
                if attempt < max_retries:
                    error_handler.logger.warning(f"Attempt {attempt + 1} failed, retrying in {delay}s...")
                    import time
                    time.sleep(delay)
                else:
                    error_handler.logger.error(f"All {max_retries + 1} attempts failed")

        # If we get here, all retries failed
        return error_handler.handle_error(last_error)

    return wrapper

def get_error_context() -> Dict[str, Any]:
    """Get current error context information."""
    return {
        'error_summary': error_handler.get_error_summary(),
        'python_version': sys.version,
        'platform': sys.platform,
        'working_directory': os.getcwd()
    }