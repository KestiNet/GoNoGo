import tkinter as tk
from tkinter import messagebox
import datetime

work_time = 41.5

# Function to be called when button is pressed
def show_message():
    times = [entry.get() for entry in entries]
    friday_start_time = friday_start_entry.get()

    try:
        friday_start_value = float(friday_start_time)
    except ValueError:
        friday_start_value = 0
    
    converted_friday = convert_decimal_hours_to_time(friday_start_value)

    sum_of_entries = 0
    message = ""
    for day, time in zip(weekdays, times):
        try:
            value = float(time)
        except ValueError:
            value = 0
        sum_of_entries += value
        converted_time = convert_decimal_hours_to_time(value)
        message += f"{day}: {converted_time[0]:02d}:{converted_time[1]:02d}\n"

    message += f"Friday start time: {converted_friday[0]:02d}:{converted_friday[1]:02d}\n"
    go_home_time = calc_GoHomeTime(sum_of_entries)
    go_home_time_converted = convert_decimal_hours_to_time(go_home_time)
    message += f"GoHome: {go_home_time_converted[0]:02d}:{go_home_time_converted[1]:02d}\n"
    total_sum_time = convert_decimal_hours_to_time(sum_of_entries)
    message += f"\nTotal Sum: {total_sum_time[0]:02d}:{total_sum_time[1]:02d}"
    messagebox.showinfo("Message", message)

def calc_GoHomeTime(sum_of_enteries):
    GoHome = work_time - sum_of_enteries
    return GoHome



def convert_decimal_hours_to_time(value):
    total_minutes = value * 60
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return int(hours), int(minutes)
    

# Create the main window
root = tk.Tk()
root.title("GoNoGo")

# Create a frame to hold the label and entry widgets
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Weekdays list
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]

# Create label and entry widget pairs for each weekday
entries = []
for i, day in enumerate(weekdays):
    label = tk.Label(input_frame, text=f"{day}:")
    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)

    entry = tk.Entry(input_frame)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Ask the user to enter Friday start time
friday_start_label = tk.Label(input_frame, text="Friday start time:")
friday_start_label.grid(row=len(weekdays), column=0, padx=5, pady=5, sticky=tk.W)

friday_start_entry = tk.Entry(input_frame)
friday_start_entry.grid(row=len(weekdays), column=1, padx=5, pady=5)

# Create a button that calls show_message when pressed
button = tk.Button(root, text="Calculate GoNoGo", command=show_message)
button.pack(pady=10)

# Run the application
root.mainloop()
