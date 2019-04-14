import tkinter as tk
q_values = []
def create_grid(event=None):

    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intervals of 100
    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line', fill = 'white')
        #c.create_text()

    # Creates all horizontal lines at intervals of 100
    for i in range(0, h, 100):
        c.create_line([(0, i), (w, i)], tag='grid_line', fill = 'white')



root = tk.Tk()

c = tk.Canvas(root, height=500, width=500, bg='black')
c.pack(fill = tk.BOTH, expand=True)
c.bind('<Configure>', create_grid)


root.resizable(width=False, height=False)
root.mainloop()