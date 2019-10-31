import numpy as np
import matplotlib.pyplot as plt

# Return the forward difference approximation for a function at a given point
# for a given differential equation and timestep.
def forward_time_diff(func, diff_eq, delta_t):
    func_next = func + diff_eq * delta_t
    return(func_next)

# Return the forward difference approximation for a function at a given point
# for a given differential equation and timestep.
def backward_time_diff(func, diff_eq_next, delta_t):
    func_next = func + diff_eq_next * delta_t
    return(func_next)

# Return the forward difference approximation for a function at a given point
# for a given differential equation and timestep.
def centered_time_diff(func, diff_eq, diff_eq_next, delta_t):
    func_next = func + 0.5 * (diff_eq + diff_eq_next) * delta_t
    return(func_next)

def main():
    # Initial conditions and parameters for the integration.
    delta_t = 0.2
    time_n = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6]
    forw_int_func, back_int_func, cent_int_func = [1.0], [1.0], [1.0]
    forw_err, back_err, cent_err = [0.0], [0.0], [0.0]

    # Call each integration method at each timestep. Calculate and record errors.
    for t in time_n[1:]:
        u_current = forw_int_func[-1]
        diff_eq_current = - u_current
        forw_int_func.append(forward_time_diff(u_current, diff_eq_current, delta_t))
        forw_err.append((forw_int_func[-1] - np.exp(-t)) / np.exp(-t))

        u_current = back_int_func[-1]
        diff_eq_next = - u_current / (1.0 + delta_t)
        back_int_func.append(backward_time_diff(u_current, diff_eq_next, delta_t))
        back_err.append((back_int_func[-1] - np.exp(-t)) / np.exp(-t))

        u_current = cent_int_func[-1]
        diff_eq_current = - u_current
        diff_eq_next = - (u_current + (-u_current * delta_t / 2.0)) / (1.0 + delta_t)
        cent_int_func.append(centered_time_diff(u_current, diff_eq_current, diff_eq_next, delta_t))
        cent_err.append((cent_int_func[-1] - np.exp(-t)) / np.exp(-t))

    # Plot the integrated functions and their errors on separate axes.
    fig, ax = plt.subplots(2)
    ax[0].plot(time_n, forw_int_func)
    ax[0].plot(time_n, back_int_func)
    ax[0].plot(time_n, cent_int_func)
    ax[1].plot(time_n, forw_err)
    ax[1].plot(time_n, back_err)
    ax[1].plot(time_n, cent_err)
    plt.show()

main()
