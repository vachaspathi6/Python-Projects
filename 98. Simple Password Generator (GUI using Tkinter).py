import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4 characters.")
        return
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    password_entry.config(text=password)

# Create GUI
window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_label = tk.Label(window, text="Generated Password:")
password_label.pack(pady=5)
password_entry = tk.Label(window, text="", bg="white", relief="sunken", width=30)
password_entry.pack(pady=5)

window.mainloop()
