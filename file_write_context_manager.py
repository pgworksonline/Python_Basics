# Example of a custom context manager for file operations.
# Useful in DevOps for writing logs, configs, or build artifacts,
# while guaranteeing files are closed cleanly during automation runs.

from contextlib import contextmanager

@contextmanager
def writeable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()
