# class for agent
class Agent:


  def __init__(self):
    self.past_state = None
    self.state = [0, 4, 0]
    self.position = [0, 4]
    self.policy = None
    self.bank_account = 0
    self.reward = 0
    self.num_operators = 0

  def initialize(self):
    self.past_state = None
    self.state = [0, 4, 0]  # [row, column, block]
    self.position = [0, 4]
    self.bank_account = 0
    self.reward = 0
    self.num_operators = 0

  def updateRewards(self, reward):
    self.reward = reward
    self.bank_account += reward

  def updatePosition(self):
    self.position[0] = self.state[0]
    self.position[1] = self.state[1]

  def updateState(self, new_state):
    self.past_state = self.state
    self.state = new_state

  def canPickup(self):
    return self.state[2] == 0

  def hasBlock(self):
    return self.state[2] == 1