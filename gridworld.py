from tkinter import *
import numpy as np
import time
from pd_main import *


class GridWorld(Frame):

  def __init__(self, master=None):
    self.master = master
    Frame.__init__(self, self.master)
    self.c = Canvas(self.master, height=500, width=500, bg='black')
    self.agent_data = {"x": 0, "y": 0, "item": None}
    self.create_grid()
    self.num = 1
    self.update_gird_numbs()
    self.agent = ()
    self.create_agent()
    self.master.bind("<space>", lambda e: self.prompt_experiments())
    self.c.pack(fill=BOTH, expand=True)

  def create_grid(self):
    w = 500
    h = 500
    self.c.delete('grid_line')
    self.c.create_rectangle(0, 0, 100, 100, fill="sea green")
    self.c.create_rectangle(200, 200, 300, 300, fill="sea green")
    self.c.create_rectangle(400, 400, 500, 500, fill="sea green")

    self.c.create_rectangle(400, 100, 500, 200, fill="dark orange")
    self.c.create_rectangle(300, 400, 200, 500, fill="dark orange")
    self.c.create_rectangle(0, 400, 100, 500, fill="dark orange")
    y_coordinate = 0
    for i in range(0, 500, 100):
      self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='red', width=1, arrow=FIRST, tags='nums')
    y_coordinate = 100
    for i in range(0, 500, 100):
      self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='red', width=1, arrow=FIRST, tags='nums')
    y_coordinate = 200
    for i in range(0, 500, 100):
      self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='red', width=1, arrow=FIRST, tags='nums')
    y_coordinate = 300
    for i in range(0, 500, 100):
      self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='red', width=1, arrow=FIRST, tags='nums')
    y_coordinate = 400
    for i in range(0, 500, 100):
      self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='red', width=1, arrow=FIRST, tags ='nums')

    for i in range(0, 600, 100):
      self.c.create_line([(i, 0), (i, h)], tag='grid_line', fill='white')

    for i in range(0, 600, 100):
      self.c.create_line([(0, i), (w, i)], tag='grid_line', fill='white')


  def update_arrows(self):
    global pickup_q_table
    global dropoff_q_table
    global agent

    q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table

    row = 0
    column = 0
    y_coordinate = 0
    for i in range(0,500,100):
      direction = self.get_max_q_value(row,column,q_table)
      if(q_table[row][column][direction] > 2.25):
        if(direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif(direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif(direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif(direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
      else:
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
      column += 1
    row = 1
    column = 0
    y_coordinate = 100
    for i in range(0, 500, 100):
      direction = self.get_max_q_value(row, column, q_table)
      if (q_table[row][column][direction] > 2.25):
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
      else:
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
      column += 1
    row = 2
    column = 0
    y_coordinate = 200
    for i in range(0, 500, 100):
      direction = self.get_max_q_value(row, column, q_table)
      if (q_table[row][column][direction] > 2.25):
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
      else:
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
      column += 1
    row = 3
    column = 0
    y_coordinate = 300
    for i in range(0, 500, 100):
      direction = self.get_max_q_value(row, column, q_table)
      if (q_table[row][column][direction] > 2.25):
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
      else:
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
      column += 1
    row = 4
    column = 0
    y_coordinate = 400
    for i in range(0, 500, 100):
      direction = self.get_max_q_value(row, column, q_table)
      if (q_table[row][column][direction] > 2.25):
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='green2', width=1, arrow=FIRST,
                             tags='nums')
      else:
        if (direction == 0):
          self.c.create_line(i + 50, y_coordinate + 40, i + 50, y_coordinate + 60, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 1):
          self.c.create_line(i + 60, y_coordinate + 50, i + 40, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 2):
          self.c.create_line(i + 50, y_coordinate + 60, i + 50, y_coordinate + 40, fill='white', width=1, arrow=FIRST,
                             tags='nums')
        elif (direction == 3):
          self.c.create_line(i + 40, y_coordinate + 50, i + 60, y_coordinate + 50, fill='white', width=1, arrow=FIRST,
                             tags='nums')
      column += 1

  def get_max_q_value(self, x, y, table):
    max = table[x][y][3]
    index = 3
    for i in range(4):
      if(table[x][y][i] > max):
        max = table[x][y][i]
        index = i
    return index

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
      self.c.create_text(i + 50, y_coordinate + 10, text=q_table[row][column][0], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 85, y_coordinate + 50, text=q_table[row][column][1], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      self.c.create_text(i + 50, y_coordinate + 90, text=q_table[row][column][2], font="Verdana 8 bold",
                         fill='white', tags='nums')
      self.c.create_text(i + 15, y_coordinate + 50, text=q_table[row][column][3], font="Verdana 8 bold",
                         fill='white', tags='nums', angle=90)
      column += 1

  def create_agent(self):
    self.agent = self.c.create_oval(434, 34, 464, 64, fill='cyan', tags='Agent')
    self.agent_data["item"] = self.c.find_closest(448, 47)[0]

  def moveAndUpdateAgent(self):
    # time.sleep(0.2)
    self.move_agent(agent.action)
    self.delete_nums()
    self.update_arrows()
    self.update_gird_numbs()
    self.master.update()

  def resetAgent(self):
    self.c.delete(self.agent)
    self.agent_data["item"] = None
    self.create_agent()

  def experiment_1(self):

    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    initalizeCells(pickup_states, dropoff_states)

    for index in range(4000):
      agent.policy = "PRandom"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      # time.sleep(0.1)
      self.moveAndUpdateAgent()

    # TODO Where we display the Q_table

    for index in range(4000):
      agent.policy = "PGreedy"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      # time.sleep(0.1)
      self.moveAndUpdateAgent()

    print("FINISH")

  def experiment_2(self):
    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    initalizeCells(pickup_states, dropoff_states)

    for index in range(200):
      agent.policy = "PRandom"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      # time.sleep(0.35)
      self.moveAndUpdateAgent()

    for index in range(7800):
      agent.policy = "PExploit"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      # time.sleep(0.35)
      self.moveAndUpdateAgent()

    print("FINISH")


    initialize_Q_table()

  def move_agent(self, action):
    if action.name == "NORTH":
      self.c.move(self.agent, 0, -100)
    elif action.name == "EAST":
      self.c.move(self.agent, 100, 0)
    elif action.name == "SOUTH":
      self.c.move(self.agent, 0, 100)
    elif action.name == "WEST":
      self.c.move(self.agent, -100, 0)
    elif action.name == "RESET":
      self.resetAgent()

    self.master.update()

  def delete_nums(self):
    self.c.delete("nums")

  def prompt_experiments(self):
    experiment_num = int(input("Choose Experiment 1 - 5 by entering the corresponding number -  \n" ))
    if experiment_num == 1:
      print("|----------------Running Experiment 1----------------| \n")
      self.experiment_1()
      initialize_Q_table()
      self.create_agent()
      self.delete_nums()
    elif experiment_num == 2:
      print("|----------------Running Experiment 2----------------|\n")
      self.experiment_2()
      initialize_Q_table()
      self.create_agent()
      self.delete_nums()
    # elif experiment_num == 3:
    #   print("|----------------Running Experiment 3----------------|\n")
    #   experiment_3()
    # elif experiment_num == 4:
    #   print("|----------------Running Experiment 4----------------|\n")
    #   experiments_4()
    # elif experiment_num == 5:
    #   print("|----------------Running Experiment 5----------------|\n")
    #   experiment_5()


class Main(GridWorld):
  def __init__(self):
    master = Tk()
    
    master.resizable(width=False, height=False)

    app = GridWorld(master)
    app.mainloop()


Main()
