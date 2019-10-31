import numpy as np
import matplotlib.pyplot as plt

def analytic_soln(NX=50,v_d=0.001,n_max=25,t=1):
	x = np.linspace(0.0, 1.0, NX)
	w = np.zeros(NX)
	for n in range(n_max):
		w += 2.0 * np.sin(n * np.pi / 2)* np.sin(np.pi * n * x) * np.exp(-np.pi**2.0 * n**2.0 * v_d * t)
	return(x, w)

# Return the forward difference approximation for the space derivative of an
# arbitrary discretized function, for some interval delta_x, and about the
# spatial grid point j.
def 2d_forward_time_diff():
    func_next = func + (v_d * delta_t / delta_x**2.0) * (func_next + func_last - 2 * func)
    return(func_next)
