#esta es la grafica para primer orden
import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("datos18.txt")

x=data[:, 0]
y=data[:, 1]

x1=np.linspace(0, 3, 100)
y1=[]
for i in x1:
	y2=np.exp(-i)
	y1.append(y2)

plt.figure()
plt.scatter(x, y)
plt.plot(x1, y1)
plt.savefig("ejer18.png")



