import functools
import time
from contextlib import contextmanager
from pathlib import Path


def load_puzzle_input(filename: str) -> str:
    path = Path(__file__).parent.parent.parent / f"puzzle_inputs/{filename}.txt"
    with open(path) as file:
        return file.read()
