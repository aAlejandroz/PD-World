from tkinter import *


class GridWorld(Frame):
  def __init__(self, master = None):
    self.master = master
    Frame.__init__(self, self.master)
    self.c = Canvas(self.master,  height=500, width=500, bg='black')
    self.create_grid()
    self.init_zeros()
    self.c.pack(fill = BOTH, expand=True)
  
  def create_grid(self):
    w = 500
    h = 500
    self.c.delete('grid_line')
    for i in range(0, 500, 100):
      print(w)
      self.c.create_line([(i, 0), (i, h)], tag='grid_line', fill = 'white')

    for i in range(0, 500, 100):
      self.c.create_line([(0, i), (w, i)], tag='grid_line', fill = 'white')

  def init_zeros(self):
    
    
    
    pass


class Main(GridWorld):
  def __init__(self):
    master = Tk()
    
    master.resizable(width = True, height = True)
    
    app = GridWorld(master)
    app.mainloop()
    
Main()
