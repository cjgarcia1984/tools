import logging
import sys

def setup_logging(file_path):
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.FileHandler(file_path, 'w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # clear all handlers
    root.handlers = []
    root.addHandler(handler)

    # redirect stdout and stderr
    sys.stdout = handler.stream
    sys.stderr = handler.stream

logger = logging.getLogger(__name__)
