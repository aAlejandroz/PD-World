from agent import Agent
from grid_cells import Cells
import random
import copy
import enum
import numpy as np

# creating enumerations using class
class actions(enum.Enum):
  NORTH  = 0
  EAST   = 1
  SOUTH  = 2
  WEST   = 3
  PICKUP = 4
  DROP   = 5

environment = [[[None, -1, -1, None], [None, -1, -1, -1], [None, -1, -1, -1], [None, -1, -1, -1], [None, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, None, -1, -1]],
                 [[-1, -1, None, None], [-1, -1, None, -1], [-1, -1, None, -1], [-1, -1, None, -1], [-1, None, None, -1]]]

pickup_q_table = [ [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]]

dropoff_q_table = [ [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]]

pickup_states = [[0, 0], [2, 2], [4, 4]]
dropoff_states = [[1,4], [4, 0], [4, 2]]
pickup_cells = []   # list of pickup cells
dropoff_cells = []  # list of drop off cells

for pos in pickup_states:
  pickup_cells.append(Cells(pos, 5))

for pos in pickup_states:
  dropoff_cells.append(Cells(pos, 0))

agent = Agent()

learning_rate = 0.5
discount_rate = 1

# ------------------- DECREMENT/INCREMENT BLOCK COUNT ON CELL ------------------- #

# decrement blocks on cell #
def decrementNumBlocksInCell(pos):
  for cell in pickup_cells:
    if cell.position == pos:
      cell.num_of_blocks -= 1
      return


# increment blocks on cell #
def incrementNumBlocksInCell(pos):
  for cell in dropoff_cells:
    if cell.position == pos:
      cell.num_of_blocks += 1
      return

# --------------------------------- POLICIES --------------------------------- #

# random policy #
def PRandom(possible_actions):
  return random.choice(possible_actions)


# exploit policy #
def PExploit(possible_actions, agent, row, col):
  duplicate = []

  q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table

  # choose action with best q-value 80% of the time
  if random.random() <= 0.8:
    max_action = possible_actions[0]
    for num in possible_actions:
      q_value = q_table[row][col][num]
      max_q_value = q_table[row][col][max_action]

      if q_value > max_q_value:
        max_action = num
        duplicate.clear()
        duplicate.append(num)
      if q_value == max_q_value:
        duplicate.append(num)

    exploit_choice = random.choice(duplicate) if len(duplicate) > 1 else max_action
  else:
    exploit_choice = random.choice(possible_actions)

  return exploit_choice


# greedy policy #
def PGreedy(possible_actions, agent, row, col):
  duplicate = []

  q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table

  # choose action with best q-value 100% of the time
  max_action = possible_actions[0]
  for num in possible_actions:
    q_value = q_table[row][col][num]
    max_q_value = q_table[row][col][max_action]

    if q_value > max_q_value:
      max_action = num
      duplicate.clear()
      duplicate.append(num)
    if q_value == max_q_value:
      duplicate.append(num)

  greedy_choice = random.choice(duplicate) if len(duplicate) > 1 else max_action

  return greedy_choice

# ------------------------------ HELPER FUNCTIONS ------------------------------- #

# calculates reward from action #
def calculateRewardFromAction(action):
  negative_reward = ["NORTH", "EAST", "SOUTH", "WEST"]
  positive_reward = ["PICKUP", "DROP"]

  operator = action.name

  if operator in negative_reward:
    reward = -1
  if operator in positive_reward:
    reward = 13

  return reward


# returns action enum given agent's policy and possible actions #
def getPolicyAction(agent, state, possible_actions):
  row = state[0]
  col = state[1]
  pos = [row, col]

  if pos in pickup_states and state[2] == 0:      # pickup
    action = actions.PICKUP
    decrementNumBlocksInCell(pos)
  elif pos in dropoff_states and state[2] == 1:   # drop off
    action = actions.DROP
    incrementNumBlocksInCell(pos)
  else:                                           # directional move
    if agent.policy == "PRandom":
      action = actions(PRandom(possible_actions))
    if agent.policy == "PExploit":
      action = actions(PExploit(possible_actions, agent, row, col))
    if agent.policy == "PGreedy":
      action = actions(PGreedy(possible_actions, agent, row, col))

  agent.num_operators += 1

  return action


# returns new state when action is applied to old state #
def getNextState(old_state, action):
  new_state = copy.deepcopy(old_state)

  if action.name == "NORTH":
    new_state[0] -= 1
  elif action.name == "EAST":
    new_state[1] += 1
  elif action.name == "SOUTH":
    new_state[0] += 1
  elif action.name == "WEST":
    new_state[1] -= 1
  elif action.name == "PICKUP":
    new_state[2] = 1
  elif action.name == "DROP":
    new_state[2] = 0

  return new_state


