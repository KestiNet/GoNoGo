import tkinter as tk
from tkinter import messagebox

# Function to be called when button is pressed
def show_message():
    inputs = [entry.get() for entry in entries]
    
    sum_of_entries = 0

    message = ""
    for day, input in zip(weekdays, inputs):
        try:
            value = int(input)
        except ValueError:
            value = 0
        sum_of_entries += value
        message += f"{day}: {input}\n"
    
    message += f"\nTotal Sum: {sum_of_entries}"
    messagebox.showinfo("Message", message)
    
    #message = "\n".join(f"{day}: {input}" for day, input in zip(weekdays, inputs))
    #messagebox.showinfo("Message", message)

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
