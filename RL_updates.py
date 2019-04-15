# from pd_main import *
# from cell_methods import *
#
# # Q Learning update #
# def Q_learning(learning_rate, discount_rate, agent, pickup_states, dropoff_states):
#   position = agent.position
#   row = position[0]
#   col = position[1]
#
#   possible_actions = getAllPossibleNextAction(position)                                          # possible actions in state
#   action = getPolicyAction(agent, agent.state, possible_actions, pickup_states, dropoff_states)  # a = action chosen in state
#   next_state = getNextState(agent.state, action)                                                 # s' = next state after action is applied
#   reward = calculateRewardFromAction(action)                                                     # calculate agent's rewards & bank account
#   agent.updateRewards(reward)
#
#   new_row = next_state[0]
#   new_col = next_state[1]
#
#   q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table
#
#   old_value = q_table[row][col][action.value]
#   next_max = np.max(q_table[new_row][new_col])
#   new_q_value = (1 - learning_rate) * old_value + learning_rate * (agent.reward + discount_rate * next_max)
#   q_table[row][col][action.value] = new_q_value
#
#   agent.updateState(next_state)
#   agent.updatePosition()
#
#   is_terminal = False
#   val = 0
#
#   for cell in dropoff_cells:
#     val += cell.num_of_blocks
#     if val == 15:
#       is_terminal = True
#
#   if is_terminal:
#     agent.initialize()
#     initalizeCells(pickup_states, dropoff_states)
#     print("\n-----------INITIALIZED----------")
#
#
#
# # SARSA update, returns next action #
# def SARSA_update(learning_rate, discount_rate, next_action, agent, pickup_states, dropoff_states):
#   position = agent.position
#   row = position[0]
#   col = position[1]
#
#   if next_action is None:
#     possible_actions = getAllPossibleNextAction(position)                                                  # possible actions in state
#     action = getPolicyAction(agent, agent.state, possible_actions, pickup_states, dropoff_states)          # a = action chosen in state
#   else:
#     action = next_action                                                    # we know what our action is, so we chose it
#
#   reward = calculateRewardFromAction(action)                                # calculate agent's rewards & bank account
#   agent.updateRewards(reward)
#
#   next_state = getNextState(agent.state, action)                            # s' = next state after action is applied
#   next_possible_actions = getAllPossibleNextAction(next_state)              # all possible actions in s'
#   next_action = getPolicyAction(agent, next_state, next_possible_actions, pickup_states, dropoff_states)   # a' = next action in s'
#
#   q_table = dropoff_q_table if agent.hasBlock() else pickup_q_table
#   q_value = q_table[row][col][action.value]
#
#   q_table[row][col][action.value] = q_value + learning_rate * (reward + discount_rate *
#                                                                 q_table[next_state[0]][next_state[1]][next_action.value] - q_value)
#
#   agent.updateState(next_state)
#   agent.updatePosition()
#
#   return next_action
#
