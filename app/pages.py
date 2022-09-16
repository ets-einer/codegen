from rich import print
from .common import get_base
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def generate_pages(name: str):
    content = get_base(f"{dir_path}/../bases/Page.txt")
