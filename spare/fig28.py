import numpy as np 
import matplotlib.pyplot as plt 

NX=400
NT=140

iplot=1
for s in [1,1.0001]:
	# init phi
	P=np.zeros(NX)
	# trick to get it look like wavepacket
	P[150:250]=np.cos(np.linspace(-np.pi/2,np.pi/2,100))*1.05
	phi=np.zeros([NT,NX])
	phi[0]=P


	v1  =0.001
	rho0=1
	cs  =1
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

	plt.subplot(1,2,iplot)
	plt.plot(phi[0], "-.",markersize=.5,label="Initial pressure")	
	plt.plot(phi[-1],"-o",markersize=.5,c="red", label="final pressure")
	# since rho0=cs=1, psi is same as density, add arbitrary scaling for values to much
	plt.plot(psi[-1]*2,"-",markersize=.0001,c="green", label="velocity(arbitrary normalization")
	plt.text(325,-0.5, "s={}".format(s))
	plt.xlabel("$x/\Delta x$")
	plt.ylabel("$P,v$")
	plt.legend()
	iplot+=1
plt.tight_layout()
plt.show()
