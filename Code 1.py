import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

no_of_simulations = [100, 1000, 10000]

States = ['Bull', 'Bear', 'Stagnant']
States_1 = [0, 1, 2]

"""
0 - BULL STATE
1 - BEAR STATE
2 - STAGNANT STATE
"""

Y = [0, 0, 0]  # frequency
transition_matrix = np.array([[0.9, 0.075, 0.025], [0.15, 0.8, 0.05], [0.5, 0.25, 0.25]])

Starting_State = 2
Current_State = Starting_State

n = 10000

for i in range(n):
    next_state = np.random.choice([0, 1, 2], p=transition_matrix[Current_State])
    Y[next_state] += 1
    Current_State = next_state

plt.bar(States, Y)
plt.xlabel('STATES')
plt.ylabel('FREQUENCY')
plt.title('FREQUENCY GRAPH WHEN STARTING STATE IS "STAGNANT" AND NO OF SIMULATIONS = ' + str(n))
for i in range(3):
    plt.text(i, Y[i], Y[i], ha='center')
plt.show()
