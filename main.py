import tkinter as tk

def create_window():
    # Create a root window
    root = tk.Tk()
    root.title("Always On Top Box")

    # Set the window size
    root.geometry("36x12")

    # Make the window stay on top
    root.attributes("-topmost", True)

    # Optionally, remove the window decoration (title bar, borders, etc.)
    root.overrideredirect(True)

    # Set window background to transparent
    root.attributes("-alpha", 1.0)

    # Create a label with some text
    label = tk.Label(root, text="abc", bg="light gray")
    label.pack(expand=True, fill=tk.BOTH)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_window()