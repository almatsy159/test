import os

import tkinter as tk

print(os.name)

if os.name == 'posix':
    os.system("bash app_sh.py")
else :
    print("os = windows")
