from agent import Agent
import random

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
        3 : 'west'
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

# TODO: pass in row to lookup in q-table
def PRandom(row, col, agent):
    if (pickup_matrix[row][col] in pickup_states):
      agent.state_space[2] = 1       # pickup
      # TODO: decrement blocks on space
    else:
      possible_actions = []

      for i in range(4):
        if pickup_matrix[row][col][i] != None:
          possible_actions.append(i)

      choice = random.choice(possible_actions)
      direction = directions.get(choice)

      if direction == "north":
        agent.state_space[0] -= 1
      elif direction == "east":
        agent.state_space[1] += 1
      elif direction == "south":
        agent.state_space[0] += 1
      elif direction == "west":
        agent.state_space[1] -= 1

# print("Current position: ", agent.state_space)
# PRandom(row,col,agent)
# print("New position: ", agent.state_space)