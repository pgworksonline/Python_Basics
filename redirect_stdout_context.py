# Custom context manager to redirect stdout in Python.
# Useful in DevOps pipelines for controlling log streams,
# capturing output during automation tasks, or rerouting print
# statements to files, buffers, or monitoring systems.

import sys

class RedirectStdout:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.saved_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, *args):
        sys.stdout = self.saved_output
