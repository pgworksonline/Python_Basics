# Example of a custom context manager in Python.
# Demonstrates how __enter__ and __exit__ work, including how exceptions
# inside a 'with' block are passed to __exit__ for handling/cleanup.
class BonjourLeMonde:
        def __enter__(self):
                print("Entering context")
                return "Salut"
        def __exit__(self, exc_type, exc_value, exc_tb):
            if exc_tb is not None:
                print("Exception occurred in context", exc_type, exc_value, exc_tb)
            print("Leaving context")
