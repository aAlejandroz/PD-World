# class for agent
class Agent:

  past_state = None
  state = [0, 4, 0]
  position = [0, 4]
  policy = None
  bank_account = 0
  reward = 0
  num_operators = 0

  def __init__(self):
    state = [0, 4, 0] #[row, column, block]
    policy = None
    bank_account = 0
    num_operators = 0

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