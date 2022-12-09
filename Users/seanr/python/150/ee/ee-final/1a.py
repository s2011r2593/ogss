import numpy as np

from nn import *

# Initialize input data
datax = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
datay = np.array([4.11, 6.07, 8.01, 9.46, 10.0, 9.46, 8.01, 6.07, 4.11, 2.49])

[w, b, k, mse, t] = BeSmart(
  datax, datay, # Pass in data
  2,            # Pass in N
  plot=True,    # Draw plot
  use_preset=1  # Uses predefined weights given in instructions
)

# Print result
print(f'Weights:\n{w}\nBiases:\n{b}\nIters: {k}\nMSE: {mse}')
