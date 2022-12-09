import numpy as np
import matplotlib.pyplot as plt
import time

# Parameters:
#   dx         = data x
#   dy         = data y
#   n          = hidden layer size
#   plot       = draw plot at end?
#   use_preset = 1 => preset in 1a
#                2 => preset in 1b
def BeSmart(dx, dy, n, plot=False, use_preset=0):
  start = time.process_time() # Start Timer

  # Get Data-related variables
  dlen = len(dx)
  two_over_m = 2 / dlen

  ### Network Initialization
  w1 = np.random.normal(0, 1, size=(n, 1)) # Weights for In -> Hidden
  w2 = np.random.normal(0, 1, size=(n, 1)) # Weights for Hidden -> Out
  bh = np.zeros((n, 1), dtype=np.float64)  # Hidden Bias
  bo = 0.0                                 # Output Bias
  eta = 0.001                              # Learning Rate

  # Presets Defined in Final instructions
  if use_preset == 1:
    w1 = np.array([[-0.94], [0.32]])
    w2 = np.array([[0.87], [-0.68]])
  elif use_preset == 2:
    w1 = np.array([
      [-1.27], [ 1.13], [-1.00], [-1.06], [ 0.86],
      [ 0.79], [-0.08], [ 0.21], [-0.79], [ 0.09]
    ])
    w2 = np.array([
      [ 0.95], [-0.13], [ 1.28], [-1.89], [ 0.40],
      [ 0.32], [ 1.73], [ 0.91], [-0.97], [ 0.69]
    ])

  k = 0               # Iteration Tracker
  max_iters = 1000000 # Iters before stopping gradient descent
  threshold = 1e-6    # Threshold for stopping gradient descent

  ### Training Loop
  prev_mse = 0
  mse = 1
  for k in range(max_iters):
    ### Evaluate network
    # column vectors are (i * w1) + bh for i in dx
    x = (w1 * dx) + bh
    
    # softplus of x
    h = np.log(1 + np.exp(x))

    # Gets final output and error for each data point
    o = (h * w2).sum(axis=0) + bo
    error = dy - o

    ### Update MSE
    prev_mse = mse
    mse = np.power(error, 2).sum() / dlen

    ### Gradient Descent

    sig = np.exp(x) / (1 + np.exp(x)) # Logistic of x
    repeated = error * sig
    
    # Get Gradients
    #         -(2/M)      * w2 * sum( (y-p) * exp(x)/(1+exp(x)) * in )
    grad_w1 = -two_over_m * w2 * (repeated * dx).sum(axis=1, keepdims=True)

    #         -(2/M)      * sum( (y-p) * a )
    grad_w2 = -two_over_m * (error * h).sum(axis=1, keepdims=True)

    #         -(2/M)      * w2 * sum( (y-p) * exp(x)/(1+exp(x)) * 1 )
    grad_bh = -two_over_m * w2 * repeated.sum(axis=1, keepdims=True)

    #         -(2/M)      * sum( (y-p) )
    grad_bo = -two_over_m * error.sum()

    # Perform Gradient Descent
    w1 -= eta * grad_w1
    w2 -= eta * grad_w2
    bh -= eta * grad_bh
    bo -= eta * grad_bo

    # Check if done
    if (abs(prev_mse - mse) < threshold):
      break;

  end = time.process_time() # Get Elapsed Time

  if plot:
    domain = np.linspace(0, 11, 50)
    outs = (np.log(1 + np.exp((w1 * domain) + bh)) * w2).sum(axis=0) + bo
    plt.plot(domain, outs)
    plt.plot(dx, dy, 'ro')
    plt.show()

  return [
    np.concatenate((w1, w2)).flatten(), # Weights
    np.append(bh, bo),                  # Biases
    k + 1,                              # Num Iters (k initially 0 hence +1)
    mse,                                # MSE
    end - start                         # Elapsed Time
  ]
