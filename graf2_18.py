#esta es la grafica para segundo orden
import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("datos182.txt")

x=data[:, 0]
y=data[:, 1]
z=data[:, 2]

x1=np.linspace(0, 10, 100)
y1=[]
for i in x1:
	y2=np.cos(i)
	y1.append(y2)

plt.figure()
plt.scatter(x, y, color="red", label="x contra y")
plt.legend()
plt.savefig("ejer182.png")

plt.clf()

plt.figure()
plt.scatter(y, z, label="y contra z")
plt.legend()
plt.savefig("ejer182.png")

plt.clf()

plt.figure()
plt.plot(x1, y1, label="teorica")
plt.legend()
plt.savefig("ejer182.png")



