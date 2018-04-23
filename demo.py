import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#import seaborn as sns
np.set_printoptions(threshold=np.inf)
mpl.rcParams['lines.markersize'] = 10

all_packets = 240*4;

arr = np.ones((5, 310), dtype=int)
count_miss=0;
undecode = np.zeros((1,310),dtype=int)
undecode_pkt=0;
miss_frame=0

#for i in range(4):
#	arr[0][i] = 'layer%d' %i

for line in open('receivedtrace.txt'):
	if(int(line.split()[1]) <= 10):
		arr[0][int(line.split()[8])] = 0
	else:
		arr[int(line.split()[4])+1][int(line.split()[8])] = 0
	print(line.split()[4], line.split()[8])
#for i in range(150):
#    arr[0][2*i] = 1


for i in range(5):
	for j in range(240):
		if(arr[i][j]==1):
			count_miss=count_miss+1
			undecode[0][j]=undecode[0][j]+1
		else:
			if(undecode[0][j]>0):
				undecode_pkt=undecode_pkt+1

for i in range(240):
	if(undecode[0][i]==5):
		miss_frame=miss_frame+1;
				


count_receive=all_packets-count_miss;

print (arr)
labels = ['H', 'L0', 'L1', 'L2', 'L3']

plt.imshow(arr, interpolation='nearest', cmap=plt.cm.Pastel1, aspect='auto')
plt.yticks(range(arr.shape[0]), labels, fontsize=20)
#plt.plot(x,y,'rs')

plt.axis([-1,240,-1,6])
plt.xlabel('Frame',fontsize=18)
plt.xticks(fontsize=12)
plt.text(100,5.5,'Received Pkts:'+ str(count_receive),fontsize=16)
plt.text(100,5.1,'Missed Pkts:'+ str(count_miss),fontsize=16)
plt.text(100,4.7,'Missed Frames:' + str(miss_frame),fontsize=16)
plt.text(100,4.3,'Undecodable Pkts:'+str(undecode_pkt),fontsize=16)
#ax = plt.subplots()
#heatmap = plt.pcolor(x,y)
plt.show()
