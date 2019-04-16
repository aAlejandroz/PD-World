from agent import Agent
from cell_methods import *
from grid_cells import *
from policies import *
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
  RESET  = 6

# Environment matrix
environment = [[[None, -1, -1, None], [None, -1, -1, -1], [None, -1, -1, -1], [None, -1, -1, -1], [None, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, None, -1, -1]],
                 [[-1, -1, None, None], [-1, -1, None, -1], [-1, -1, None, -1], [-1, -1, None, -1], [-1, None, None, -1]]]

# Pickup q table
pickup_q_table = [ [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]]

# Dropoff q table
dropoff_q_table = [ [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]]

# agent object
agent = Agent()

pickup_cells = []   # list of pickup cells
dropoff_cells = []  # list of drop off cells

# random policy #
# returns a random number in the possible actions list
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

# decrement blocks on cell #
def decrementNumBlocksInCell(pos):
  cell = getCellFromPosition(pos, pickup_cells)
  cell.num_of_blocks -= 1


# increment blocks on cell #
def incrementNumBlocksInCell(pos):
  cell = getCellFromPosition(pos, dropoff_cells)
  cell.num_of_blocks += 1

# Initialize environment to original #
def initalizeCells(pickup_states, dropoff_states):
  pickup_cells.clear()
  dropoff_cells.clear()

  for pos in pickup_states:
    pickup_cells.append(Cells(pos, 5))

  for pos in dropoff_states:
    dropoff_cells.append(Cells(pos, 0))

# returns the cell object in the given position #
# pos = [x,y]
def getCellFromPosition(pos, cell_list):
  for cell in cell_list:
    if cell.position == pos:
      return cell

# function to initialize Q table #
def initialize_Q_table():
  global pickup_q_table, dropoff_q_table

  pickup_q_table = [
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]]

  dropoff_q_table = [
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]]

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


def isPickup(pos, pickup_states):
  return pos in pickup_states


def isDropOff(pos, dropoff_states):
  return pos in dropoff_states


# returns action enum given agent's policy and possible actions #
def getPolicyAction(agent, state, possible_actions, pickup_states, dropoff_states):
  row = state[0]
  col = state[1]
  pos = [row, col]

  # finds pickup or dropoff cell if position is a pickup or dropoff state
  if pos in pickup_states:
    cell = getCellFromPosition(pos, pickup_cells)
  elif pos in dropoff_states:
    cell = getCellFromPosition(pos, dropoff_cells)

  if pos in pickup_states and state[2] == 0 and not cell.is_empty():      # pos is pickup state, agent has no block, and cell not empty
    action = actions.PICKUP
    decrementNumBlocksInCell(pos)
    print('\nAgent picked up a block')
    print(f'Pickup cell {cell.position} = {cell.num_of_blocks}')
  elif pos in dropoff_states and state[2] == 1 and not cell.is_full():
    action = actions.DROP
    incrementNumBlocksInCell(pos)
    print('\nAgent dropped up a block')
    print(f'Drop off cell {cell.position} = {cell.num_of_blocks}')
  else:                                                 # directional move
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

def Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states):
  position = agent.position
  row = position[0]
  col = position[1]

  possible_actions = getAllPossibleNextAction(position)                                          # possible actions in state
  action = getPolicyAction(agent, agent.state, possible_actions, pickup_states, dropoff_states)  # a = action chosen in state
  agent.action = action
  next_state = getNextState(agent.state, action)                                                 # s' = next state after action is applied
  reward = calculateRewardFromAction(action)                                                     # calculate agent's rewards & bank account
  agent.updateRewards(reward)

  new_row = next_state[0]
  new_col = next_state[1]

  q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table

  old_value = q_table[row][col][action.value]

  new_pos = [new_row, new_col]

  # if pickup or drop off
  if isPickup(new_pos, pickup_states):
    cell = getCellFromPosition(new_pos, pickup_cells)
    if cell.is_empty():
      pickup_q_table[new_row][new_col] = [0,0,0,0,0,0]
  elif isDropOff(new_pos, dropoff_states):
    cell = getCellFromPosition(new_pos, dropoff_cells)
    if cell.is_full():
      dropoff_q_table[new_row][new_col] = [0,0,0,0,0,0]

  next_max = np.max(q_table[new_row][new_col])

  new_q_value = (1 - learning_rate) * old_value + learning_rate * (agent.reward + discount_rate * next_max)
  q_table[row][col][action.value] = round(new_q_value, 2)

  agent.updateState(next_state)
  agent.updatePosition()

  is_terminal = False
  val = 0

  for cell in dropoff_cells:
    val += cell.num_of_blocks
    if val == 15:
      is_terminal = True

  if is_terminal:
    agent.initialize()
    agent.action = actions.RESET
    initalizeCells(pickup_states, dropoff_states)
    print("\n-----------INITIALIZED----------")


