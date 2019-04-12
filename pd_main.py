from agent import Agent
import random
import copy
import enum
# import numpy as np

# creating enumerations using class
class actions(enum.Enum):
  NORTH  = 0
  EAST   = 1
  SOUTH  = 2
  WEST   = 3
  PICKUP = 4
  DROP   = 5

pickup_matrix = [[[None, -1, -1, None], [None, -1, -1, 13], [None, -1, -1, -1], [None, -1, -1, -1], [None, None, -1, -1]],
                 [[13, -1, -1, None], [-1, -1, -1, -1], [-1, -1, 13, -1], [-1, -1, -1, -1], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, 13, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 13], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [13, -1, -1, -1], [-1, -1, -1, -1], [-1, None, 13, -1]],
                 [[-1, -1, None, None], [-1, -1, None, -1], [-1, -1, None, -1], [-1, 13, None, -1], [-1, None, None, -1]]]

q_table = [ [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]]

# 25 states with 6 actions
# new_q_table = np.zeros([25,6])
pickup_states = [[0, 0], [2, 2], [4, 4]]

learning_rate = 0.5
discount_rate = 1

agent = Agent()
agent.policy = "PRandom"

# returns action enum given agent's policy and possible actions
def getPolicyAction(agent, state, possible_actions):
  row = state[0]
  col = state[1]
  pos = [row, col]

  if pos in pickup_states and state[2] == 0:
    action = actions.PICKUP
    agent.bank_account += 13
    reward = 13
    # TODO: decrement blocks on space
  else:
    if agent.policy == "PRandom":
      action = actions(PRandom(possible_actions))
      agent.bank_account -= 1
      reward = -1
    # TODO: Add other policies
    # if policy == "PExploit":
    #   action = actions(exploitAction(possible_actions))
    # if policy == "PGreedy":
    #   action = actions(greedyAction(possible_actions))

  agent.reward = reward
  agent.num_operators += 1

  return action


# returns new state when action is applied to old state
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

# TODO: Q-Leaning update function


# updates q-value in q-table, returns next action
def SARSA_update(learning_rate, discount_rate, next_action, agent):
  row = agent.position[0]
  col = agent.position[1]
  position = agent.position

  if next_action is None:
    possible_actions = getAllPossibleNextAction(position)                   # possible actions in state
    action = getPolicyAction(agent, agent.state, possible_actions)          # a = action chosen in state
    next_state = getNextState(agent.state, action)                          # s' = next state after action is applied
  else:
    action = next_action                                                    # we know what our action is, so we chose it
    next_state = getNextState(agent.state, next_action)

# random policy
def PRandom(possible_actions):
  randomChoice = random.choice(possible_actions)
  return randomChoice

# updates q-value in q-table, returns next action
def SARSA_update(learning_rate, discount_rate, next_action, agent):
  row = agent.position[0]
  col = agent.position[1]
  position = agent.position

  if next_action is None:
    possible_actions = getAllPossibleNextAction(position)                   # possible actions in state
    action = getPolicyAction(agent, agent.state, possible_actions)          # a = action chosen in state
    next_state = getNextState(agent.state, action)                          # s' = next state after action is applied
  else:
    action = next_action                                                    # we know what our action is, so we chose it
    next_state = getNextState(agent.state, next_action)

  next_possible_actions = getAllPossibleNextAction(next_state)              # all possible actions in s'
  next_action = getPolicyAction(agent, next_state, next_possible_actions)   # a' = next action in s'

  # TODO: Fix duplicate pickup
  Q_value = q_table[row][col][action.value]
  print(f'Q({action.name}, {agent.state}) = {q_table[row][col][action.value]}')

  if action.value < 4:
    q_table[row][col][action.value] = Q_value + learning_rate * (pickup_matrix[row][col][action.value] + discount_rate *
                                   q_table[next_state[0]][next_state[1]][next_action.value] - Q_value)

  print(f'Q({action.name}, {agent.state}) = {q_table[row][col][action.value]}')

  agent.updateState(next_state)   # new state is updated
  agent.updatePosition()          # agent's position is updated

  return next_action

# q(a,s) = 1- alpha * old_q(a,s) + alpha *[ Reward + discount * MAX_q)a',s')
# def Q_learning(current_state,action,next_state):
#     current_reward = 10
#     learning_rate = 0.5
#     discount_rate = 0.5
#     old_value = new_q_table[current_state][action]
#     next_max = np.max(new_q_table[next_state])
#     new_q_value = (1 - learning_rate )* old_value + learning_rate*(current_reward + discount_rate * next_max)
#     new_q_table[current_state][action] = new_q_value
#     print(new_q_table)

#--------- MAIN ----------#
print("STEP 1")
print("Current state: ", agent.state)
next_action = SARSA_update(learning_rate, discount_rate, None, agent)
print("New state: ", agent.state)

for i in range(99):
  print("\nSTEP ",2 + i)
  print("Current state: ", agent.state)
  next_action = SARSA_update(learning_rate, discount_rate, next_action, agent)
  print("New state: ", agent.state)

print("\n")

print("Q TABLE")
for row in range(5):
  for column in range(5):
    print(q_table[row][column], end = " ")
  print()

# Q_learning(0,2,5)

