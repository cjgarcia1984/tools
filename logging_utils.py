import logging
import sys

def setup_logging(path, name, debug=False):
    if not debug:
        root = logging.getLogger()
        root.setLevel(logging.INFO)
        file_path = f"{path}/{name}.log"
        print(f"Debug mode off: logging to {file_path}")
        handler = logging.FileHandler(file_path, 'w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # clear all handlers
        root.handlers = []
        root.addHandler(handler)

        # redirect stdout and stderr
        sys.stdout = handler.stream
        sys.stderr = handler.stream
    else:
        print("Debug mode on: logging to console")

logger = logging.getLogger(__name__)