# SARSA update, returns next action #
def SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states):
  position = agent.position
  row = position[0]
  col = position[1]

  if next_action is None:
    possible_actions = getAllPossibleNextAction(position)                                                  # possible actions in state
    action = getPolicyAction(agent, agent.state, possible_actions, pickup_states, dropoff_states)          # a = action chosen in state
  else:
    action = next_action                                                    # we know what our action is, so we chose it

  reward = calculateRewardFromAction(action)                                # calculate agent's rewards & bank account
  agent.action = action
  agent.updateRewards(reward)

  next_state = getNextState(agent.state, action)                            # s' = next state after action is applied

  new_row = next_state[0]
  new_col = next_state[1]
  new_pos = [new_row, new_col]

  # if pickup or drop off
  if isPickup(new_pos, pickup_states):
    cell = getCellFromPosition(new_pos, pickup_cells)
    if cell.is_empty():
      pickup_q_table[new_row][new_col] = [0, 0, 0, 0, 0, 0]
  elif isDropOff(new_pos, dropoff_states):
    cell = getCellFromPosition(new_pos, dropoff_cells)
    if cell.is_full():
      dropoff_q_table[new_row][new_col] = [0, 0, 0, 0, 0, 0]

  next_possible_actions = getAllPossibleNextAction(next_state)  # all possible actions in s'
  next_action = getPolicyAction(agent, next_state, next_possible_actions, pickup_states, dropoff_states)  # a' = next action in s'

  q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table
  old_value = q_table[row][col][action.value]

  new_q_value = old_value + learning_rate * (reward + discount_rate *
                                                                q_table[next_state[0]][next_state[1]][next_action.value] - old_value)

  q_table[row][col][action.value] = round(new_q_value, 2)

  agent.updateState(next_state)
  agent.updatePosition()

  is_terminal = False
  val = 0

  for cell in dropoff_cells:
    val += cell.num_of_blocks
    if val == 15:
      is_terminal = True

  if is_terminal:
    agent.initialize()
    initalizeCells(pickup_states, dropoff_states)
    print("\n-----------INITIALIZED----------")
    agent.action = actions.RESET
    return None

  return next_action


# ----------------------------- EXPERIMENTS ---------------------------- #

