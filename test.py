import tkinter as tk

print("Script started...")

root = tk.Tk()
root.title("Test Window")
root.geometry("300x200")

label = tk.Label(root, text="Tkinter is working!", font=("Arial", 14))
label.pack(pady=50)

# Force the window to the front
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

print("About to run mainloop...")
root.mainloop()
print("Exited mainloop.")
