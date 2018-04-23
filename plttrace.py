import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os, sys

np.set_printoptions(threshold=np.inf)
mpl.rcParams['lines.markersize'] = 1

arr = []
c = 0
for line in open('CREW52trace-rdo.txt'):
	if(int(line.split()[10]) < 10000):
		arr.append(int(line.split()[10]))
		print line.split()[10]

print arr
"""#x = [i+1 for i in range(1,250)]
#y = arr[0,0:249]

#plt.plot(x,y)
#plt.axis([-1,250,10,50])
#plt.xlabel('Frame',fontsize = 20)
#plt.ylabel('PSNR in dB',fontsize = 20)
#plt.hlines(ava,0,250,color="red",linestyles="dashed")
#plt.xticks(fontsize=12)
#plt.yticks(fontsize=14)
#
#plt.text(100,47,'Average:'+str(round(ava,2)),fontsize=16)
#plt.text(100,44,'Minimum:'+str(round(mini,2)),fontsize=16)
#plt.text(100,41,'Maximum'+str(round(maxi,2)),fontsize=16)"""

bins = [0]
for i in range(100):
	bins.append(i*50)

plt.hist(arr, bins = bins, cumulative=True)

plt.show()