# def experiment_1():
#   learning_rate = 0.3
#   discount_rate = 0.5
#
#   pickup_states = [[0, 0], [2, 2], [4, 4]]
#   dropoff_states = [[1, 4], [4, 0], [4, 2]]
#
#   initialize_Q_table()
#   initalizeCells(pickup_states, dropoff_states)
#
#   for index in range(4000):
#     agent.policy = "PRandom"
#     Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
#
#   #TODO Where we display the Q_table
#
#   for index in range(4000):
#     agent.policy = "PGreedy"
#     Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
#
#   print('\n')
#
#   print("\nPickup Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(pickup_q_table[row][column], end=" ")
#     print()
#
#   print("\nDropoff Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(dropoff_q_table[row][column], end=" ")
#     print()
#
#
# def experiment_2():
#   learning_rate = 0.3
#   discount_rate = 0.5
#
#   pickup_states = [[0, 0], [2, 2], [4, 4]]
#   dropoff_states = [[1, 4], [4, 0], [4, 2]]
#
#   initialize_Q_table()
#   initalizeCells(pickup_states, dropoff_states)
#
#   for index in range(200):
#     agent.policy = "PRandom"
#     Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
#
#   # TODO Display and interpret the Q-table
#
#   for index in range(7800):
#     agent.policy = "PExploit"
#     Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
#
#   print("\nPickup Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(pickup_q_table[row][column], end=" ")
#     print()
#
#   print("\nDropoff Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(dropoff_q_table[row][column], end=" ")
#     print()
#
#
# def experiment_3():
#   learning_rate = 0.3
#   discount_rate = 0.5
#
#   pickup_states = [[0, 0], [2, 2], [4, 4]]
#   dropoff_states = [[1, 4], [4, 0], [4, 2]]
#
#   initialize_Q_table()
#   initalizeCells(pickup_states, dropoff_states)
#
#   agent.policy = "PRandom"
#   next_action = SARSA_update(learning_rate, discount_rate, None, agent, pickup_states, dropoff_states)
#   for index in range(200):
#     next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)
#
#   # TODO Display and interpret the Q-table
#
#   for index in range(7800):
#     agent.policy = "PExploit"
#     next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)
#
#   #TODO final Q_table
#
#   print("\nPickup Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(pickup_q_table[row][column], end=" ")
#     print()
#
#   print("\nDropoff Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(dropoff_q_table[row][column], end=" ")
#     print()
#
#
# def experiments_4():
#   learning_rate = 0.3
#   discount_rate = 1
#
#   pickup_states = [[0, 0], [2, 2], [4, 4]]
#   dropoff_states = [[1, 4], [4, 0], [4, 2]]
#
#   initialize_Q_table()
#   initalizeCells(pickup_states, dropoff_states)
#
#   agent.policy = "PRandom"
#   next_action = SARSA_update(learning_rate, discount_rate, None, agent, pickup_states, dropoff_states)
#   for index in range(200):
#     next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)
#
#   # TODO Display and interpret the Q-table
#
#   for index in range(7800):
#     agent.policy = "PExploit"
#     next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)
#
#   # TODO final Q_table
#
#   print("\nPickup Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(pickup_q_table[row][column], end=" ")
#     print()
#
#   print("\nDropoff Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(dropoff_q_table[row][column], end=" ")
#     print()
#
#
# def experiment_5():
#   learning_rate = 0.3
#   discount_rate = 0.5
#
#   pickup_states =  [[1, 4], [4, 0], [4, 2]]
#   dropoff_states = [[0, 0], [2, 2], [4, 4]]
#
#   initialize_Q_table()
#   initalizeCells(pickup_states, dropoff_states)
#
#   for index in range(200):
#     agent.policy = "PRandom"
#     Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
#
#   # TODO Display and interpret the Q-table
#
#   for index in range(7800):
#     agent.policy = "PExploit"
#     Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)
#
#   print("\nPickup Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(pickup_q_table[row][column], end=" ")
#     print()
#
#   print("\nDropoff Q TABLE")
#   for row in range(5):
#     for column in range(5):
#       print(dropoff_q_table[row][column], end=" ")
#     print()

#--------- MAIN ----------#
# if __name__ == '__main__':
#
#   while True:
#
#     try:
#       experiment_num = int(input("Choose Experiment 1 - 5 by entering the corresponding number -  \n" ))
#
#     except ValueError:
#       print("Did not enter a number. Try again")
#     else:
#       if experiment_num == 1:
#         print("|----------------Running Experiment 1----------------| \n")
#         experiment_1()
#       elif experiment_num == 2:
#         print("|----------------Running Experiment 2----------------|\n")
#         experiment_2()
#       elif experiment_num == 3:
#         print("|----------------Running Experiment 3----------------|\n")
#         experiment_3()
#       elif experiment_num == 4:
#         print("|----------------Running Experiment 4----------------|\n")
#         experiments_4()
#       elif experiment_num == 5:
#         print("|----------------Running Experiment 5----------------|\n")
#         experiment_5()
#
#       print()
#

