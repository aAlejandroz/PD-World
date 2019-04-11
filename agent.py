# class for agent
class Agent():

  past_state_space = [0, 4, 0]
  new_state_space = [0, 4, 0]
  policy = None
  bank_account = 0
  reward = 0
  num_operators = 0

  def __init__(self):
    state_space = [0, 4, 0] #[row, column, block]
    policy = None
    bank_account = 0
    num_operators = 0

