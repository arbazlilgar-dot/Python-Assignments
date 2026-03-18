import tkinter as tk

# Function to calculate the math result
def calculate():
    try:
        # eval() automatically solves the math string (e.g., "5+5" becomes 10)
        result = eval(entry.get())
        entry.delete(0, tk.END) # Clear the box
        entry.insert(tk.END, str(result)) # Show the answer
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the screen
def clear_screen():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the input box at the top
entry = tk.Entry(window, width=25, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Create buttons using a grid layout (Row 1)
tk.Button(window, text="7", width=5, command=lambda: entry.insert(tk.END, "7")).grid(row=1, column=0)
tk.Button(window, text="8", width=5, command=lambda: entry.insert(tk.END, "8")).grid(row=1, column=1)
tk.Button(window, text="9", width=5, command=lambda: entry.insert(tk.END, "9")).grid(row=1, column=2)
tk.Button(window, text="+", width=5, command=lambda: entry.insert(tk.END, "+")).grid(row=1, column=3)

# Row 2
tk.Button(window, text="4", width=5, command=lambda: entry.insert(tk.END, "4")).grid(row=2, column=0)
tk.Button(window, text="5", width=5, command=lambda: entry.insert(tk.END, "5")).grid(row=2, column=1)
tk.Button(window, text="6", width=5, command=lambda: entry.insert(tk.END, "6")).grid(row=2, column=2)
tk.Button(window, text="-", width=5, command=lambda: entry.insert(tk.END, "-")).grid(row=2, column=3)

# Row 3
tk.Button(window, text="1", width=5, command=lambda: entry.insert(tk.END, "1")).grid(row=3, column=0)
tk.Button(window, text="2", width=5, command=lambda: entry.insert(tk.END, "2")).grid(row=3, column=1)
tk.Button(window, text="3", width=5, command=lambda: entry.insert(tk.END, "3")).grid(row=3, column=2)
tk.Button(window, text="*", width=5, command=lambda: entry.insert(tk.END, "*")).grid(row=3, column=3)

# Row 4
tk.Button(window, text="C", width=5, command=clear_screen).grid(row=4, column=0)
tk.Button(window, text="0", width=5, command=lambda: entry.insert(tk.END, "0")).grid(row=4, column=1)
tk.Button(window, text="=", width=5, command=calculate).grid(row=4, column=2)
tk.Button(window, text="/", width=5, command=lambda: entry.insert(tk.END, "/")).grid(row=4, column=3)

# Keep the window open
window.mainloop()