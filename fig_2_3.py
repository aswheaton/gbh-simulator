import numpy as np
import matplotlib.pyplot as plt

def analytic_soln(x, t, v_d=0.001, n_max=25):
	soln = 0.0
	for n in range(1, n_max):
		soln += 2.0 * np.sin(n * np.pi / 2)* np.sin(np.pi * n * x) * np.exp(-np.pi**2.0 * n**2.0 * v_d * t)
	return(soln)

# Return the forward difference approximation in time for a spatially dependent
# function u(x), for some discretization delta_x, and time interval delta_t for
# all spatial grid points j.
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

	# Initial conditions and parameters for the integration.
	x_start = 0.0
	x_stop = 1.5
	delta_x = 0.002

	# Plot the analytical solution at t=1.0 and t=3.0.
	positions = np.linspace(x_start, x_stop, num=((x_stop - x_start) / delta_x))
	u_analytic_t1 = analytic_soln(positions, 1.0)
	u_analytic_t3 = analytic_soln(positions, 3.0)
	plt.plot(positions, u_analytic_t1, label='t=1.0, Analytical')
	plt.plot(positions, u_analytic_t3, label='t=3.0, Analytical')

	# Perform the integration from t=1.0 to t=3.0, for various delta_t and plot
	# the results.
	t_start, t_stop = 1.0, 3.0
	for delta_t in [0.2,0.1,0.05]:
		# Advance the numerical solution to some smooth state analytically.
		u_numerical = analytic_soln(positions, t_start)

		# Compute the rest numerically by calling the forward_time_diff function.
		for t in np.linspace(t_start, t_stop, num=((t_stop - t_start) / delta_t)):
			u_numerical = forward_time_diff(u_numerical, delta_x, delta_t)
		errors = abs(u_numerical - analytic_soln(positions, t_stop)) / analytic_soln(positions, t_stop)
		plt.plot(positions, u_numerical, label='t=3.0, $\Delta$t='+str(delta_t))
		plt.plot(positions, errors, label='$\epsilon$, t=3.0, $\Delta$t='+str(delta_t))

	plt.legend()
	plt.show()

	# Initial conditions and parameters for the integration.
	# delta_t = 0.2
	# delta_x = [0.02, 0.01, 0.005]

main()
