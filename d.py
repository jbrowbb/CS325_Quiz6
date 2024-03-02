from abc import ABC, abstractmethod

# Define an abstract logging interface
class Logger(ABC):
    @abstractmethod
    def debug(self, message: str):
        pass

    @abstractmethod
    def info(self, message: str):
        pass

    @abstractmethod
    def warning(self, message: str):
        pass

    @abstractmethod
    def error(self, message: str):
        pass

# Implement a logging adapter for the logging library
class LoggingLibraryAdapter(Logger):
    def debug(self, message: str):
        # Implement debug logging using the logging library
        print(f"[DEBUG] {message}")

    def info(self, message: str):
        # Implement info logging using the logging library
        print(f"[INFO] {message}")

    def warning(self, message: str):
        # Implement warning logging using the logging library
        print(f"[WARNING] {message}")

    def error(self, message: str):
        # Implement error logging using the logging library
        print(f"[ERROR] {message}")

# Example application code using the abstract logging interface
class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform_operation(self):
        # Perform some operation
        self.logger.debug("Starting operation...")
        try:
            # Simulate an operation that may raise an exception
            result = 1 / 0
        except Exception as e:
            # Log the error message and exception details
            self.logger.error(f"An error occurred: {str(e)}")
        else:
            self.logger.info("Operation completed successfully.")