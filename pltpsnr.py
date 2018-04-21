import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os, sys

np.set_printoptions(threshold=np.inf)
mpl.rcParams['lines.markersize'] = 1

arr = np.zeros((1,310), dtype=float)
c = 0;

readFile = open('psnrtrace.txt')
lines = readFile.readlines()
readFile.close()
w = open('psnredit.txt','w')
w.writelines([item for item in lines[:-3]])
w.close()


for line in open('psnredit.txt'):
	string = str(line.split()[1])
	tmp = string[:2]+"."+string[3:]
	#print(c)
	#print(tmp)
	arr[0,c] = float(tmp)
	c = c+1

x = [i+1 for i in range(1,311)]
y = arr[0,:]

plt.plot(x,y)
plt.axis([-1,c-1,-1,60])
plt.xlabel('Frame Number')
plt.ylabel('PSNR')

plt.show()



