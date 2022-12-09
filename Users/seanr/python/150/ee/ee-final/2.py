import matplotlib.pyplot as plt
import numpy as np

from nn import *

# Initialize input data
datax = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
datay = np.array([4.11, 6.07, 8.01, 9.46, 10.0, 9.46, 8.01, 6.07, 4.11, 2.49])

# Parameters given by instructions
n_start = 2
n_end = 10
num_trials = 10

n_range = range(n_start, n_end + 1)
inv_trials = 1 / num_trials

# Initialize averages
avg_k = np.array([0.0 for _ in n_range])
avg_mse = np.array([0.0 for _ in n_range])
avg_t = np.array([0.0 for _ in n_range])

# Sweep across values of N
for n in n_range:
  ind = n - n_start
  for trial in range(num_trials):
    print(f'N={n} Trial #{trial + 1}\033[K', end="\r")
    
    # Get [w, b, k, mse, t]
    res = BeSmart(datax, datay, n)

    # Add k, mse, and t to respective arrays @ ind corresponding to n
    avg_k[ind] += res[2]
    avg_mse[ind] += res[3]
    avg_t[ind] += res[4]

# Divide sums to find average
avg_k *= inv_trials
avg_mse *= inv_trials
avg_t *= inv_trials
  
# Plot Results
figure, axes = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

axes[0].plot(n_range, avg_k)
axes[0].set_ylabel("# of Iterations")
axes[0].set_xlabel("N Value")

axes[1].plot(n_range, avg_mse)
axes[1].set_ylabel("MSE Value")
axes[1].set_xlabel("N Value")

axes[2].plot(n_range, avg_t)
axes[2].set_ylabel("Process Runtime (s)")
axes[2].set_xlabel("N Value")

figure.tight_layout()
plt.show()