# returns list of all possible action in a given position #
def getAllPossibleNextAction(position):
  row = position[0]
  col = position[1]

  possible_actions = []

  for i in range(4):
    if environment[row][col][i] != None:
      possible_actions.append(i)

  return (possible_actions)

# ------------------------- REINFORCEMENT LEARNING UPDATES ------------------------- #

# Q Learning update #
def Q_learning(learning_rate, discount_rate, agent):
  position = agent.position
  row = position[0]
  col = position[1]

  possible_actions = getAllPossibleNextAction(position)           # possible actions in state
  action = getPolicyAction(agent, agent.state, possible_actions)  # a = action chosen in state
  next_state = getNextState(agent.state, action)                  # s' = next state after action is applied
  reward = calculateRewardFromAction(action)                      # calculate agent's rewards & bank account
  agent.updateRewards(reward)

  new_row = next_state[0]
  new_col = next_state[1]

  q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table

  old_value = q_table[row][col][action.value]
  next_max = np.max(q_table[new_row][new_col])
  new_q_value = (1 - learning_rate) * old_value + learning_rate * (agent.reward + discount_rate * next_max)
  q_table[row][col][action.value] = new_q_value

  #print(f'Q({action.name}, {agent.state}) = {pickup_q_table[row][col][action.value]}')

  agent.updateState(next_state)
  agent.updatePosition()


# SARSA update, returns next action #
def SARSA_update(learning_rate, discount_rate, next_action, agent):
  position = agent.position
  row = position[0]
  col = position[1]

  if next_action is None:
    possible_actions = getAllPossibleNextAction(position)                   # possible actions in state
    action = getPolicyAction(agent, agent.state, possible_actions)          # a = action chosen in state
  else:
    action = next_action                                                    # we know what our action is, so we chose it

  reward = calculateRewardFromAction(action)                                # calculate agent's rewards & bank account
  agent.updateRewards(reward)

  next_state = getNextState(agent.state, action)                            # s' = next state after action is applied
  next_possible_actions = getAllPossibleNextAction(next_state)              # all possible actions in s'
  next_action = getPolicyAction(agent, next_state, next_possible_actions)   # a' = next action in s'

  q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table
  q_value = q_table[row][col][action.value]

  q_table[row][col][action.value] = q_value + learning_rate * (reward + discount_rate *
                                                                q_table[next_state[0]][next_state[1]][next_action.value] - q_value)

  agent.updateState(next_state)
  agent.updatePosition()

  return next_action

# ----------------------------- EXPERIMENTS ---------------------------- #

def experiment_1():
  learning_rate = 0.3
  discount_rate = 0.5

  for index in range(4000):
    agent.policy = "PRandom"
    Q_learning(learning_rate, discount_rate, agent)

  #TODO Where we display the Q_table

  for index in range(4000):
    agent.policy = "PGreedy"
    Q_learning(learning_rate, discount_rate, agent)

  print('\n')

  print("Pickup Q TABLE")
  for row in range(5):
    for column in range(5):
      print(pickup_q_table[row][column], end=" ")
    print()

  print("\nDropoff Q TABLE")
  for row in range(5):
    for column in range(5):
      print(dropoff_q_table[row][column], end=" ")
    print()


def experiment_2():
  learning_rate = 0.3
  discount_rate = 0.5

  for index in range(200):
    agent.policy = "PRandom"
    Q_learning(learning_rate,discount_rate,agent)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    Q_learning(learning_rate,discount_rate,agent)

def experiment_3():
  learning_rate = 0.3
  discount_rate = 0.5

  agent.policy = "PRandom"
  next_action = SARSA_update(learning_rate, discount_rate, None, agent)
  for index in range(200):
    next_action = SARSA_update(learning_rate, discount_rate, next_action,agent)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    next_action = SARSA_update(learning_rate, discount_rate, next_action ,agent)

  #TODO final Q_table

def experiments_4():
  learning_rate = 0.3
  discount_rate = 1

  agent.policy = "PRandom"
  next_action = SARSA_update(learning_rate, discount_rate, None, agent)
  for index in range(200):
    next_action = SARSA_update(learning_rate, discount_rate, next_action, agent)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    next_action = SARSA_update(learning_rate, discount_rate, next_action, agent)

  # TODO final Q_table


def experiment_5():
  pass



#--------- MAIN ----------#
if __name__ == '__main__':
  print()
  experiment_1()
