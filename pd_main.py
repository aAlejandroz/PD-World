from agent import Agent

[None, 1, 1, None]

pickup_matrix = [[[None, -1, -1, None], [None, -1, -1, 13], [None, -1, -1, -1], [None, -1, -1, -1], [None, None, -1, -1]],
                 [[13, -1, -1, None], [-1, -1, -1, -1], [-1, -1, 13, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]],
                 [[-1, -1, -1, None], [-1, 13, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 13], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [13, -1, -1, -1], [-1, -1, -1, -1], [-1, None, 13, -1]],
                 [[-1, -1, None, None], [-1, -1, None, -1], [-1, -1, None, -1], [-1, 13, None, -1], [-1, None, None, -1]]]

q_table = [ [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],
            [0,0,0,0,0,0]]

directions = {
        0 : 'north',
        1 : 'east',
        2 : 'south',
        3 : 'east'
      }

pickup_states = [[0, 0], [2, 2], [4, 4]]

learning_rate = None
discount_rate = None

agent = Agent()
agent.policy = "PRandom"

row = agent.state_space[0]
col = agent.state_space[1]
hasBlock = agent.state_space[2]

position = [row, col]

# PRandom(row, col)

# pass in row to lookup in q-table
def PRandom(row, col):
    # if state is a pickup state, pickup
    # else choose random column based on current row.
    if (pickup_matrix[row][col] in pickup_states):
      # pickup
    else:
      # choose random action if applicable
      # for num in pickup_matrix[row][col]:
      #   if
      for row in pickup_matrix[row][col]:
        for col in pickup_matrix[row][col]:

      possible_actions = ['east', 'south']


