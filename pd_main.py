from agent import Agent
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

pickup_matrix = [[[None, -1, -1, None], [None, -1, -1, -1], [None, -1, -1, -1], [None, -1, -1, -1], [None, None, -1, -1]],
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


# 25 states with 6 actions
# new_pickup_q_table = np.zeros([25,6])
pickup_states = [[0, 0], [2, 2], [4, 4]]
dropoff_states = [[1,4], [4, 0], [4, 2]]

learning_rate = 0.5
discount_rate = 1

agent = Agent()

# returns action enum given agent's policy and possible actions
def getPolicyAction(agent, state, possible_actions):
  row = state[0]
  col = state[1]
  pos = [row, col]

  if pos in pickup_states and state[2] == 0:      # Pickup
    action = actions.PICKUP
    agent.bank_account += 13
    reward = 13
    # TODO: decrement blocks on pick up space
  elif pos in dropoff_states and state[2] == 1:   # Dropoff
    action = actions.DROP
    agent.bank_account += 13
    reward = 13
    # TODO: increment blocks on drop off space
  else:
    if agent.policy == "PRandom":
      action = actions(PRandom(possible_actions))
    if agent.policy == "PExploit":
      action = actions(PExploit(possible_actions, row, col))
    if agent.policy == "PGreedy":
      action = actions(PGreedy(possible_actions, row, col))

    agent.bank_account -= 1
    reward = -1

  agent.reward = reward
  agent.num_operators += 1

  return action


# returns new state when action is applied to old state
def getNextState(agent, old_state, action):
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

  # agent.updateState(new_state)
  return new_state


# returns all possible action in a given position
def getAllPossibleNextAction(position):
  row = position[0]
  col = position[1]

  possible_actions = []

  for i in range(4):
    if pickup_matrix[row][col][i] != None:
      possible_actions.append(i)

  return (possible_actions)


# random policy
def PRandom(possible_actions):
  randomChoice = random.choice(possible_actions)
  return randomChoice


# exploit policy
def PExploit(possible_actions, row, col):
  duplicate = []
  if random.random() <= 0.8:
    max_action = possible_actions[0]  # max_q_value is first action in possible_actions
    for num in possible_actions:
      q_value = pickup_q_table[row][col][num]
      cur_q_max = pickup_q_table[row][col][max_action]
      if q_value > cur_q_max:
        max_action = num
        duplicate.clear()
        duplicate.append(num)
      elif q_value == cur_q_max:
        duplicate.append(num)

    exploit_choice = max_action

    if (len(duplicate) > 1):
      exploit_choice = random.choice(duplicate)
  else:
    exploit_choice = random.choice(possible_actions)

  return exploit_choice


# greedy policy
def PGreedy(possible_actions, row, col):
  duplicate = []

  max_action = possible_actions[0]
  for num in possible_actions:
    q_value = pickup_q_table[row][col][num]
    cur_q_max = pickup_q_table[row][col][max_action]
    if q_value > cur_q_max:
      max_action = num
      duplicate.clear()
      duplicate.append(num)
    elif q_value == cur_q_max:
      duplicate.append(num)

  greedy_choice = max_action

  if (len(duplicate) > 1):
    greedy_choice = random.choice(duplicate)

  return greedy_choice


# updates q-value in q-table, returns next action
def SARSA_update(learning_rate, discount_rate, next_action, agent):
  row = agent.position[0]
  col = agent.position[1]
  position = agent.position

  if next_action is None:
    possible_actions = getAllPossibleNextAction(position)                   # possible actions in state
    action = getPolicyAction(agent, agent.state, possible_actions)          # a = action chosen in state
  else:
    action = next_action                                                    # we know what our action is, so we chose it

  next_state = getNextState(agent, agent.state, action)                     # s' = next state after action is applied
  reward = agent.reward
  next_possible_actions = getAllPossibleNextAction(next_state)              # all possible actions in s'
  next_action = getPolicyAction(agent, next_state, next_possible_actions)   # a' = next action in s'

  if (not agent.hasBlock()):
    Q_value = pickup_q_table[row][col][action.value]
    pickup_q_table[row][col][action.value] = Q_value + learning_rate * (reward + discount_rate *
                                                                        pickup_q_table[next_state[0]][next_state[1]][
                                                                          next_action.value] - Q_value)
  else:
    Q_value = dropoff_q_table[row][col][action.value]
    dropoff_q_table[row][col][action.value] = Q_value + learning_rate * (reward + discount_rate *
                                                                        dropoff_q_table[next_state[0]][next_state[1]][
                                                                          next_action.value] - Q_value)

  agent.updateState(next_state)   # new state is updated
  agent.updatePosition()          # agent's position is updated

  return next_action


# q(a,s) = 1- alpha * old_q(a,s) + alpha *[ Reward + discount * MAX_q)a',s')
def Q_learning(learning_rate, discount_rate, agent):
  row = agent.position[0]
  col = agent.position[1]
  position = agent.position

  possible_actions = getAllPossibleNextAction(position)           # possible actions in state
  action = getPolicyAction(agent, agent.state, possible_actions)  # a = action chosen in state
  next_state = getNextState(agent, agent.state, action)                  # s' = next state after action is applied

  new_row = next_state[0]
  new_col = next_state[1]

  if (not agent.hasBlock()):
    old_value = pickup_q_table[row][col][action.value]
    next_max = np.max(pickup_q_table[new_row][new_col])
    new_q_value = (1 - learning_rate) * old_value + learning_rate * (agent.reward + discount_rate * next_max)
    pickup_q_table[row][col][action.value] = new_q_value
  else:
    old_value = dropoff_q_table[row][col][action.value]
    next_max = np.max(dropoff_q_table[new_row][new_col])
    new_q_value = (1 - learning_rate) * old_value + learning_rate * (agent.reward + discount_rate * next_max)
    dropoff_q_table[row][col][action.value] = new_q_value


  #print(f'Q({action.name}, {agent.state}) = {pickup_q_table[row][col][action.value]}')

  agent.updateState(next_state)
  agent.updatePosition()         # agent's position is updated


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
  for index in range(200):
    agent.policy = "PRandom"
    SARSA_update(learning_rate, discount_rate, None,agent)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    SARSA_update(learning_rate, discount_rate,None ,agent)

  #TODO final Q_table

def experiments_4():
  learning_rate = 0.3
  discount_rate = 1
  for index in range(200):
    agent.policy = "PRandom"
    SARSA_update(learning_rate, discount_rate, None, agent)

  # TODO Display and interpret the Q-table

  for index in range(7800):
    agent.policy = "PExploit"
    SARSA_update(learning_rate, discount_rate, None, agent)

  # TODO final Q_table


def experiment_5():
  pass



#--------- MAIN ----------#
if __name__ == '__main__':
  print()
  experiment_1()

  # print("Sarsa")
  # print("STEP 1")
  # print("Current state: ", agent.state)
  # next_action = SARSA_update(learning_rate, discount_rate, None, agent)
  # print("New state: ", agent.state)
  #
  # for i in range(999):
  #   print("\nSTEP ", 2 + i)
  #   print("Current state: ", agent.state)
  #   next_action = SARSA_update(learning_rate, discount_rate, next_action, agent)
  #   print("New state: ", agent.state)
  #
  # print("\n")
  #
  # print("Q TABLE")
  # for row in range(5):
  #   for column in range(5):
  #     print(pickup_q_table[row][column], end=" ")
  #   print()
