from agent import Agent
import random
import copy
import numpy as np


pickup_matrix = [[[None, -1, -1, None], [None, -1, -1, 13], [None, -1, -1, -1], [None, -1, -1, -1], [None, None, -1, -1]],
                 [[13, -1, -1, None], [-1, -1, -1, -1], [-1, -1, 13, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]],
                 [[-1, -1, -1, None], [-1, 13, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 13], [-1, None, -1, -1]],
                 [[-1, -1, -1, None], [-1, -1, -1, -1], [13, -1, -1, -1], [-1, -1, -1, -1], [-1, None, 13, -1]],
                 [[-1, -1, None, None], [-1, -1, None, -1], [-1, -1, None, -1], [-1, 13, None, -1], [-1, None, None, -1]]]

#Q(a, s)
#Q(west, [0,4])
#q_table[0][4][3]

q_table = [ [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
            [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]]

#25 states with 6 actions
new_q_table = np.zeros([25,6])

actions = {
        0 : 'north',
        1 : 'east',
        2 : 'south',
        3 : 'west',
        4 : 'pickup',
        5 : 'drop'
      }

pickup_states = [[0, 0], [2, 2], [4, 4]]

learning_rate = None
discount_rate = None
current_reward = 0

agent = Agent()
agent.policy = "PRandom"

row = agent.new_state_space[0]
col = agent.new_state_space[1]
hasBlock = agent.new_state_space[2]
position = [row, col]

# TODO: pass in row to lookup in q-table
def get_PRandom_action(row, col, agent):
  agent.past_state_space = copy.deepcopy(agent.new_state_space)
  if (pickup_matrix[row][col] in pickup_states):
      agent.new_state_space[2] = 1       # pickup
      agent.bank_account += 13
      action = 4
    # TODO: decrement blocks on space
  else:
      possible_actions = []

      for i in range(4):
        if pickup_matrix[row][col][i] != None:
          possible_actions.append(i)

      randomChoice = random.choice(possible_actions)
      action = randomChoice
      current_reward = pickup_matrix[row][col][action]

      direction = actions.get(randomChoice)

      if direction == "north":

        agent.new_state_space[0] -= 1

      elif direction == "east":

        agent.new_state_space[1] += 1
      elif direction == "south":

        agent.new_state_space[0] += 1

      elif direction == "west":
        agent.new_state_space[1] -= 1

      agent.bank_account -= 1

  agent.num_operators += 1

  return action
# end PRandom

# TODO: update Q-value
# action = action
# state = agent.new_state_space
# def SARSA_update(action, state):


# q(a,s) = 1- alpha * old_q(a,s) + alpha *[ Reward + discount * MAX_q)a',s')

def Q_learning(current_state,action,next_state):
    current_reward = 10
    learning_rate = 0.5
    discount_rate = 0.5
    old_value = new_q_table[current_state][action]
    next_max = np.max(new_q_table[next_state])
    new_q_value = (1 - learning_rate )* old_value + learning_rate*(current_reward + discount_rate * next_max)
    new_q_table[current_state][action] = new_q_value
    print(new_q_table)



print("Current position: ", agent.new_state_space)
new_action = get_PRandom_action(row,col,agent)
print("New position: ", agent.new_state_space)

Q_learning(0,2,5)

# SARSA_update(action, agent.past_state_space)