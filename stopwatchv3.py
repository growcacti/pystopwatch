import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch")

        self.timer_running = False
        self.start_time = None

        self.time_entry = tk.Entry(master, font=('Arial', 30))
        self.time_entry.grid(row=0, columnspan=3)

        self.start_button = tk.Button(master, text='Start', command=self.start_timer)
        self.start_button.grid(row=1, column=0)

        self.stop_button = tk.Button(master, text='Stop', command=self.stop_timer)
        self.stop_button.grid(row=1, column=1)

        self.reset_button = tk.Button(master, text='Reset', command=self.reset_timer)
        self.reset_button.grid(row=1, column=2)
        self.lapclear_button = tk.Button(master, text='Clear Lap', command=self.lapclear)
        self.lapclear_button.grid(row=1, column=3)
        self.stopped_times_listbox = tk.Listbox(master, width=20, height=10)
        self.stopped_times_listbox.grid(row=2, columnspan=3)

    def start_timer(self):
        if not self.timer_running:
            self.start_time = time.time() - (self.start_time or 0)
            self.update_timer()
            self.timer_running = True

    def stop_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            time_string = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
            self.stopped_times_listbox.insert(tk.END, time_string)
            self.start_time = None
            self.timer_running = False

    def reset_timer(self):
        self.start_time = None
        self.timer_running = False
        self.time_entry.delete(0, tk.END)
        
    def lapclear(self):
       self.stopped_times_listbox.delete(0, tk.END)

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            hours, minutes = divmod(minutes, 60)
            milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
            time_string = f'{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}'
            self.time_entry.delete(0, tk.END)
            self.time_entry.insert(0, time_string)
##            self.time_label.config(text=time_string)
        self.master.after(10, self.update_timer)  # Update every 10 milliseconds for milliseconds precision









def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
