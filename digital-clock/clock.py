import tkinter as tk
import time

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("300x100")

        # Create label for displaying date
        self.date_label = tk.Label(self, font=("Arial", 24))
        self.date_label.pack(side="top")

        # Create label for displaying time
        self.time_label = tk.Label(self, font=("Arial", 24))
        self.time_label.pack(side="top")

        # Create quit button
        self.quit_button = tk.Button(self, text="Quit", command=self.quit, font=("Arial", 24))
        self.quit_button.pack(side="bottom")

        # Update clock display
        self.update_clock()

    def update_clock(self):
        # Update date label
        current_date = time.strftime("%A %B %d, %Y")
        self.date_label.config(text=current_date)

        # Update time label
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)

        # Schedule the update in 1 second
        self.after(1000, self.update_clock)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
