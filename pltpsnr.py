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

ava = np.mean(arr[0,0:249])
mini = 100
maxi = 0

for i in range(250):
	if(arr[0,i]>maxi):
		maxi=arr[0,i]
	if(arr[0,i]<mini):
		mini=arr[0,i]
	

x = [i+1 for i in range(1,250)]
y = arr[0,0:249]

plt.plot(x,y)
plt.axis([-1,250,10,50])
plt.xlabel('Frame',fontsize = 20)
plt.ylabel('PSNR in dB',fontsize = 20)
plt.hlines(ava,0,250,color="red",linestyles="dashed")
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)

plt.text(100,47,'Average:'+str(round(ava,2)),fontsize=16)
plt.text(100,44,'Minimum:'+str(round(mini,2)),fontsize=16)
plt.text(100,41,'Maximum'+str(round(maxi,2)),fontsize=16)

plt.show()



