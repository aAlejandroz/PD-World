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
