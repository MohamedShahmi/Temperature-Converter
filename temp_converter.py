import tkinter as tk
from tkinter import messagebox

# Functions for temperature conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to handle conversion based on user input
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        
        if var.get() == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(temp)
            result_label.config(text=f"{temp} Celsius = {result} Fahrenheit")
        elif var.get() == "Celsius to Kelvin":
            result = celsius_to_kelvin(temp)
            result_label.config(text=f"{temp} Celsius = {result} Kelvin")
        elif var.get() == "Fahrenheit to Celsius":
            result = fahrenheit_to_celsius(temp)
            result_label.config(text=f"{temp} Fahrenheit = {result} Celsius")
        elif var.get() == "Fahrenheit to Kelvin":
            result = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"{temp} Fahrenheit = {result} Kelvin")
        elif var.get() == "Kelvin to Celsius":
            result = kelvin_to_celsius(temp)
            result_label.config(text=f"{temp} Kelvin = {result} Celsius")
        elif var.get() == "Kelvin to Fahrenheit":
            result = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"{temp} Kelvin = {result} Fahrenheit")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Set the window size and color
window.geometry("400x300")
window.config(bg="#f0f8ff")

# Title Label
title_label = tk.Label(window, text="Temperature Converter", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#0066cc")
title_label.pack(pady=20)

# Input Field for Temperature
entry_temp = tk.Entry(window, font=("Helvetica", 14), width=20, borderwidth=2, relief="solid", fg="#333")
entry_temp.pack(pady=10)

# Dropdown menu for temperature conversion types
var = tk.StringVar(window)
var.set("Celsius to Fahrenheit")  # default value

conversion_options = [
    "Celsius to Fahrenheit", 
    "Celsius to Kelvin", 
    "Fahrenheit to Celsius", 
    "Fahrenheit to Kelvin", 
    "Kelvin to Celsius", 
    "Kelvin to Fahrenheit"
]

dropdown_menu = tk.OptionMenu(window, var, *conversion_options)
dropdown_menu.config(font=("Helvetica", 12), width=20, bg="#80c7e3", fg="white")
dropdown_menu.pack(pady=10)

# Convert Button
convert_button = tk.Button(window, text="Convert", font=("Helvetica", 14, "bold"), bg="#28a745", fg="white", command=convert_temperature)
convert_button.pack(pady=15)

# Result Label
result_label = tk.Label(window, text="Enter a temperature and select a conversion type", font=("Helvetica", 14), bg="#f0f8ff", fg="#333")
result_label.pack(pady=10)

# Run the window
window.mainloop()
