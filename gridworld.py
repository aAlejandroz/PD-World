# import tkinter as tk
# import numpy as np
# import time
#
# class Gridworld:
#
#   def __init__(self, gamma=0.9, alpha=0.5, epsilon=0.01):
#
#     self.root = tk
#     #self.frame = self.root.Canvas(bg='black', height=400, width=500)
#     self.frame = self.root.Canvas(bg='black', height=600, width=600)
#     self.frame.pack()
#     self.gamma = gamma
#     self.alpha = alpha
#     self.epsilon = epsilon
#     self.sr = []
#     self.agent = ()
#     self.move = ()
#
#   def reward_table(self):
#     s = 0
#     x = 11
#     y = 5
#
#     self.sr = np.zeros([x, y], dtype=np.object)
#     for x in range(11):
#       self.sr[:, 1:] = float(0)
#       self.sr[x][0] = s
#       s = s + 1
#
#     """Just delete any line below to see what it codes for"""
#
#   def grid(self):
#
#     self.reward_table()
#
#     # self.frame.create_rectangle(30, 30, 470, 360, fill='sea green')
#     # self.frame.create_rectangle(360, 140, 470, 250, fill='red')
#
#     # Column 4 north
#     self.frame.create_text(415, 40, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 4 east
#     self.frame.create_text(455, 85, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 4 south
#     self.frame.create_text(415, 130, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 4 west
#     self.frame.create_text(375, 85, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#
#     # self.frame.create_text(415, 85, text=self.sr[0][4], font="Verdana 10 bold", fill='white')
#     self.frame.create_polygon(250, 30, 360, 30, 305, 85, 250, 30, fill='black')
#     self.frame.create_text(305, 42, text=self.sr[1][1], font="Verdana 10 bold", fill='white')
#
#     # column 3 south
#     self.frame.create_polygon(250, 140, 360, 140, 305, 85, 250, 140, fill='black')
#     self.frame.create_text(305, 130, text=self.sr[1][2], font="Verdana 10 bold", fill='white')
#
#     # Column 5 south
#     self.frame.create_text(525, 130, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 5 west
#     self.frame.create_text(485, 85, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 5 east
#     self.frame.create_text(565, 85, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 5 north
#     self.frame.create_text(525, 45, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#
#
#     # Column 2 north
#     self.frame.create_text(195, 150, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 2 east
#     self.frame.create_text(235, 195, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 2 south
#     self.frame.create_text(195, 240, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#     # Column 2 east
#     self.frame.create_text(155, 195, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#
#
#
#     self.frame.create_polygon(250, 30, 250, 140, 305, 85, 250, 30, fill='black')
#     self.frame.create_text(265, 85, text=self.sr[1][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(360, 30, 360, 140, 305, 85, 360, 30, fill='black')
#     self.frame.create_text(345, 85, text=self.sr[1][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 30, 250, 30, 195, 85, 140, 30, fill='black')
#     self.frame.create_text(195, 42, text=self.sr[2][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 140, 250, 140, 195, 85, 140, 140, fill='black')
#     self.frame.create_text(195, 130, text=self.sr[2][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 30, 140, 140, 195, 85, 140, 30, fill='black')
#     self.frame.create_text(155, 85, text=self.sr[2][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(250, 30, 250, 140, 195, 85, 250, 30, fill='black')
#     self.frame.create_text(235, 85, text=self.sr[2][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 30, 140, 30, 85, 85, 30, 30, fill='black')
#     self.frame.create_text(85, 42, text=self.sr[3][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 140, 140, 140, 85, 85, 30, 140, fill='black')
#     self.frame.create_text(85, 130, text=self.sr[3][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 30, 30, 140, 85, 85, 30, 30, fill='black')
#     self.frame.create_text(48, 85, text=self.sr[3][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 30, 140, 140, 85, 85, 140, 30, fill='black')
#     self.frame.create_text(125, 85, text=self.sr[3][4], font="Verdana 10 bold", fill='white')
#
#
#     self.frame.create_text(305, 150, text=self.sr[5][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(250, 250, 360, 250, 305, 195, 250, 250, fill='black')
#     self.frame.create_text(305, 240, text=self.sr[5][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(250, 140, 250, 250, 305, 195, 250, 140, fill='black')
#     self.frame.create_text(265, 195, text=self.sr[5][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(360, 140, 360, 250, 305, 195, 360, 140, fill='black')
#     self.frame.create_text(345, 195, text=self.sr[5][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 140, 140, 140, 85, 195, 30, 140, fill='black')
#     self.frame.create_text(85, 150, text=self.sr[6][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 250, 140, 250, 85, 195, 30, 250, fill='black')
#     self.frame.create_text(85, 240, text=self.sr[6][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 140, 30, 250, 85, 195, 30, 140, fill='black')
#     self.frame.create_text(48, 195, text=self.sr[6][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 140, 140, 250, 85, 195, 140, 140, fill='black')
#     self.frame.create_text(124, 195, text=self.sr[6][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(360, 250, 470, 250, 415, 305, 360, 250, fill='black')
#     self.frame.create_text(415, 260, text=self.sr[7][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(360, 360, 470, 360, 415, 305, 360, 360, fill='black')
#     self.frame.create_text(415, 350, text=self.sr[7][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(360, 250, 360, 360, 415, 305, 360, 250, fill='black')
#     self.frame.create_text(375, 305, text=self.sr[7][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(470, 250, 470, 360, 415, 305, 470, 250, fill='black')
#     self.frame.create_text(453, 305, text=self.sr[7][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(250, 250, 360, 250, 305, 305, 250, 250, fill='black')
#     self.frame.create_text(305, 260, text=self.sr[8][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(250, 360, 360, 360, 305, 305, 250, 360, fill='black')
#     self.frame.create_text(305, 350, text=self.sr[8][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(250, 250, 250, 360, 305, 305, 250, 250, fill='black')
#     self.frame.create_text(265, 305, text=self.sr[8][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(360, 250, 360, 360, 305, 305, 360, 250, fill='black')
#     self.frame.create_text(345, 305, text=self.sr[8][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 250, 250, 250, 195, 305, 140, 250, fill='black')
#     self.frame.create_text(195, 260, text=self.sr[9][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 360, 250, 360, 195, 305, 140, 360, fill='black')
#     self.frame.create_text(195, 350, text=self.sr[9][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 250, 140, 360, 195, 305, 140, 250, fill='black')
#     self.frame.create_text(155, 305, text=self.sr[9][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(250, 250, 250, 360, 195, 305, 250, 250, fill='black')
#     self.frame.create_text(235, 305, text=self.sr[9][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 250, 140, 250, 85, 305, 30, 250, fill='black')
#     self.frame.create_text(85, 260, text=self.sr[10][1], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 360, 140, 360, 85, 305, 30, 360, fill='black')
#     self.frame.create_text(85, 350, text=self.sr[10][2], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(30, 250, 30, 360, 85, 305, 30, 250, fill='black')
#     self.frame.create_text(47, 305, text=self.sr[10][3], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_polygon(140, 250, 140, 360, 85, 305, 140, 250, fill='black')
#     self.frame.create_text(125, 305, text=self.sr[10][4], font="Verdana 10 bold", fill='white')
#
#     self.frame.create_line(28, 30, 580, 30, 580, 580, 30, 580, 30, 30, fill='white', width=5)
#     self.frame.create_line(30, 140, 580, 140, fill='white', width=2)
#     self.frame.create_line(30, 250, 580, 250, fill='white', width=2)
#     self.frame.create_line(30, 360, 580, 360, fill='white', width=2)
#     self.frame.create_line(30, 470, 580, 470, fill='white', width=2)
#     self.frame.create_line(140, 30, 140, 580, fill='white', width=2)
#     self.frame.create_line(250, 30, 250, 580, fill='white', width=2)
#     self.frame.create_line(360, 30, 360, 580, fill='white', width=2)
#     self.frame.create_line(470, 30, 470, 580, fill='white', width=2)
#     self.frame.create_line(30, 250, 140, 360, fill='white', width=2)
#     self.frame.create_line(30, 140, 250, 360, fill='white', width=2)
#     self.frame.create_line(30, 30, 140, 140, fill='white', width=2)
#     self.frame.create_line(140, 30, 470, 360, fill='white', width=2)
#     self.frame.create_line(250, 30, 360, 140, fill='white', width=2)
#     self.frame.create_line(250, 250, 360, 360, fill='white', width=2)
#     self.frame.create_line(140, 30, 30, 140, fill='white', width=2)
#     self.frame.create_line(250, 30, 30, 250, fill='white', width=2)
#     self.frame.create_line(360, 30, 250, 140, fill='white', width=2)
#     self.frame.create_line(140, 250, 30, 360, fill='white', width=2)
#     self.frame.create_line(360, 30, 250, 140, fill='white', width=2)
#     self.frame.create_line(360, 140, 140, 360, fill='white', width=2)
#     self.frame.create_line(360, 250, 250, 360, fill='white', width=2)
#     self.frame.create_line(470, 250, 360, 360, fill='white', width=2)
#     # self.agent = self.frame.create_oval(290, 70, 320, 100, fill='cyan')
#     # self.agent = self.frame.create_oval(180, 70, 210, 100, fill='cyan')
#     # self.agent = self.frame.create_oval(70, 70, 100, 100, fill='cyan')
#     self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
#     self.frame.update()
#
#     """epsilon determines the degree of exploration (high) versus exploitation (high)"""
#
#   def get_action(self):
#     previous_state = 10
#     choice = np.random.uniform()
#     if choice < self.epsilon:
#       for i in range(11):
#         if self.sr[i, 0] == previous_state:
#           s = self.sr[i]
#           state_rewards = s[1:]
#           state_rewards = state_rewards.tolist()
#           maxq = state_rewards.index(max(state_rewards))
#           move = ['up', 'down', 'left', 'right']
#           self.move = move[maxq]
#           if state_rewards[state_rewards.index(max(state_rewards))] == 0:
#             self.move = np.random.choice(['up', 'down', 'left', 'right'])
#     else:
#       self.move = np.random.choice(['up', 'down', 'left', 'right'])
#
#   def reset(self):
#     self.frame.delete(self.agent)
#     self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
#     # self.agent = self.frame.create_oval(70, 70, 100, 100, fill='cyan')
#     # self.agent = self.frame.create_oval(180, 70, 210, 100, fill='cyan')
#     # self.frame.create_oval(290, 70, 320, 100, fill='cyan')
#     self.frame.update()
#
#   def move_agent(self):
#
#     coords = [[70, 290], [180, 290], [290, 290], [400, 290], [70, 180], [290, 180], [400, 180], [70, 70],
#               [180, 70], [290, 70], [400, 70]]
#     self.grid()
#     time.sleep(0.5)
#
#     for i in range(1, 20):
#       time.sleep(0.1)
#       s = self.frame.coords(self.agent)
#       previous_state_coords = [int(s[0]), int(s[1])]
#       for x in range(len(coords)):
#         if coords[x] == previous_state_coords:
#           previous_state = (len(coords) - 1) - x
#       self.get_action()
#       move = self.move
#       if move == 'up':
#         if s[0] == 70:
#           if s[1] > 70:
#             move_agent = np.array([0, -110])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#         if s[0] == 290:
#           if s[1] > 70:
#             move_agent = np.array([0, -110])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#         if s[0] == 400:
#           if s[1] > 70:
#             move_agent = np.array([0, -110])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#             time.sleep(0.5)
#             if s[0] == 400:
#               self.reset()
#       if move == 'right':
#         if s[1] == 290:
#           if s[0] < 291:
#             move_agent = np.array([110, 0])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#         if s[1] == 70:
#           if s[0] < 291:
#             move_agent = np.array([110, 0])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#             if s[0] == 400:
#               time.sleep(0.5)
#               self.reset()
#         if s[1] == 180:
#           if s[0] == 290:
#             move_agent = np.array([110, 0])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#           if s[0] == 400:
#             time.sleep(0.5)
#             self.reset()
#       if move == 'left':
#         if s[1] == 290:
#           if s[0] > 70:
#             move_agent = np.array([-110, 0])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#         if s[1] == 70:
#           if s[0] > 70:
#             move_agent = np.array([-110, 0])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#       if move == 'down':
#         if s[0] == 70:
#           if s[1] < 290:
#             move_agent = np.array([0, 110])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#         if s[0] == 290:
#           if s[1] < 290:
#             move_agent = np.array([0, 110])
#             self.frame.move(self.agent, move_agent[0], move_agent[1])
#             s = self.frame.coords(self.agent)
#             self.frame.update()
#       current_state_coords = [int(s[0]), int(s[1])]
#       for x in range(len(coords)):
#         if coords[x] == current_state_coords:
#           current_state = (len(coords) - 1) - x
#
#     self.root.mainloop()
#
# data = Gridworld()
#
# # data.__init__()
# #data.reward_table()
# # data.grid()
# data.move_agent()


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
    self.init_zeros()
    self.create_grid()
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
    row = 0
    column = 0
    y_coordinate = 0
    self.c.create_rectangle(0, 0, 100, 100, fill="sea green")
    self.c.create_rectangle(200, 200, 300, 300, fill="sea green")
    self.c.create_rectangle(400, 400, 500, 500, fill="sea green")

    self.c.create_rectangle(400, 100, 500, 200, fill="dark orange")
    self.c.create_rectangle(300, 400, 200, 500, fill="dark orange")
    self.c.create_rectangle(0, 400, 100, 500, fill="dark orange")
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=pickup_q_table[row][column][0], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text=pickup_q_table[row][column][1], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text=pickup_q_table[row][column][2], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text=pickup_q_table[row][column][3], font="Verdana 8 bold",
                         fill='white')
      column += 1
    y_coordinate = 100
    row = 1
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=pickup_q_table[row][column][0], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text=pickup_q_table[row][column][1], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text=pickup_q_table[row][column][2], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text=pickup_q_table[row][column][3], font="Verdana 8 bold",
                         fill='white')
      column += 1
    y_coordinate = 200
    row = 2
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=pickup_q_table[row][column][0], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text=pickup_q_table[row][column][1], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text=pickup_q_table[row][column][2], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text=pickup_q_table[row][column][3], font="Verdana 8 bold",
                         fill='white')
      column += 1
    y_coordinate = 300
    row = 3
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=pickup_q_table[row][column][0], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text=pickup_q_table[row][column][1], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text=pickup_q_table[row][column][2], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text=pickup_q_table[row][column][3], font="Verdana 8 bold",
                         fill='white')
      column += 1
    y_coordinate = 400
    row = 4
    column = 0
    for i in range(0, 500, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text=pickup_q_table[row][column][0], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text=pickup_q_table[row][column][1], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text=pickup_q_table[row][column][2], font="Verdana 8 bold",
                         fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text=pickup_q_table[row][column][3], font="Verdana 8 bold",
                         fill='white')
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

    initialize_Q_table()
    initalizeCells(pickup_states, dropoff_states)

    for index in range(4000):
      agent.policy = "PRandom"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      self.update_gird_numbs()
      self.master.update()

    # TODO Where we display the Q_table

    for index in range(4000):
      agent.policy = "PGreedy"
      Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
      self.update_gird_numbs()

  def move_agent(self):
    for i in range(4):
      time.sleep(0.4)
      self.c.move(self.agent_data['item'], -100, 100)
      self.master.update()


class Main(GridWorld):
  def __init__(self):
    master = Tk()

    master.resizable(width=False, height=False)

    app = GridWorld(master)
    app.mainloop()


Main()
