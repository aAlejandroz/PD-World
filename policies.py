from pd_main import *
import random

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