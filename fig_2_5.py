import numpy as np
import matplotlib.pyplot as plt

def analytic_soln(x, t, v_d=0.001, n_max=25):
	soln = 0.0
	for n in range(1, n_max):
		soln += 2.0 * np.sin(n * np.pi / 2)* np.sin(np.pi * n * x) * np.exp(-np.pi**2.0 * n**2.0 * v_d * t)
	return(soln)

def forward_time_diff(u_num, delta_x, delta_t, v_d=0.001):
	u_num_next = []
	for j in range(len(u_num)):
		if j != 0 and j != (len(u_num) - 1):
			u_num_next.append(u_num[j]
			+ (v_d * delta_t / delta_x**2.0)
			* (u_num[j+1] + u_num[j-1] - 2.0 * u_num[j]))
		else: # Boundary condition always sets first and last item of u to 0.0.
			u_num_next.append(0.0)
	return(np.array(u_num_next))

def main():

    delta_x, delta_t = 0.02, 0.2
    x_start, x_stop = 0.0, 1.0

    positions = np.linspace(x_start, x_stop, num=((x_stop - x_start) / delta_x))

	# Perform the integration from t=1.0 to t=3.0, for various delta_t and plot
	# the results.
    t_start, t_stop = 0.0, 1.0
	# Advance the numerical solution to some smooth state analytically.
    u_numerical = analytic_soln(positions, t_start)
	# Compute the rest numerically by calling the forward_time_diff function.
    for t in np.linspace(t_start, t_stop, num=((t_stop - t_start) / delta_t)):
		u_numerical = forward_time_diff(u_numerical, delta_x, delta_t)
    plt.plot(positions, u_numerical, label='t='+str(t_stop)+', $\Delta$x=0.11')

    t_start, t_stop = 0.0, 3.0
	# Advance the numerical solution to some smooth state analytically.
    u_numerical = analytic_soln(positions, t_start)
	# Compute the rest numerically by calling the forward_time_diff function.
    for t in np.linspace(t_start, t_stop, num=((t_stop - t_start) / delta_t)):
		u_numerical = forward_time_diff(u_numerical, delta_x, delta_t)
    plt.plot(positions, u_numerical, label='t='+str(t_stop)+', $\Delta$x=0.19')

    t_start, t_stop = 0.0, 9.0
	# Advance the numerical solution to some smooth state analytically.
    u_numerical = analytic_soln(positions, t_start)
	# Compute the rest numerically by calling the forward_time_diff function.
    for t in np.linspace(t_start, t_stop, num=((t_stop - t_start) / delta_t)):
		u_numerical = forward_time_diff(u_numerical, delta_x, delta_t)
    plt.plot(positions, u_numerical, label='t='+str(t_stop)+', $\Delta$x=0.32')

    plt.legend()
    plt.show()

main()
