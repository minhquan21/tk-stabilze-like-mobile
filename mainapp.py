import tkinter as tk
import webbrowser

def buttonclicked():
    webbrowser.open("https://github.com/minhquan21", new=2)

def on_move(event=None):
    """Quickly reposition the button only when the window moves or resizes."""
    global last_win_x, last_win_y, last_win_w, last_win_h

    # Get the window's current position and size
    win_x = mainwindow.winfo_x()
    win_y = mainwindow.winfo_y()
    win_w = mainwindow.winfo_width()
    win_h = mainwindow.winfo_height()

    # Only update if the position or size has changed
    if (win_x, win_y, win_w, win_h) != (last_win_x, last_win_y, last_win_w, last_win_h):
        btn.update_idletasks()  # Ensure accurate size

        # Get screen size
        screen_width = mainwindow.winfo_screenwidth()
        screen_height = mainwindow.winfo_screenheight()

        # Get button size
        btn_width = btn.winfo_width()
        btn_height = btn.winfo_height()

        # Calculate button's absolute position (fixed at center of screen)
        btn_x = (screen_width // 2) - (btn_width // 2) - win_x
        btn_y = (screen_height // 2) - (btn_height // 2) - win_y

        # Move the button instantly
        btn.place(x=btn_x, y=btn_y)

        # Store the last known position and size
        last_win_x, last_win_y, last_win_w, last_win_h = win_x, win_y, win_w, win_h

# Create main window
mainwindow = tk.Tk()
mainwindow.title("this is a python-tk test script")
mainwindow.geometry("350x350")  # Window size

# Create button
btn = tk.Button(mainwindow,text="Click Me", fg="red", command=buttonclicked)
btn.config(padx=10, pady=20)
btn.place(x=0, y=0)  # Temporary position until it's moved


# Initialize position variables
last_win_x = last_win_y = last_win_w = last_win_h = -1

# Update button position after UI initializes
mainwindow.update_idletasks()
on_move()

# Track window movement
mainwindow.bind("<Configure>", on_move)

mainwindow.mainloop()
