# This is a sample Python script.
import os
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if len(sys.arv) > 2:
    print('too many')
    sys.exit()

if len(sys.arv) < 2:
    print('not enough')
    sys.exit()

input_path = sys.argv[1]

if not os.path.isdir(input_path):
    print('path does not ')
    sys.exit()

print('\n'.join(os.listdir(input_path)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
