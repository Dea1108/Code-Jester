import tkinter as tk

def calculate_bmi():
    weight_kg = float(weight_entry.get())
    height_m = float(height_entry.get())
    bmi = weight_kg / (height_m ** 2)
    bmi_label.config(text="Your BMI is: {:.2f}".format(bmi))

def calculate_bmr():
    weight_kg = float(weight_entry.get())
    height_m = float(height_entry.get())
    user_age = int(age_entry.get())
    bmr = 88.362 + (13.397 * weight_kg) + (479.9 * height_m) - (5.677 * user_age)
    bmr_label.config(text="Your BMR is: {:.2f}".format(bmr))

def calculate_tdee():
    bmr = float(bmr_label.cget("text").split(":")[1].strip())
    activity_level = float(activity_entry.get())
    tdee_result = bmr * activity_level
    tdee_label.config(text="Your TDEE is: {:.2f}".format(tdee_result))

def calculate_daily_calorie_needs():
    weight_kg = float(weight_entry.get())
    target_weight = float(target_weight_entry.get())
    time_frame = int(time_frame_entry.get())

    weight_loss = weight_kg - target_weight
    calorie_deficit = weight_loss * 7700 / time_frame
    daily_calorie_needs = 2000 - calorie_deficit / 7

    if daily_calorie_needs <= 800:
        calorie_needs_label.config(text="Your goal is too high, think more...")
    else:
        calorie_needs_label.config(text="Your daily calorie needs for weight loss are: {:.2f}".format(daily_calorie_needs))

def reuse():
    question = tk.messagebox.askquestion("Confirmation", "Do you want to use the app again?")
    if question == "yes":
        clear_entries()
    else:
        root.destroy()

def clear_entries():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    target_weight_entry.delete(0, tk.END)
    time_frame_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)
    bmi_label.config(text="")
    bmr_label.config(text="")
    tdee_label.config(text="")
    calorie_needs_label.config(text="")

root = tk.Tk()
root.title("Fitness App")

# Create labels
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, sticky="e")
height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, sticky="e")
age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, sticky="e")
target_weight_label = tk.Label(root, text="Target Weight (kg):")
target_weight_label.grid(row=3, column=0, sticky="e")
time_frame_label = tk.Label(root, text="Time Frame (weeks):")
time_frame_label.grid(row=4, column=0, sticky="e")
activity_label = tk.Label(root, text="Activity Level:")
activity_label.grid(row=5, column=0, sticky="e")

bmi_label = tk.Label(root, text="")
bmi_label.grid(row=6, column=0, columnspan=2)
bmr_label = tk.Label(root, text="")
bmr_label.grid(row=7, column=0, columnspan=2)
tdee_label = tk.Label(root, text="")
tdee_label.grid(row=8, column=0, columnspan=2)
calorie_needs_label = tk.Label(root, text="")
calorie_needs_label.grid(row=9, column=0, columnspan=2)

# Create entry fields
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)
target_weight_entry = tk.Entry(root)
target_weight_entry.grid(row=3, column=1)
time_frame_entry = tk.Entry(root)
time_frame_entry.grid(row=4, column=1)
activity_entry = tk.Entry(root)
activity_entry.grid(row=5, column=1)

# Create buttons
bmi_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
bmi_button.grid(row=0, column=2)
bmr_button = tk.Button(root, text="Calculate BMR", command=calculate_bmr)
bmr_button.grid(row=1, column=2)
tdee_button = tk.Button(root, text="Calculate TDEE", command=calculate_tdee)
tdee_button.grid(row=5, column=2)
calorie_needs_button = tk.Button(root, text="Calculate Daily Calorie Needs", command=calculate_daily_calorie_needs)
calorie_needs_button.grid(row=3, column=2)
reuse_button = tk.Button(root, text="Reuse App", command=reuse)
reuse_button.grid(row=10, column=1)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    weight_kg = float(weight_entry.get())
    height_m = float(height_entry.get())
    bmi = weight_kg / (height_m ** 2)
    bmi_label.config(text="Your BMI is: {:.2f}".format(bmi))

