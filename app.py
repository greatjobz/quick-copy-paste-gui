import tkinter as tk
from tkinter import messagebox
import pyperclip  # Install with: pip install pyperclip
import datetime
import os

# Import credentials (make sure it's ignored in .gitignore)
try:
    from credentials import USERNAME, PASSWORD
except ImportError:
    USERNAME = "Not Found"
    PASSWORD = "Not Found"

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)
    messagebox.showinfo("Copied", f"'{text}' copied to clipboard!")

# Function to get the current date
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# Function to get the current time
def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

# GUI Setup
root = tk.Tk()
root.title("Quick Copy-Paste Tool")
root.geometry("300x300")

# Labels
tk.Label(root, text="Quick Copy-Paste", font=("Arial", 14, "bold")).pack(pady=10)

# Buttons for Date and Time
tk.Button(root, text="Copy Date", command=lambda: copy_to_clipboard(get_current_date())).pack(pady=5)
tk.Button(root, text="Copy Time", command=lambda: copy_to_clipboard(get_current_time())).pack(pady=5)

# Buttons for Username and Password
tk.Button(root, text="Copy Username", command=lambda: copy_to_clipboard(USERNAME)).pack(pady=5)
tk.Button(root, text="Copy Password", command=lambda: copy_to_clipboard(PASSWORD)).pack(pady=5)

# Run the GUI
root.mainloop()
