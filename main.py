"""# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
from datetime import datetime

ten, start, end, rain = input().strip(), input().strip(), input().strip(), int(input().strip())
time_start = datetime.strptime(start, "%H:%M")
time_end = datetime.strptime(end, "%H:%M")
time = time_end - time_start
time = time.total_seconds() / 3600
print(time)