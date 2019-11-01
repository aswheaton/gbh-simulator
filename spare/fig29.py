import numpy as np 
import matplotlib.pyplot as plt 

###############################
### NOTE: It ain't working ####
###############################

def analytic(x,t):
	w=1-x
	wseries=0
	for n in range(1,100):
		wseries+=np.sin(n*np.pi*x)*np.exp(-n*n*np.pi*np.pi*t)/n
	return w-wseries*2/np.pi

def integrate():
	# parameters
	dx=0.025
	dt=.03
	N_X=int(1 / dx)
	N_T=int(0.1 / dt)
	vd=1
	# initialize
	x = np.arange(0,1,dx)
	u_num=np.zeros([N_T,N_X])
	u_num[0,:]=analytic(x,0.2)
	print(u_num[0])
	u_ana=analytic(x,.3)
	for t in range(1,N_T):
		u_num[t]=u_num[t-1]
		u_num[t,1:-1] = u_num[t-1,1:-1]+dt / (dx*dx) * (u_num[t-1,2:]+u_num[t-1,:-2] - 2*u_num[t-1,1:-1])
		for _ in range(30):
			u_old = u_num[t].copy()
			u_num[t,1:-1] = u_num[t-1,1:-1]+dt / (dx*dx) * (u_old[2:]+u_old[:-2] - 2*u_old[1:-1])

	return x,{
		"analytic":u_ana,
		"numerical":u_num[N_T-1],
	}


x,u=integrate()
# plt.plot(x,u["analytic"])
plt.plot(x,u["numerical"])

plt.legend()
plt.show()