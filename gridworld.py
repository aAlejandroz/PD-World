from tkinter import *
import numpy as np
import time
from pd_main import *


class GridWorld(Frame):

  def __init__(self, master=None):
    self.master = master
    Frame.__init__(self, self.master)
    self.c = Canvas(self.master, height=500, width=500, bg='black')
    self.sr = []
    self.agent_data = {"x": 0, "y": 0, "item": None}
    self.create_grid()
    self.num = 1
    self.update_gird_numbs()
    self.agent = ()
    self.create_agent()
    self.c.bind("<Key>", self.key)
    self.c.bind("<Button-1>", self.callback)
    self.master.bind("<space>", lambda e: self.experiment_1())
    self.c.pack(fill=BOTH, expand=True)

  def create_grid(self):
    w = 500
    h = 500
    self.c.delete('grid_line')
    for i in range(0, 600, 100):
      self.c.create_line([(i, 0), (i, h)], tag='grid_line', fill='white')

    for i in range(0, 600, 100):
      self.c.create_line([(0, i), (w, i)], tag='grid_line', fill='white')
    self.c.create_rectangle(0, 0, 100, 100, fill="sea green")
    self.c.create_rectangle(200, 200, 300, 300, fill="sea green")
    self.c.create_rectangle(400, 400, 500, 500, fill="sea green")

    self.c.create_rectangle(400, 100, 500, 200, fill="dark orange")
    self.c.create_rectangle(300, 400, 200, 500, fill="dark orange")
    self.c.create_rectangle(0, 400, 100, 500, fill="dark orange")

  def init_zeros(self):
    s = 0
    x = 25
    y = 5
    self.sr = np.zeros([x, y], dtype=np.object)
    for x in range(25):
      self.sr[:, 1:] = float(0)
      self.sr[x][0] = s
      s = s + 1

  def update_gird_numbs(self):
    global pickup_q_table
    global dropoff_q_table
    global agent

    q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table
    
    row = 0
    column = 0
    y_coordinate = 0

    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=q_table[row][column][0], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 85, y_coordinate + 50, text=q_table[row][column][1], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      self.c.create_text(i + 50, y_coordinate + 90, text=q_table[row][column][2], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 15, y_coordinate + 50, text=q_table[row][column][3], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      column += 1
    y_coordinate = 100
    row = 1
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=q_table[row][column][0], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 85, y_coordinate + 50, text=q_table[row][column][1], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      self.c.create_text(i + 50, y_coordinate + 90, text=q_table[row][column][2], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 15, y_coordinate + 50, text=q_table[row][column][3], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      column += 1
    y_coordinate = 200
    row = 2
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=q_table[row][column][0], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 85, y_coordinate + 50, text=q_table[row][column][1], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      self.c.create_text(i + 50, y_coordinate + 90, text=q_table[row][column][2], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 15, y_coordinate + 50, text=q_table[row][column][3], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      column += 1
    y_coordinate = 300
    row = 3
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=q_table[row][column][0], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 85, y_coordinate + 50, text=q_table[row][column][1], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      self.c.create_text(i + 50, y_coordinate + 90, text=q_table[row][column][2], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 15, y_coordinate + 50, text=q_table[row][column][3], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      column += 1
    y_coordinate = 400
    row = 4
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text= q_table[row][column][0], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 85, y_coordinate + 50, text= q_table[row][column][1], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      self.c.create_text(i + 50, y_coordinate + 90, text= q_table[row][column][2], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 15, y_coordinate + 50, text= q_table[row][column][3], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      column += 1

  def create_agent(self):
    self.agent = self.c.create_oval(434, 34, 464, 64, fill='cyan', tags='Agent')
    self.agent_data["item"] = self.c.find_closest(448, 47)[0]

  def key(self, event):
    print("pressed", repr(event.char))

  def callback(self, event):
    print("clicked at", event.x, event.y)

  def experiment_1(self):

    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    initalizeCells(pickup_states, dropoff_states)

    for index in range(4000):
      agent.policy = "PRandom"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      time.sleep(0.35)
      self.move_agent(agent.action)
      self.delete_nums()
      self.update_gird_numbs()
      self.master.update()

    # TODO Where we display the Q_table

    for index in range(4000):
      agent.policy = "PGreedy"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      time.sleep(0.35)
      self.move_agent(agent.action)
      self.delete_nums()
      self.update_gird_numbs()
      self.master.update()

    print("FINISH")

    initialize_Q_table()

  def experiment_2(self):
    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    initalizeCells(pickup_states, dropoff_states)

    for index in range(200):
      agent.policy = "PRandom"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      time.sleep(0.35)
      self.move_agent(agent.action)
      self.delete_nums()
      self.update_gird_numbs()
      self.master.update()

    for index in range(7800):
      agent.policy = "PExploit"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      time.sleep(0.35)
      self.move_agent(agent.action)
      self.delete_nums()
      self.update_gird_numbs()
      self.master.update()

    print("FINISH")

    initialize_Q_table()


  def move_agent(self, action):

    if action.name == "NORTH":
      self.c.move(self.agent_data['item'], 0, -100)
    elif action.name == "EAST":
      self.c.move(self.agent_data['item'], 100, 0)
    elif action.name == "SOUTH":
      self.c.move(self.agent_data['item'], 0, 100)
    elif action.name == "WEST":
      self.c.move(self.agent_data['item'], -100, 0)

    self.master.update()


  def delete_nums(self):
    self.c.delete("nums")


class Main(GridWorld):
  def __init__(self):
    master = Tk()

    master.resizable(width=False, height=False)

    app = GridWorld(master)
    app.mainloop()


Main()