def calculate_bmr():
    weight_kg = float(weight_entry.get())
    height_m = float(height_entry.get())
    user_age = int(age_entry.get())
    bmr = 88.362 + (13.397 * weight_kg) + (479.9 * height_m) - (5.677 * user_age)
    bmr_label.config(text="Your BMR is: {:.2f}".format(bmr))

def calculate_tdee():
    bmr = float(bmr_label.cget("text").split(":")[1].strip())
    activity_level = float(activity_entry.get())
    tdee_result = bmr * activity_level
    tdee_label.config(text="Your TDEE is: {:.2f}".format(tdee_result))

def calculate_daily_calorie_needs():
    weight_kg = float(weight_entry.get())
    target_weight = float(target_weight_entry.get())
    time_frame = int(time_frame_entry.get())

    weight_loss = weight_kg - target_weight
    calorie_deficit = weight_loss * 7700 / time_frame
    daily_calorie_needs = 2000 - calorie_deficit / 7

    if daily_calorie_needs <= 800:
        calorie_needs_label.config(text="Your goal is too high, think more...")
    else:
        calorie_needs_label.config(text="Your daily calorie needs for weight loss are: {:.2f}".format(daily_calorie_needs))

def reuse():
    response = messagebox.askquestion("Confirmation", "Do you want to use the app again?")
    if response == "yes":
        clear_entries()
        clear_labels()

def clear_entries():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    target_weight_entry.delete(0, tk.END)
    time_frame_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)

def clear_labels():
    bmi_label.config(text="")
    bmr_label.config(text="")
    tdee_label.config(text="")
    calorie_needs_label.config(text="")

root = tk.Tk()
root.title("Fitness App")

# Create labels, entry fields, and buttons (same as previous code)

reuse_button = tk.Button(root, text="Reuse App", command=reuse)
reuse_button.grid(row=10, column=1)

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    weight_kg = float(weight_entry.get())
    height_m = float(height_entry.get())
    bmi = weight_kg / (height_m ** 2)
    bmi_label.config(text="Your BMI is: {:.2f}".format(bmi))

def calculate_bmr():
    weight_kg = float(weight_entry.get())
    height_m = float(height_entry.get())
    user_age = int(age_entry.get())
    bmr = 88.362 + (13.397 * weight_kg) + (479.9 * height_m) - (5.677 * user_age)
    bmr_label.config(text="Your BMR is: {:.2f}".format(bmr))

def calculate_tdee():
    bmr = float(bmr_label.cget("text").split(":")[1].strip())
    activity_level = float(activity_entry.get())
    tdee_result = bmr * activity_level
    tdee_label.config(text="Your TDEE is: {:.2f}".format(tdee_result))

def calculate_daily_calorie_needs():
    weight_kg = float(weight_entry.get())
    target_weight = float(target_weight_entry.get())
    time_frame = int(time_frame_entry.get())

    weight_loss = weight_kg - target_weight
    calorie_deficit = weight_loss * 7700 / time_frame
    daily_calorie_needs = 2000 - calorie_deficit / 7

    if daily_calorie_needs <= 800:
        calorie_needs_label.config(text="Your goal is too high, think more...")
    else:
        calorie_needs_label.config(text="Your daily calorie needs for weight loss are: {:.2f}".format(daily_calorie_needs))

def reuse():
    response = messagebox.askquestion("Confirmation", "Do you want to use the app again?")
    if response == "yes":
        clear_entries()
        clear_labels()

def clear_entries():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    target_weight_entry.delete(0, tk.END)
    time_frame_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)

def clear_labels():
    bmi_label.config(text="")
    bmr_label.config(text="")
    tdee_label.config(text="")
    calorie_needs_label.config(text="")

root = tk.Tk()
root.title("Fitness App")

# Create labels, entry fields, and buttons (same as previous code)

reuse_button = tk.Button(root, text="Reuse App", command=reuse)
reuse_button.grid(row=10, column=1)

root.mainloop()

