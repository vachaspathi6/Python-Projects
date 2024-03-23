import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

def main():
    global label
    root = tk.Tk()
    root.title("Simple Clock")
    label = tk.Label(root, font=("Arial", 35), fg="black")
    label.pack(padx=50, pady=50)
    update_time()
    root.mainloop()

if __name__ == "__main__":
    main()
