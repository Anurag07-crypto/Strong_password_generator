import random
import tkinter as tk
from tkinter import messagebox

def gen_pass():
    name = name_entry.get()
    birth_year = birth_entry.get()
    special_character = special_char_entry.get()
    fav_object = object_entry.get()

    if not (name and birth_year and special_character and fav_object):
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    l = [name, birth_year, special_character, fav_object]
    random.shuffle(l)
    d = ''.join(l)

    result_label.config(text=f"Your generated password is:\n{d}")

def clear_fields():
    name_entry.delete(0, tk.END)
    birth_entry.delete(0, tk.END)
    special_char_entry.delete(0, tk.END)
    object_entry.delete(0, tk.END)
    result_label.config(text="")

# Setup the main window
root = tk.Tk()
root.title("Password Generator App")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Password Generator (●'◡'●)", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Input fields
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)
name_entry.insert(0, "Enter your name")

birth_entry = tk.Entry(root, width=30)
birth_entry.pack(pady=5)
birth_entry.insert(0, "Enter your Birth Year")

special_char_entry = tk.Entry(root, width=30)
special_char_entry.pack(pady=5)
special_char_entry.insert(0, "Enter a special character")

object_entry = tk.Entry(root, width=30)
object_entry.pack(pady=5)
object_entry.insert(0, "Enter your fav object or anime")

# Buttons
gen_button = tk.Button(root, text="Generate Password", command=gen_pass, bg="#4caf50", fg="white")
gen_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_fields, bg="#f44336", fg="white")
clear_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
result_label.pack(pady=20)

# Run the app
root.mainloop()
