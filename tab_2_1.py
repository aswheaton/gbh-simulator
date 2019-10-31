import numpy as np
import matplotlib.pyplot as plt

# Spatially discretized natural exponential function.
def discrete_exp(j, delta_x):
    return(np.exp(j * delta_x))

# Return the forward difference approximation for the space derivative of an
# arbitrary discretized function, for some interval delta_x, and about the
# spatial grid point j.
def forward_diff_quot(func, j, delta_x):
    derivative_approx = (func(j + 1.0, delta_x) - func(j, delta_x)) / delta_x
    return(derivative_approx)

# Return the backward difference approximation for the space derivative of an
# arbitrary discretized function, for some interval delta_x, and about the
# spatial grid point j.
def backward_diff_quot(func, j, delta_x):
    derivative_approx = (func(j, delta_x) - func(j - 1.0, delta_x)) / delta_x
    return(derivative_approx)

# Return the centered difference approximation for the space derivative of an
# arbitrary discretized function, for some interval delta_x, and about the
# spatial grid point j.
def centered_diff_quot(func, j, delta_x):
    derivative_approx = (func(j + 0.5, delta_x) - func(j - 0.5, delta_x)) / delta_x
    return(derivative_approx)

def main():
    delta_x = [1.0, 0.1, 0.01, 0.001]
    j = 0.0 # Perform calculations about x=0. Must be float for center quotient!
    forward_approx, backward_approx, centered_approx = [], [], []
    for x in delta_x:
        forward_approx.append(forward_diff_quot(discrete_exp, j, x))
        backward_approx.append(backward_diff_quot(discrete_exp, j, x))
        centered_approx.append(centered_diff_quot(discrete_exp, j, x))

    # Print the results to console and save them to a file in tabular format.
    data = np.transpose(np.array([delta_x, forward_approx, backward_approx, centered_approx]))
    print(data)
    np.savetxt("table.csv", data, delimiter=' & ', fmt='%2.2e', newline=' \\\\\n')

main()
