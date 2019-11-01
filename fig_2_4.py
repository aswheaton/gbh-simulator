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

def scheme_233(func_last, diff_eq, delta_t):
    func_next = 2.0 * delta_t * diff_eq + func_last
    return(func_next)

def main():

    fig, ax = plt.subplots(2, 2)

    # Initial conditions and parameters for the integration.
    delta_t = 1.5
    time_n = np.linspace(0.0, 12.0, num=12.0/delta_t)
    forw_int_func_t15, back_int_func_t15, cent_int_func_t15 = [1.0], [1.0], [1.0]

    # Call each integration method at each timestep.
    for t in time_n[1:]:
        u_current = forw_int_func_t15[-1]
        diff_eq_current = - u_current
        forw_int_func_t15.append(forward_time_diff(u_current, diff_eq_current, delta_t))

        u_current = back_int_func_t15[-1]
        diff_eq_next = - u_current / (1.0 + delta_t)
        back_int_func_t15.append(backward_time_diff(u_current, diff_eq_next, delta_t))

        u_current = cent_int_func_t15[-1]
        diff_eq_current = - u_current
        diff_eq_next = - (u_current + (-u_current * delta_t / 2.0)) / (1.0 + delta_t)
        cent_int_func_t15.append(centered_time_diff(u_current, diff_eq_current, diff_eq_next, delta_t))

    ax[0][0].plot(time_n, forw_int_func_t15)
    ax[0][0].plot(time_n, back_int_func_t15)
    ax[0][0].plot(time_n, cent_int_func_t15)
    ax[0][0].plot(time_n, np.exp(-time_n), 'r')
    ax[0][0].set_xlim([0.0, 12.0])
    ax[0][0].set_ylim([-1.5, 1.5])
    ax[0][0].set_xlabel('t')
    ax[0][0].set_ylabel('u(t)')

    delta_t = 2.05
    time_n = np.linspace(0.0, 12.0, num=12.0/delta_t)
    forw_int_funct_205, back_int_funct_205, cent_int_funct_205 = [1.0], [1.0], [1.0]

    # Call each integration method at each timestep.
    for t in time_n[1:]:
        u_current = forw_int_funct_205[-1]
        diff_eq_current = - u_current
        forw_int_funct_205.append(forward_time_diff(u_current, diff_eq_current, delta_t))

        u_current = back_int_funct_205[-1]
        diff_eq_next = - u_current / (1.0 + delta_t)
        back_int_funct_205.append(backward_time_diff(u_current, diff_eq_next, delta_t))

        u_current = cent_int_funct_205[-1]
        diff_eq_current = - u_current
        diff_eq_next = - (u_current + (-u_current * delta_t / 2.0)) / (1.0 + delta_t)
        cent_int_funct_205.append(centered_time_diff(u_current, diff_eq_current, diff_eq_next, delta_t))

    ax[0][1].plot(time_n, forw_int_funct_205)
    ax[0][1].plot(time_n, back_int_funct_205)
    ax[0][1].plot(time_n, cent_int_funct_205)
    ax[0][1].plot(time_n, np.exp(-time_n), 'r')
    ax[0][1].set_xlim([0.0, 12.0])
    ax[0][1].set_ylim([-1.5, 1.5])
    ax[0][1].set_xlabel('t')

    delta_t = 0.45
    time_n = np.linspace(0.0, 12.0, num=12.0/delta_t)
    scheme_233_int_func_t045 = [1.0, np.exp(-time_n[1])]

    # Call each integration method at each timestep. Calculate and record errors.
    for t in time_n[2:]:
        u_last = scheme_233_int_func_t045[-2]
        diff_eq_current = -scheme_233_int_func_t045[-1]
        scheme_233_int_func_t045.append(scheme_233(u_last, diff_eq_current, delta_t))

    ax[1][0].plot(time_n, scheme_233_int_func_t045)
    ax[1][0].plot(time_n, np.exp(-time_n), 'r')
    ax[1][0].set_xlim([0.0, 12.0])
    ax[1][0].set_ylim([-1.5, 1.5])
    ax[1][0].set_xlabel('t')
    ax[1][0].set_ylabel('u(t)')

    delta_t = 0.045
    time_n = np.linspace(0.0, 12.0, num=12.0/delta_t)
    scheme_233_int_func_t0045 = [1.0, np.exp(-time_n[1])]

    # Call each integration method at each timestep. Calculate and record errors.
    for t in time_n[2:]:
        u_last = scheme_233_int_func_t0045[-2]
        diff_eq_current = -scheme_233_int_func_t0045[-1]
        scheme_233_int_func_t0045.append(scheme_233(u_last, diff_eq_current, delta_t))

    ax[1][1].plot(time_n, scheme_233_int_func_t0045)
    ax[1][1].plot(time_n, np.exp(-time_n), 'r')
    ax[1][1].set_xlim([0.0, 12.0])
    ax[1][1].set_ylim([-1.5, 1.5])
    ax[1][1].set_xlabel('t')

    plt.show()

    fig.savefig('fig_2_4.jpg')

main()
