import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

pi = np.array([0, 0, 0, 0, 1])
P = np.zeros([5, 5])

l = [0.407407,
     0.120370,
     0.041667,
     0.092593,
     0.337963,
     0.438596,
     0.122807,
     0.035088,
     0.052632,
     0.350877,
     0.533333,
     0.133333,
     0,
     0.066667,
     0.266667,
     0.297872,
     0.063830,
     0.021277,
     0.085106,
     0.531915,
     0.453039,
     0.104972,
     0.016575,
     0.099448,
     0.325966]

row = 0
col = 0
for i in l:
    P[row][col] = i
    if col < 4:
        col += 1
    else:
        row += 1
        col = 0

print(P)

pi_5 = np.matmul(pi, np.linalg.matrix_power(P, 1))
pi_10 = np.matmul(pi, np.linalg.matrix_power(P, 5))
pi_15 = np.matmul(pi, np.linalg.matrix_power(P, 10))

hg = np.array([pi_5[0], pi_10[0], pi_15[0]])
lg = np.array([pi_5[1], pi_10[1], pi_15[1]])
nc = np.array([pi_5[2], pi_10[2], pi_15[2]])
ll = np.array([pi_5[3], pi_10[3], pi_15[3]])
hl = np.array([pi_5[4], pi_10[4], pi_15[4]])

x = ["1 DAY", "5 DAYS", "10 DAYS"]

plt.bar(x, hg, color='r')
plt.bar(x, lg, bottom=hg, color='b')
plt.bar(x, nc, bottom=hg + lg, color='y')
plt.bar(x, ll, bottom=hg + lg + nc, color='g')
plt.bar(x, hl, bottom=hg + lg + nc + ll, color='cyan')

plt.xlabel("TIME")
plt.ylabel("PROBABILITY")
plt.legend(["High Gain", "Low Gain", "No Change", "Low Loss", "High Loss"])
plt.show()
