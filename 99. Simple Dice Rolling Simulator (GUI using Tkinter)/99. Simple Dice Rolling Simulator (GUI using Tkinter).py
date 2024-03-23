import tkinter as tk
from PIL import Image, ImageTk
import random

def roll_dice():
    dice_values = [1, 2, 3, 4, 5, 6]
    dice_value = random.choice(dice_values)
    image_path = f"dice_images/{dice_value}.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    dice_label.config(image=photo)
    dice_label.image = photo

# Create GUI
window = tk.Tk()
window.title("Dice Rolling Simulator")

dice_label = tk.Label(window)
dice_label.pack(pady=10)

roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)

window.mainloop()
