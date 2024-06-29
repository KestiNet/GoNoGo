import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a label
label = tk.Label(root, text="Hello, World!")
label.pack(pady=10)

# Function to update the label
def update_label():
    label.config(text="Button Clicked!")

# Create a button
button = tk.Button(root, text="Click Me", command=update_label)
button.pack(pady=10)

# Run the application
root.mainloop()
