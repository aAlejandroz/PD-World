from agent import Agent
from policies import *
from cell_methods import *
from RL_updates import *
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

agent = Agent()

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
def getPolicyAction(agent, state, possible_actions, pickup_states, dropoff_states):
  row = state[0]
  col = state[1]
  pos = [row, col]

  # finds pickup or dropoff cell if position is a pickup or dropoff state
  if pos in pickup_states:
    cell = getCellFromPosition(pos, pickup_cells)
  elif pos in dropoff_states:
    cell = getCellFromPosition(pos, dropoff_cells)

  if pos in pickup_states and state[2] == 0 and not cell.is_empty():
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
  next_state = getNextState(agent.state, action)                                                 # s' = next state after action is applied
  reward = calculateRewardFromAction(action)                                                     # calculate agent's rewards & bank account
  agent.updateRewards(reward)

  new_row = next_state[0]
  new_col = next_state[1]

  q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table

  old_value = q_table[row][col][action.value]
  next_max = np.max(q_table[new_row][new_col])
  new_q_value = (1 - learning_rate) * old_value + learning_rate * (agent.reward + discount_rate * next_max)
  q_table[row][col][action.value] = new_q_value

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
  agent.updateRewards(reward)

  next_state = getNextState(agent.state, action)                            # s' = next state after action is applied
  next_possible_actions = getAllPossibleNextAction(next_state)              # all possible actions in s'
  next_action = getPolicyAction(agent, next_state, next_possible_actions, pickup_states, dropoff_states)   # a' = next action in s'

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

  pickup_states = [[0, 0], [2, 2], [4, 4]]
  dropoff_states = [[1, 4], [4, 0], [4, 2]]

  initalizeCells(pickup_states, dropoff_states)

  for index in range(4000):
    agent.policy = "PRandom"
    Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)

  #TODO Where we display the Q_table

  for index in range(4000):
    agent.policy = "PGreedy"
    Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)

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

  pickup_states = [[0, 0], [2, 2], [4, 4]]
  dropoff_states = [[1, 4], [4, 0], [4, 2]]

  initalizeCells(pickup_states, dropoff_states)

  for index in range(200):
    agent.policy = "PRandom"
    Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)


def experiment_3():
  learning_rate = 0.3
  discount_rate = 0.5

  pickup_states = [[0, 0], [2, 2], [4, 4]]
  dropoff_states = [[1, 4], [4, 0], [4, 2]]

  initalizeCells(pickup_states, dropoff_states)

  agent.policy = "PRandom"
  next_action = SARSA_update(learning_rate, discount_rate, None, agent, pickup_states, dropoff_states)
  for index in range(200):
    next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

  #TODO final Q_table

def experiments_4():
  learning_rate = 0.3
  discount_rate = 1

  pickup_states = [[0, 0], [2, 2], [4, 4]]
  dropoff_states = [[1, 4], [4, 0], [4, 2]]

  initalizeCells(pickup_states, dropoff_states)

  agent.policy = "PRandom"
  next_action = SARSA_update(learning_rate, discount_rate, None, agent, pickup_states, dropoff_states)
  for index in range(200):
    next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    next_action = SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states)

  # TODO final Q_table


def experiment_5():
  learning_rate = 0.3
  discount_rate = 0.5

  pickup_states =  [[1, 4], [4, 0], [4, 2]]
  dropoff_states = [[0, 0], [2, 2], [4, 4]]

  initalizeCells(pickup_states, dropoff_states)

  for index in range(200):
    agent.policy = "PRandom"
    Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states)


#--------- MAIN ----------#
if __name__ == '__main__':

  while True:

    try:
      experiment_num = int(input("Choose Experiment 1 - 5 by entering the corresponding number -  \n" ))

    except ValueError:
      print("Did not enter a number. Try again")
    else:
      if experiment_num == 1:
        print("|----------------Running Experiment 1----------------| \n")
        experiment_1()
      elif experiment_num == 2:
        print("|----------------Running Experiment 2----------------|\n")
        experiment_2()
      elif experiment_num == 3:
        print("|----------------Running Experiment 3----------------|\n")
        experiment_3()
      elif experiment_num == 4:
        print("|----------------Running Experiment 4----------------|\n")
        experiments_4()
      elif experiment_num == 5:
        print("|----------------Running Experiment 5----------------|\n")
        experiment_5()

      print()


