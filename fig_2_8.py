import numpy as np
import matplotlib.pyplot as plt

NX=400
NT=140

# Create a wavepacket in the center of the spatial integration range.
pressure = np.zeros()
pressure[150:250] = 1.05 * np.cos(np.linspace(-np.pi/2.0, np.pi/2.0, 100))

phi = np.zeros([NT,NX])
phi[0]=pressure

v_1 = 0.001
rho_0 = 1.0
c_s = 1.0
v=np.ones(NX)*v1
psi=np.zeros([NT,NX])
psi[0]=v*rho0*cs
# staggering does not really change much in the code
# as j+1/2,j-1/2 is equivalent to j+1,j
for t in range(1,NT):
	psi[t,:-1]=psi[t-1,:-1]-s*(phi[t-1,1:]-phi[t-1,:-1])
	phi[t,1:]=phi[t-1,1:]-s*(psi[t,1:]-psi[t,:-1])
	psi[t,-1]=v1
	phi[t, 0]=0

	###
    fig, ax = plt.subplots(2)
	ax[0].plot(phi[0], "-.",markersize=.5,label="Initial pressure")
	ax[0].plot(phi[-1],"-o",markersize=.5,c="red", label="final pressure")
	# since rho0=cs=1, psi is same as density, add arbitrary scaling for values to much
	plt.plot(psi[-1]*2,"-",markersize=.0001,c="green", label="velocity(arbitrary normalization")
	plt.text(325,-0.5, "s={}".format(s))
	plt.xlabel("$x/\Delta x$")
	plt.ylabel("$pressure,v$")
	plt.legend()
	iplot+=1
plt.tight_layout()
plt.show()
