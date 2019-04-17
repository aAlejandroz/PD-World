from tkinter import *
import numpy as np
import time
from pd_main import *
from tkinter import PhotoImage


class GridWorld(Frame):

  def __init__(self, master=None):
    self.pickup_list = []
    self.dropoff_list = []
    self.master = master
    Frame.__init__(self, self.master)
    self.c = Canvas(self.master, height=500, width=500, bg='black')
    self.seconds = 0
    self.create_grid()
    self.num = 1
    self.agent = ()
    self.create_agent()
    self.update_grid_nums()
    self.master.bind("<space>", lambda e: self.prompt_experiments())
    self.c.pack(fill=BOTH, expand=True)


  def initialize_pickup_and_dropoff(self, num):
    if num == 0:
      self.pickup1 = self.c.create_rectangle(0, 0, 100, 100, fill="sea green")
      self.pickup2 = self.c.create_rectangle(200, 200, 300, 300, fill="sea green")
      self.pickup3 = self.c.create_rectangle(400, 400, 500, 500, fill="sea green")

      self.dropoff1 = self.c.create_rectangle(400, 100, 500, 200, fill="dark orange")
      self.dropoff2 = self.c.create_rectangle(0, 400, 100, 500, fill="dark orange")
      self.dropoff3 = self.c.create_rectangle(300, 400, 200, 500, fill="dark orange")
    elif num == 1:
      self.c.coords(self.pickup1, 400, 100, 500, 200)
      self.c.itemconfig(self.pickup1, fill="sea green")
      self.c.coords(self.pickup2, 0, 400, 100, 500)
      self.c.itemconfig(self.pickup2, fill="sea green")
      self.c.coords(self.pickup3, 300, 400, 200, 500)
      self.c.itemconfig(self.pickup3, fill="sea green")

      self.c.coords(self.dropoff1, 0, 0, 100, 100)
      self.c.itemconfig(self.dropoff1, fill="dark orange")
      self.c.coords(self.dropoff2, 200, 200, 300, 300)
      self.c.itemconfig(self.dropoff2, fill="dark orange")
      self.c.coords(self.dropoff3, 400, 400, 500, 500)
      self.c.itemconfig(self.dropoff3, fill="dark orange")


  def create_grid(self):
    w = 500
    h = 500
    self.c.delete('grid_line')

    self.initialize_pickup_and_dropoff(0)

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


  def update_grid_nums(self):
    global pickup_q_table
    global dropoff_q_table
    global agent

    self.update_agent()
    self.update_active_states()

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


  def update_agent(self):
    global agent

    if agent.hasBlock():
      self.c.itemconfig(self.agent, fill="yellow", tags='Agent')
    else:
      self.c.itemconfig(self.agent, fill="cyan", tags='Agent')

  # Function deactivate cell if no blocks in pickup or dropoff cell is full
  def update_active_states(self):
    pickup_list = [self.pickup1, self.pickup2, self.pickup3]
    dropoff_list = [self.dropoff1, self.dropoff2, self.dropoff3]

    # TODO: update pickup cells when we switch
    for i in range(len(pickup_cells)):
      if pickup_cells[i].is_empty():
        self.c.itemconfig(pickup_list[i], fill="snow3")

    for i in range(len(dropoff_cells)):
      if dropoff_cells[i].is_full():
        self.c.itemconfig(dropoff_list[i], fill="snow3")

  # Resets color of pickup/dropoff cells
  def reset_cells_color(self):
    pickup_list = [self.pickup1, self.pickup2, self.pickup3]
    dropoff_list = [self.dropoff1, self.dropoff2, self.dropoff3]

    for i in range(len(pickup_list)):
      self.c.itemconfig(pickup_list[i], fill="sea green")
      self.c.itemconfig(dropoff_list[i], fill="dark orange")


  # Moves agent and update grid numbers & arrows
  def moveAndUpdateAgent(self):
    time.sleep(self.seconds)
    self.delete_nums()
    self.update_arrows()
    self.update_grid_nums()
    self.move_agent(agent.action)

    self.master.update()


  # Resets cell colors and recreates agent in top right
  def reset_world(self):
    self.update_active_states()
    self.reset_cells_color()
    self.resetAgent()
    time.sleep(1)


  # Moves agent on canvas
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
      self.reset_world()

    self.master.update()


  # Deletes and reinitializes agent
  def resetAgent(self):
    self.c.delete(self.agent)
    self.create_agent()


  # Writes output to a txt file
  def output_(self):
    file1 = open("MyFile.txt","w")
    print(bank_account_list)
    print(num_operator_list)
    file1.write(' '.join(map(str,bank_account_list)))
    file1.write('\n')
    file1.write(' '.join(map(str,num_operator_list)))


  # --------------------------------- EXPERIMENTS -------------------------------------- #
  def experiment_1(self):

    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    agent.reset()

    initialize_Q_table()
    initializeCells(pickup_states, dropoff_states)

    print("\n|---------------- RANDOM POLICY ----------------| \n")

    for index in range(4000):
      agent.policy = "PRandom"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      self.moveAndUpdateAgent()

    print("\n|---------------- GREEDY POLICY ----------------| \n")

    for index in range(4000):
      agent.policy = "PGreedy"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      self.moveAndUpdateAgent()

    print("FINISH")
    self.output_()

  def experiment_2(self):
    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    agent.reset()

    initialize_Q_table()
    initializeCells(pickup_states, dropoff_states)

    print("\n|---------------- RANDOM POLICY ----------------| \n")

    for index in range(200):
      agent.policy = "PRandom"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      self.moveAndUpdateAgent()

    print("\n|---------------- EXPLOIT POLICY ----------------| \n")

    for index in range(7800):
      agent.policy = "PExploit"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      self.moveAndUpdateAgent()

    print("FINISH")
    self.output_()

  def experiment_3(self):

    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    agent.reset()

    initialize_Q_table()
    initializeCells(pickup_states, dropoff_states)

    print("\n|---------------- RANDOM POLICY ----------------| \n")

    agent.policy = "PRandom"
    next_action = SARSA_update(learning_rate, discount_rate, None, agent, pickup_states, dropoff_states)
    for index in range(200):
      self.moveAndUpdateAgent()
      next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

    print("\n|---------------- EXPLOIT POLICY ----------------| \n")

    agent.policy = "PExploit"
    for index in range(7800):
      self.moveAndUpdateAgent()
      next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

    print("FINISHED")
    self.output_()

  def experiment_4(self):
    learning_rate = 0.3
    discount_rate = 1

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states = [[1, 4], [4, 0], [4, 2]]

    agent.reset()

    initialize_Q_table()
    initializeCells(pickup_states, dropoff_states)

    print("\n|---------------- RANDOM POLICY ----------------| \n")

    agent.policy = "PRandom"
    next_action = SARSA_update(learning_rate, discount_rate, None, agent, pickup_states, dropoff_states)
    for index in range(200):
      self.moveAndUpdateAgent()
      next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

    print("\n|---------------- EXPLOIT POLICY ----------------| \n")

    agent.policy = "PExploit"
    for index in range(7800):
      self.moveAndUpdateAgent()
      next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

    print("FINISHED")
    self.output_()

  def experiment_5(self):
    learning_rate = 0.3
    discount_rate = 0.5

    pickup_states = [[0, 0], [2, 2], [4, 4]]
    dropoff_states =  [[1, 4], [4, 0], [4, 2]]

    # new_pickup_states = [[1, 4], [4, 0], [4, 2]]
    # new_dropoff_states = [[0, 0], [2, 2], [4, 4]]

    agent.reset()

    initialize_Q_table()
    initializeCells(pickup_states, dropoff_states)

    swapped = False

    print("\n|---------------- RANDOM POLICY ----------------| \n")

    agent.policy = "PRandom"
    for index in range(200):
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      if agent.getTerminalStatesReached() == 2 and not swapped:
        print("\n|---------------- SWAPPED ----------------| \n")
        swapped = True
        pickup_states, dropoff_states = dropoff_states, pickup_states
        self.initialize_pickup_and_dropoff(1)
        initializeCells(pickup_states, dropoff_states)
      self.moveAndUpdateAgent()


    print("\n|---------------- EXPLOIT POLICY ----------------| \n")

    agent.policy = "PExploit"
    for index in range(7800):
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      if agent.getTerminalStatesReached() == 2 and not swapped:
        print("\n|---------------- SWAPPED ----------------| \n")
        swapped = True
        pickup_states, dropoff_states = dropoff_states, pickup_states
        self.initialize_pickup_and_dropoff(1)
        initializeCells(pickup_states, dropoff_states)
      self.moveAndUpdateAgent()

    print("FINISHED")
    self.output_()


  def delete_nums(self):
    self.c.delete("nums")

  def prompt_experiments(self):
    experiment_num = int(input("Choose Experiment 1 - 5 by entering the corresponding number -  \n" ))
    self.seconds = float(input("How fast do you want to the experiment to run? (From 0 to 1.0)"))
    if experiment_num == 1:
      print("|----------------Running Experiment 1----------------| \n")
      self.experiment_1()
    elif experiment_num == 2:
      print("|----------------Running Experiment 2----------------|\n")
      self.experiment_2()
    elif experiment_num == 3:
      print("|----------------Running Experiment 3----------------|\n")
      self.experiment_3()
    elif experiment_num == 4:
      print("|----------------Running Experiment 4----------------|\n")
      self.experiment_4()
    elif experiment_num == 5:
      print("|----------------Running Experiment 5----------------|\n")
      self.experiment_5()


class Main(GridWorld):
  def __init__(self):
    master = Tk()
    
    master.resizable(width=False, height=False)

    app = GridWorld(master)
    app.mainloop()


Main()
