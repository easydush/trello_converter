# Нажми Shift+F10, чтобы запустить
from loader import load
from uploader import upload


def print_hi():
    print(f'Привет, сладкоежка *))')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi()
    loaded = load()
    upload(loaded)
