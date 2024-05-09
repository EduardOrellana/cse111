import tkinter as tk
from tkinter import messagebox

# Function to display a message box
def show_message():
    messagebox.showinfo("Message", "Hello, Tkinter!")

# Create main window
root = tk.Tk()
root.title("Tkinter GUI Demo")

# Label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Button
button = tk.Button(root, text="Click Me", command=show_message)
button.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# Checkbox
checkbox = tk.Checkbutton(root, text="Check me!")
checkbox.pack()

# Radio buttons
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="option1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="option2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Optoin 3")
radio1.pack()
radio2.pack()

# Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()

# Combobox
from tkinter.ttk import Combobox
combo = Combobox(root)
combo['values'] = ("Option 1", "Option 2", "Option 3")
combo.pack()

# Menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack()
canvas.create_rectangle(50, 25, 150, 75, fill="blue")

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(root, yscrollcommand=scrollbar.set)
for i in range(20):
    text.insert(tk.END, f"This is line {i+1}\n")
text.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=text.yview)

# Run the main event loop
root.mainloop()
