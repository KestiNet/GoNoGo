import tkinter as tk
from tkinter import messagebox

# Function to be called when button is pressed
def show_message():
    time = [entry.get() for entry in entries]
    
    sum_of_entries = 0

    message = ""
    for day, time in zip(weekdays, time):
        try:
            value = float(time)  # Correctly convert the string to an integer
        except ValueError:
            value = 0
        sum_of_entries += value
        converted_time = convert_decimal_hours_to_time(value)
        message += f"{day}: {converted_time[0]}:{converted_time[1]}\n"
    message += f"\nTotal Sum: {convert_decimal_hours_to_time(sum_of_entries)[0]}:{convert_decimal_hours_to_time(sum_of_entries)[1]}"
    messagebox.showinfo("Message", message)
    
   #TODO: fix time presentation


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
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Create label and entry widget pairs for each weekday
entries = []
for i, day in enumerate(weekdays):
    label = tk.Label(input_frame, text=f"{day}:")
    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)

    entry = tk.Entry(input_frame)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Create a button that calls show_message when pressed
button = tk.Button(root, text="Calculate GoNoGo", command=show_message)
button.pack(pady=10)

# Run the application
root.mainloop()
