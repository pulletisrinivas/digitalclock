import tkinter as tk
from datetime import datetime
 
class DigitalClock(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.pack()
 
        # Create label for displaying time
        self.time = tk.Label(
            font=('Helvetica', 48), 
            foreground='black', background='red'
        )
        self.time.pack(fill=tk.BOTH, expand=True)
 
    def tick(self):
        now = datetime.now().strftime('%H:%M:%S')
        self.time['text'] = now
        self.time.after(1000, self.tick)
 
 
if __name__ == '__main__':
    root = tk.Tk()
    app = DigitalClock(root)
    app.tick()
    root.mainloop()