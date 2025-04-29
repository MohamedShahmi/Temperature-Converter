import tkinter as tk
from tkinter import messagebox

# Conversion Functions 
def celsius_to_fahrenheit(c): 
    return (c * 9/5) + 32
def celsius_to_kelvin(c): 
    return c + 273.15
def fahrenheit_to_celsius(f): 
    return (f - 32) * 5/9
def fahrenheit_to_kelvin(f): 
    return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k): 
    return k - 273.15
def kelvin_to_fahrenheit(k): 
    return (k - 273.15) * 9/5 + 32

# Conversion Trigger 
def convert_temperature(event=None):
    try:
        temp = float(entry_temp.get())
        conversion = var.get()

        if conversion == "Select Conversion Type":
            messagebox.showwarning("Select Type", "Please choose a conversion type.")
            return

        units = {
            "Celsius": "°C",
            "Fahrenheit": "°F",
            "Kelvin": "K"
        }

        if conversion == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(temp)
            description = f"{temp} °C is equal to {round(result, 2)} °F"
        elif conversion == "Celsius to Kelvin":
            result = celsius_to_kelvin(temp)
            description = f"{temp} °C is equal to {round(result, 2)} K"
        elif conversion == "Fahrenheit to Celsius":
            result = fahrenheit_to_celsius(temp)
            description = f"{temp} °F is equal to {round(result, 2)} °C"
        elif conversion == "Fahrenheit to Kelvin":
            result = fahrenheit_to_kelvin(temp)
            description = f"{temp} °F is equal to {round(result, 2)} K"
        elif conversion == "Kelvin to Celsius":
            result = kelvin_to_celsius(temp)
            description = f"{temp} K is equal to {round(result, 2)} °C"
        elif conversion == "Kelvin to Fahrenheit":
            result = kelvin_to_fahrenheit(temp)
            description = f"{temp} K is equal to {round(result, 2)} °F"

        result_label.config(text=description)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Reset Fields
def clear_fields():
    entry_temp.delete(0, tk.END)
    var.set("Select Conversion Type")
    result_label.config(text="Enter a value and select a conversion")

# UI Setup 
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("500x400")
window.configure(bg="#e6f2ff")
window.minsize(400, 350)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Card container
card_bg = "#f5f0ff"
card = tk.Frame(window, bg=card_bg, bd=2, relief="raised", padx=20, pady=20)
card.place(relx=0.5, rely=0.5, anchor='center')

# Title
title_label = tk.Label(card, text="Temperature Converter", font=("Times New Roman", 18, "bold"), bg=card_bg, fg="#333399")
title_label.pack(pady=15)

# Entry field
entry_temp = tk.Entry(card, font=("Times New Roman", 14), width=25, relief="solid", justify="center")
entry_temp.pack(pady=(10, 3))

# Input helper message
input_hint = tk.Label(card, text="(Enter a temperature value, e.g., 37.5)", font=("Times New Roman", 10, "italic"), bg=card_bg, fg="#777")
input_hint.pack(pady=(0, 10))

# Dropdown menu
options = [
    "Celsius to Fahrenheit", 
    "Celsius to Kelvin",
    "Fahrenheit to Celsius", 
    "Fahrenheit to Kelvin",
    "Kelvin to Celsius", 
    "Kelvin to Fahrenheit"
]
var = tk.StringVar(value="Select Conversion Type")
dropdown = tk.OptionMenu(card, var, *options)
dropdown.config(font=("Times New Roman", 12), width=22, bg="#4da6ff", fg="white", highlightthickness=0)
dropdown["menu"].config(font=("Times New Roman", 11))
dropdown.pack(pady=5)

# Dropdown hint
dropdown_hint = tk.Label(card, text="(Choose the conversion type)", font=("Times New Roman", 10, "italic"), bg=card_bg, fg="#777")
dropdown_hint.pack(pady=(0, 10))

# Buttons
button_frame = tk.Frame(card, bg=card_bg)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="Convert", font=("Times New Roman", 14, "bold"), bg="#28a745", fg="white", command=convert_temperature)
convert_button.pack(side="left", padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Times New Roman", 14, "bold"), bg="#dc3545", fg="white", command=clear_fields)
clear_button.pack(side="left", padx=10)

# Result label
result_label = tk.Label(card, text="Enter a value and select a conversion", font=("Times New Roman", 14), bg=card_bg, fg="#333")
result_label.pack(pady=10)

# Responsive centering
def resize_center(event=None):
    card.place(relx=0.5, rely=0.5, anchor='center')

window.bind('<Configure>', resize_center)
resize_center()

window.bind('<Return>', convert_temperature)

window.mainloop()
